
"""
    Condizione if(se) elif(altrimenti se) else(altrimenti)
    -----------------------------------------------------
    if Condizione:
        Codice
    else:
        Codice
    -------------------------------------------------------   
    if Condizione:
        Codice
    elif condizione:
        Codice
    else:
        Codice

"""

"""
cliente = input("Hai una prenotazione? ")

if cliente == "si":
    print("Ok")
else:
    print("Non posti")



if cliente == "si":
    print("Ok")
elif cliente == "no":
    print("Mi spiace non posti stasera")
else:
    print("Errore", "Devi rispondere (si o no)")
"""

# Autenticazione
nome = 'Moussa'
pwd = 12345


username = input("Inserisci la username: ")
password = int(input("Inserisci la password: "))

if username == nome and password == pwd:
    print("Benvenuto nel programma")
elif username != nome:
    print(f"👤 Errore il nome {username} non esiste nel sistema!")
elif password != pwd:
    print(f"🔐 Errore il nome verifica la password!")
else:
    print("⚠️ Accesso negato!")  