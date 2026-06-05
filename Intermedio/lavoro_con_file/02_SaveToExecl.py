import pandas as pd # per lavorare con i dataframe pip install pandas
import openpyxl  as pxl # per lavorare con i file excel pip install openpyxl


# Creazione del dataframe(clienti, e fornitori) = dataset(Tabella, Modello, Entity)
# nomin diversi per evitare confusione con il dataframe dipendenti
clienti = {
    "nome": ["Luca", "Giovanni", "Francesco", "Giulia", "Elena", "Federica", "Alessandro", "Simone", "Matteo", "Sara", "Andrea", "Valentina", "Davide", "Chiara", "Alessia" ,   "Federico", "Giorgia", "Lorenzo", "Martina", "Riccardo"],
    "cognome": ["Bianchi", "Neri", "Rossi", "Verdi", "Gialli", "Blu", "Rosa", "Grigio", "Viola", "Arancione", "Marrone", "Azzurro", "Giallo", "Turchese", "Fucsia" ,   "Lilla", "Indaco", "Smeraldo", "Zaffiro", "Rubino"],
    "email": ["luca.bianchi@email.com", "giovanni.neri@email.com", "francesco.rossi@email.com", "giulia.verdi@email.com", "elena.gialli@email.com", "federica.blu@email.com", "alessandro.rosa@email.com", "simone.grigio@email.com", "matteo.viola@email.com", "sara.arancione@email.com", "andrea.marrone@email.com", "valentina.azzurro@email.com", "davide.giallo@email.com", "chiara.turchese@email.com", "alessia.fucsia@email.com", "federico.lilla@email.com", "giorgia.indaco@email.com", "lorenzo.smeraldo@email.com", "martina.zaffiro@email.com", "riccardo.rubino@email.com"],
    "citta": ["Roma", "Napoli", "Torino", "Firenze", "Bologna", "Genova", "Padova", "Milano", "Biella", "San Donà di Piave", "Roma", "Napoli", "Torino", "Firenze", "Bologna", "Genova", "Padova", "Milano", "Biella", "San Donà di Piave"],
    "telefono": ["1234567890", "0987654321", "1112223334", "5556667778", "9998887776", "4445556667", "2223334445", "7778889990", "3334445556", "6667778889", "1234567890", "0987654321", "1112223334", "5556667778", "9998887776", "4445556667", "2223334445", "7778889990", "3334445556", "6667778889"],
    "tipo_cliente": ["Privato", "Azienda", "Privato", "Azienda", "Privato", "Azienda", "Privato", "Azienda", "Privato", "Azienda", "Privato", "Azienda", "Privato", "Azienda", "Privato", "Azienda", "Privato", "Azienda", "Privato", "Azienda"],
    "partita_iva": [None, "12345678901", None, "98765432109", None, "11122233344", None, "55566677788", None, "99988877766", None, "44455566677", None, "22233344455", None, "77788899900", None, "33344455566", None, "66677788899"],
    "data_registrazione": ["2020-01-15", "2019-06-30", "2021-09-01", "2018-03-20", "2017-11-05", "2016-04-10", "2022-07-25", "2015-02-18", "2014-12-12", "2013-08-01", "2020-01-15", "2019-06-30", "2021-09-01", "2018-03-20", "2017-11-05", "2016-04-10", "2022-07-25", "2015-02-18", "2014-12-12", "2013-08-01"],
}

# Lista dei fornitori con clienti diverso da quelli del dataframe clienti, per evitare confusione
fornitori = {
    "nome": ["Simone", "Matteo", "Sara", "Andrea", "Valentina", "Davide", "Chiara", "Alessia", "Federico", "Giorgia"],
    "cognome": ["Grigio", "Viola", "Arancione", "Marrone", "Azzurro", "Giallo", "Turchese", "Fucsia", "Lilla", "Indaco"],
    "email": ["simone.grigio@email.com", "matteo.viola@email.com", "sara.arancione@email.com", "andrea.marrone@email.com", "valentina.azzurro@email.com", "davide.giallo@email.com", "chiara.turchese@email.com", "alessia.fucsia@email.com", "federico.lilla@email.com", "giorgia.indaco@email.com"],
    "citta": ["Roma", "Napoli", "Torino", "Firenze", "Bologna", "Genova", "Padova", "Milano", "Biella", "San Donà di Piave"],
    "telefono": ["1234567890", "0987654321", "1112223334", "5556667778", "9998887776", "4445556667", "2223334445", "7778889990", "3334445556", "6667778889"],
    "tipo_fornitore": ["Privato", "Azienda", "Privato", "Azienda", "Privato", "Azienda", "Privato", "Azienda", "Privato", "Azienda"],
    "partita_iva": [None, "12345678901", None, "98765432109", None, "11122233344", None,"55566677788" , None, 	"99988877766"],
   	"data_registrazione": ["2020-01-15",	"2019-06-30"	,"2021-09-01"	,"2018-03-20"	,"2017-11-05"	,"2016-04-10"	,"2022-07-25"	,"2015-02-18"	,"2014-12-12"	,"2013-08-01"],
   	"fatturato_annuale": [50000, 200000, 75000, 300000, 100000, 250000, 80000, 350000, 120000, 280000],
   	"settore": ["Tecnologia","Finanza","Sanità","Commercio","Industria","Servizi","Tecnologia","Finanza","Sanità","Commercio"],
    "cliente_principale": ["Luca Bianchi", "Giovanni Neri", "Francesco Rossi", "Giulia Verdi", "Elena Gialli", "Federica Blu", "Alessandro Rosa", "Simone Grigio", "Matteo Viola", "Sara Arancione"],
    "numero_dipendenti": [10, 50, 20, 100, 30, 80, 15, 60, 25, 90],
}

# Trasformazione dei dizionari in dataframe
df_clienti = pd.DataFrame(clienti)
df_fornitori = pd.DataFrame(fornitori)


# definisci il percorso del file Excel dove salvare i dataframe
# Modificatemi          👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 
percorso_file_excel = r"D:\TalentForm_2026_3_Edition\Corso_Python_Completo\Corso_Python_Completo_3_Edition\Intermedio\lavoro_con_file\data\clienti_fornitori.xlsx"

# Verifica se il file Excel esiste già, se sì, carica i dati esistenti e aggiungi i nuovi dati, altrimenti crea un nuovo file Excel
try:
    df_clienti.head() # visualizza le prime 5 righe del dataframe clienti
    df_fornitori.head() # visualizza le prime 5 righe del dataframe fornitori

    # Salvare i dataframe in un file Excel con due fogli: "Clienti" e "Fornitori"
    with pd.ExcelWriter(percorso_file_excel, engine='openpyxl') as writer:
        df_clienti.to_excel(writer, sheet_name='Clienti', index=False)
        df_fornitori.to_excel(writer, sheet_name='Fornitori', index=False)
    
    # invia il messaggio di conferma
    print(f"I dataframe sono stati salvati con successo in {percorso_file_excel}") 
except FileNotFoundError:
    # Se il file non esiste, crea un nuovo file Excel e salva i dataframe
    with pd.ExcelWriter(percorso_file_excel, engine='openpyxl') as writer:
        df_clienti.to_excel(writer, sheet_name='Clienti', index=False)
        df_fornitori.to_excel(writer, sheet_name='Fornitori', index=False)

    print(f"I dataframe sono stati salvati con successo in {percorso_file_excel}") 
