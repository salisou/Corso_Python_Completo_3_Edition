print("\n============= Ciao Benvenuto ==============\n")

# Chiediamo all'utente di inserire i suoi dati
nome = str(input("Inserisci tuo nome: "))
cognome = str(input(f"Inserisci tuo cognome {nome} "))
eta = int(input(f"Quanti annni hai? "))
altezza = float(input("Quanto sei alto? "))


# Stampa l'utente
print(f"\nciao {nome} {cognome} hai {eta} anni e sei alto {altezza} cm")
