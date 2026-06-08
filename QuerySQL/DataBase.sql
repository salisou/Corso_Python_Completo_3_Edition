CREATE DATABASE SistemaBancarioDefinitivo;
GO

USE SistemaBancarioDefinitivo;
GO

-- =========================================================================
-- 1. STRUTTURA DELLE TABELLE OPERATIVE (CORE BANKING)
-- =========================================================================

CREATE TABLE Filiali (
    IdFiliale INT IDENTITY(1,1) NOT NULL,
    CodiceFiliale AS ('FIL-' + RIGHT('000' + CAST(IdFiliale AS VARCHAR(10)), 3)) PERSISTED,
    NomeFiliale VARCHAR(100) NOT NULL,
    Citta VARCHAR(50) NOT NULL,
    CONSTRAINT PK_Filiali PRIMARY KEY (IdFiliale)
);

CREATE TABLE Clienti (
    IdCliente INT IDENTITY(1,1) NOT NULL,
    CodiceCliente AS ('CLI-' + RIGHT('000000' + CAST(IdCliente AS VARCHAR(10)), 6)) PERSISTED,
    Nome VARCHAR(50) NOT NULL,
    Cognome VARCHAR(50) NOT NULL,
    CodiceFiscale CHAR(16) NOT NULL UNIQUE,
    TipoCliente VARCHAR(15) NOT NULL CHECK (TipoCliente IN ('Privato', 'Business')),
    Email VARCHAR(100) NOT NULL,
    FilialeId INT NOT NULL,
    CONSTRAINT PK_Clienti PRIMARY KEY (IdCliente),
    CONSTRAINT FK_Clienti_Filiali FOREIGN KEY (FilialeId) REFERENCES Filiali(IdFiliale)
);

CREATE TABLE ContiCorrenti (
    IdConto INT IDENTITY(1,1) NOT NULL,
    IBAN CHAR(27) NOT NULL UNIQUE,
    ClienteId INT NOT NULL,
    SaldoContabile DECIMAL(18,2) NOT NULL DEFAULT 0.00,
    SaldoDisponibile DECIMAL(18,2) NOT NULL DEFAULT 0.00,
    StatoConto VARCHAR(15) NOT NULL DEFAULT 'Attivo' CHECK (StatoConto IN ('Attivo', 'Sospeso', 'Chiuso')),
    DataApertura DATE NOT NULL DEFAULT GETDATE(),
    CONSTRAINT PK_ContiCorrenti PRIMARY KEY (IdConto),
    CONSTRAINT FK_Conti_Clienti FOREIGN KEY (ClienteId) REFERENCES Clienti(IdCliente)
);

CREATE TABLE Carte (
    IdCarta INT IDENTITY(1,1) NOT NULL,
    NumeroCarta CHAR(16) NOT NULL UNIQUE,
    ContoId INT NOT NULL,
    TipoCarta VARCHAR(15) NOT NULL CHECK (TipoCarta IN ('Debito', 'Credito')),
    DataScadenza DATE NOT NULL,
    StatoCarta VARCHAR(15) NOT NULL DEFAULT 'Attiva',
    CONSTRAINT PK_Carte PRIMARY KEY (IdCarta),
    CONSTRAINT FK_Carte_Conti FOREIGN KEY (ContoId) REFERENCES ContiCorrenti(IdConto)
);

CREATE TABLE Transazioni (
    IdTransazione INT IDENTITY(1,1) NOT NULL,
    ContoId INT NOT NULL,
    TipoTransazione VARCHAR(25) NOT NULL CHECK (TipoTransazione IN ('Versamento', 'Prelevamento', 'Bonifico Uscita', 'Bonifico Entrata')),
    Importo DECIMAL(18,2) NOT NULL,
    DataOra DATETIME NOT NULL DEFAULT GETDATE(),
    Descrizione VARCHAR(255) NOT NULL,
    IBANControparte CHAR(27) NULL,
    CONSTRAINT PK_Transazioni PRIMARY KEY (IdTransazione),
    CONSTRAINT FK_Transazioni_Conti FOREIGN KEY (ContoId) REFERENCES ContiCorrenti(IdConto)
);

CREATE TABLE Prestiti (
    IdPrestito INT IDENTITY(1,1) NOT NULL,
    CodiceContratto AS ('LN-' + RIGHT('00000' + CAST(IdPrestito AS VARCHAR(10)), 5)) PERSISTED,
    ClienteId INT NOT NULL,
    ImportoErogato DECIMAL(18,2) NOT NULL,
    CapitaleResiduo DECIMAL(18,2) NOT NULL,
    CONSTRAINT PK_Prestiti PRIMARY KEY (IdPrestito),
    CONSTRAINT FK_Prestiti_Clienti FOREIGN KEY (ClienteId) REFERENCES Clienti(IdCliente)
);

-- =========================================================================
-- 2. TABELLA DI ARCHIVIAZIONE INDIPENDENTE (REPOSITORY XML)
-- =========================================================================

