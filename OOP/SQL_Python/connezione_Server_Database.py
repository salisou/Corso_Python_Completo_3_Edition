""" 
    Obiettivo del corso Sql Con python:
        Colegamento al database SQL Server
        esequire query del sistema 
        recuperare automaticamente le tabelle 
        gestire errori e connessioni in modo pro
        capire come un Data Analyst esplora un Database sconosciuto
        🎉🎉🎉🎉🎉 Complimmenti 📊📊📊📊
"""
import pyodbc as odbc
import pandas as pd



conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Moussa\\SQLEXPRESS01;" # da modificare 
    "DATABASE=ScuolaDb;" # da modificare 
    "Trusted_Connection=yes;" 
    "TrustServerCertificate=yes;"
)
 
try:
    print("⏳ Connessione al server...")
    
    conn = odbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Nome server
    values = cursor.execute('SELECT @@SERVERNAME').fetchone()[0]
    print(f"✅ Connesso al server {values}\n")
    
    print("\n📚 Recupero automatico delle tabelle...\n")
    
    # Stored procedure
    cursor.execute("EXEC sp_ListaTabelle")
    
    # Recupero UNA sola volta
    tabelle = [row[0] for row in cursor.fetchall()]
    
    print("📌 Tabelle trovate:\n")
    for t in tabelle:
        print(f" → {t}")
    
    print("\n📊 LETTURA RECORD DELLE TABELLE\n")
    
    # Ciclo su ogni tabella
    for tabella in tabelle:
        print("=========================================")
        print(f"📌 Tabella: {tabella}")
        print("=========================================")
        
        try:
            query = f"SELECT TOP 10 * FROM [{tabella}]"
            cursor.execute(query)
            
            colonne = [desc[0] for desc in cursor.description]
            print(f"🧩 Colonne: {colonne}")
            
            rows = cursor.fetchall()
            
            if not rows:
                print("⚠️ Nessun record trovato.")
                continue
            
            # Evita stampa di colonne binarie
            for row in rows:
                valori = []
                for v in row:
                    if isinstance(v, bytes):
                        valori.append("<BINARY DATA>")
                    else:
                        valori.append(v)
                print(" →", valori)

        except Exception as e:
            print(f"⚠️ Errore nella tabella {tabella}: {e}")
        
except Exception as e:
    print("❌ Errore di connessione:")
    print(e)

finally:
    try:
        print("\n🔐 Chiusura connessione...")
        conn.close()
        print("Connessione chiusa.")
    except:
        print("⚠️ Impossibile chiudere la connessione.")
        pass
