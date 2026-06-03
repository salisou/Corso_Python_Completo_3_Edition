""" While esegue un blocco di codice finche la condizione restituisce Ture
    es:
        while true:
            print()
"""

contatore_valore = 1

while contatore_valore <= 10:
    print(f"Esecuzione programma: {contatore_valore}")
    contatore_valore = contatore_valore + 1
    

risposta = ''

while risposta != 'esci':
    risposta = input(f"Scrivi qualcosa: ")
    print(risposta)
print('Ciao')