CREATE TABLE ClientiCancellati (
    IdArchivio INT IDENTITY(1,1) NOT NULL,
    IdClienteAnagrafica INT NOT NULL,
    CodiceCliente CHAR(10) NOT NULL,
    Nome VARCHAR(50) NOT NULL,
    Cognome VARCHAR(50) NOT NULL,
    DataCancellazione DATETIME NOT NULL DEFAULT GETDATE(),
    DatiCompletiXML XML NOT NULL,
    CONSTRAINT PK_ClientiCancellati PRIMARY KEY (IdArchivio)
);
GO

-- =========================================================================
-- 3. AUTOMAZIONE VIA TRIGGER (INSTEAD OF DELETE)
-- =========================================================================

CREATE TRIGGER TR_Anagrafica_IsolaEArchivia
ON Clienti
INSTEAD OF DELETE
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @IdCliente INT, @CodiceCliente VARCHAR(10), @Nome VARCHAR(50), @Cognome VARCHAR(50);
    SELECT @IdCliente = IdCliente, @CodiceCliente = CodiceCliente, @Nome = Nome, @Cognome = Cognome FROM deleted;

    IF @IdCliente IS NOT NULL
    BEGIN
        DECLARE @DatiXML XML;

        -- Generazione dell'intero schema relazionale del singolo cliente in un unico oggetto gerarchico XML
        SET @DatiXML = (
            SELECT 
                c.IdCliente, c.CodiceCliente, c.Nome, c.Cognome, c.CodiceFiscale, c.Email,
                (
                    SELECT cc.IdConto, cc.IBAN, cc.SaldoContabile, cc.SaldoDisponibile,
                        (
                            SELECT ca.IdCarta, ca.NumeroCarta, ca.TipoCarta, ca.DataScadenza FROM Carte ca WHERE ca.ContoId = cc.IdConto FOR XML PATH('Carta'), TYPE
                        ) AS ElencoCarte,
                        (
                            SELECT t.IdTransazione, t.TipoTransazione, t.Importo, t.DataOra, t.Descrizione FROM Transazioni t WHERE t.ContoId = cc.IdConto FOR XML PATH('Transazione'), TYPE
                        ) AS ElencoTransazioni
                    FROM ContiCorrenti cc WHERE cc.ClienteId = c.IdCliente FOR XML PATH('ContoCorrente'), TYPE
                ) AS ElencoConti,
                (
                    SELECT p.IdPrestito, p.CodiceContratto, p.ImportoErogato, p.CapitaleResiduo FROM Prestiti p WHERE p.ClienteId = c.IdCliente FOR XML PATH('Prestito'), TYPE
                ) AS ElencoPrestiti
            FROM Clienti c
            WHERE c.IdCliente = @IdCliente
            FOR XML PATH('ProfiloCliente'), TYPE
        );

        -- Inserimento nella tabella isolata
        INSERT INTO ClientiCancellati (IdClienteAnagrafica, CodiceCliente, Nome, Cognome, DatiCompletiXML)
        VALUES (@IdCliente, @CodiceCliente, @Nome, @Cognome, @DatiXML);

        -- Eliminazione manuale bottom-up per svuotare le relazioni attive senza ON DELETE CASCADE
        DELETE FROM Carte WHERE ContoId IN (SELECT IdConto FROM ContiCorrenti WHERE ClienteId = @IdCliente);
        DELETE FROM Transazioni WHERE ContoId IN (SELECT IdConto FROM ContiCorrenti WHERE ClienteId = @IdCliente);
        DELETE FROM ContiCorrenti WHERE ClienteId = @IdCliente;
        DELETE FROM Prestiti WHERE ClienteId = @IdCliente;
        DELETE FROM Clienti WHERE IdCliente = @IdCliente;
    END
END;
GO

-- =========================================================================
-- 4. VISTE (VIEWS) DI REPORTISTICA E MONITORAGGIO
-- =========================================================================

-- Vista Sintetica della Posizione Patrimoniale Globale di ogni cliente attivo
CREATE VIEW Vw_PosizioneGlobaleClienti AS
SELECT 
    c.CodiceCliente,
    c.Cognome + ' ' + c.Nome AS Nominativo,
    ISNULL(SUM(cc.SaldoDisponibile), 0) AS LiquiditaTotale,
    ISNULL(SUM(p.CapitaleResiduo), 0) AS DebitoResiduoPrestiti,
    COUNT(DISTINCT cc.IdConto) AS NumeroContiAttivi
FROM Clienti c
LEFT JOIN ContiCorrenti cc ON c.IdCliente = cc.ClienteId AND cc.StatoConto = 'Attivo'
LEFT JOIN Prestiti p ON c.IdCliente = p.ClienteId
GROUP BY c.CodiceCliente, c.Cognome, c.Nome;
GO

