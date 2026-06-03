"""
    Liste in python
    Cos'è :
        Le liste sono strtture dati che permettono di salvare più insieme
        
        Una lista può contenere:
            - Numeri
            - Stringhe
            - boolean
            - altre liste
            
    studenti = []
"""

studenti = ["Maio", "Luca", "Luigi", "Andrea", "Rudy", "Rudy", "Fabrice"]
# print(studenti)

 # Aggiungo uno studente nella lista
studenti.append("Teresa")
print(studenti)

# Accesso agli elementi
print(studenti[2])
print(studenti[5])

studenti.append("Marco")
print(studenti)
print(studenti[-1])

# Modifica elementi
studenti[0] = "Carlo"
print(studenti[0])

# Rimuovere elementi
studenti.remove(studenti[4])
print(studenti)

studenti.remove("Teresa")
print(studenti)

