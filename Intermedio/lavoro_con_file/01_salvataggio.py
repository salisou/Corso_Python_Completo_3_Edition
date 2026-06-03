import pandas as pd

# Creazione del dataframe(dipendenti) = dataset(Tabella, Modello, Entity) 
dipendenti = {
    "nome": ["Mario", "Rudy", "Marco", "Luca", "Giovanni", "Francesco", "Giulia", "Elena", "Federica", "Alessandro"],
    "cognome": ["Ricci", "Botosso", "Secci", "Bianchi", "Neri", "Rossi", "Verdi", "Gialli", "Blu", "Rosa"],
    "email": ["mario.ricci@example.info", None, "marco.secci@example.com", None, "giovanni.neri@example.com", "francesco.rossi@example.ue", "giulia.verdi@example.com", "elena.gialli@example.it", "federica.blu@example.com", "alessandro.rosa@example.info"],
    "eta": [30, 54, 54, 28, 35, 42, 28, 32, 29, 31],
    "citta": ["Milano", "Biella", "San Donà di Piave", "Roma", "Napoli", "Torino", "Firenze", "Bologna", "Genova", "Padova"],
    "stipendio": [2000, 3000, 1500, 2500, 3500, 4000, 2500, 3000, 3500, 4000],
    "ruolo": ["Sviluppatore", "Project Manager", "Analista", "Sviluppatore", "Team Leader", "Project Manager", "Sviluppatore", "Analista", "Team Leader", "Project Manager"],
    "data_assunzione": ["2015-01-15", "2010-06-30", "2018-09-01", "2016-03-20", "2012-11-05", "2008-04-10", "2017-07-25", "2014-02-18", "2013-12-12", "2009-08-01"]
}

# Trasformazione del dizionario in un dataframe
df = pd.DataFrame(dipendenti)

path = r"percorso_file.csv"

# definisci il percorso del file CSV dove salvare il dataframe
percorso_file = r"D:\TalentForm_2026_3_Edition\Corso_Python_Completo\Corso_Python_Completo_3_Edition\Intermedio\lavoro_con_file\data\dipendenti.csv"

# Salvare il dataframe in un file CSV
df.to_csv(percorso_file, index=False)