-- Vista di Alert per i Conti in Rosso (Fido o Scoperti)
CREATE VIEW Vw_ContiInRosso AS
SELECT 
    cc.IBAN,
    c.CodiceCliente,
    c.Cognome + ' ' + c.Nome AS Titolare,
    cc.SaldoContabile,
    f.NomeFiliale
FROM ContiCorrenti cc
JOIN Clienti c ON cc.ClienteId = c.IdCliente
JOIN Filiali f ON c.FilialeId = f.IdFiliale
WHERE cc.SaldoContabile < 0;
GO

-- =========================================================================
-- 5. STORED PROCEDURES (LOGICA DI BUSINESS)
-- =========================================================================

-- SP per l'inserimento sicuro di un nuovo Conto Corrente con validazione
CREATE PROCEDURE Sp_Conti_ApriNuovoConto
    @ClienteId INT,
    @IBAN CHAR(27),
    @StatoConto VARCHAR(15) = 'Attivo'
AS
BEGIN
    SET NOCOUNT ON;
    
    IF NOT EXISTS (SELECT 1 FROM Clienti WHERE IdCliente = @ClienteId)
    BEGIN
        RAISERROR('Errore: Cliente inesistente nell''anagrafica di sistema.', 16, 1);
        RETURN;
    END

    IF EXISTS (SELECT 1 FROM ContiCorrenti WHERE IBAN = @IBAN)
    BEGIN
        RAISERROR('Errore: L''IBAN specificato è già presente nel sistema.', 16, 1);
        RETURN;
    END

    INSERT INTO ContiCorrenti (IBAN, ClienteId, SaldoContabile, SaldoDisponibile, StatoConto)
    VALUES (@IBAN, @ClienteId, 0.00, 0.00, @StatoConto);
END;
GO

-- SP Transazionale per il Trasferimento Fondi (Bonifico Interno tra due conti)
CREATE PROCEDURE Sp_Transazioni_EseguiBonificoInterno
    @IBANOrdinante CHAR(27),
    @IBANBeneficiario CHAR(27),
    @Importo DECIMAL(18,2),
    @Causale VARCHAR(255)
AS
BEGIN
    SET NOCOUNT ON;
    
    -- Validazione input iniziale
    IF @Importo <= 0
    BEGIN
        RAISERROR('L''importo del bonifico deve essere maggiore di zero.', 16, 1);
        RETURN;
    END

    DECLARE @IdContoOrdinante INT, @IdContoBeneficiario INT;
    DECLARE @SaldoDispOrdinante DECIMAL(18,2);

    SELECT @IdContoOrdinante = IdConto, @SaldoDispOrdinante = SaldoDisponibile FROM ContiCorrenti WHERE IBAN = @IBANOrdinante AND StatoConto = 'Attivo';
    SELECT @IdContoBeneficiario = IdConto FROM ContiCorrenti WHERE IBAN = @IBANBeneficiario AND StatoConto = 'Attivo';

    IF @IdContoOrdinante IS NULL OR @IdContoBeneficiario IS NULL
    BEGIN
        RAISERROR('Uno o entrambi i conti non sono attivi o non esistono.', 16, 1);
        RETURN;
    END

    IF @SaldoDispOrdinante < @Importo
    BEGIN
        RAISERROR('Disponibilità insufficiente sul conto ordinante per eseguire l''operazione.', 16, 1);
        RETURN;
    END

    -- Apertura della Transazione ACID per garantire l'integrità dei dati
    BEGIN TRANSACTION;
    BEGIN TRY
        -- 1. Addebito Ordinante
        UPDATE ContiCorrenti 
        SET SaldoContabile = SaldoContabile - @Importo,
            SaldoDisponibile = SaldoDisponibile - @Importo
        WHERE IdConto = @IdContoOrdinante;

        -- 2. Accredito Beneficiario
        UPDATE ContiCorrenti 
        SET SaldoContabile = SaldoContabile + @Importo,
            SaldoDisponibile = SaldoDisponibile + @Importo
        WHERE IdConto = @IdContoBeneficiario;

        -- 3. Scrittura Storico Movimenti per l'Ordinante
        INSERT INTO Transazioni (ContoId, TipoTransazione, Importo, Descrizione, IBANControparte)
        VALUES (@IdContoOrdinante, 'Bonifico Uscita', @Importo, @Causale, @IBANBeneficiario);

        -- 4. Scrittura Storico Movimenti per il Beneficiario
        INSERT INTO Transazioni (ContoId, TipoTransazione, Importo, Descrizione, IBANControparte)
        VALUES (@IdContoBeneficiario, 'Bonifico Entrata', @Importo, @Causale, @IBANOrdinante);

        -- Tutto è andato a buon fine, salvataggio definitivo
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        -- In caso di qualsiasi anomalia hardware o software, ripristino lo stato iniziale dei conti
        ROLLBACK TRANSACTION;
        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        RAISERROR(@ErrorMessage, 16, 1);
    END CATCH
END;
GO