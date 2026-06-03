""" 
    Ciclo for e funzione range()
    range(5) -> genera i numeri da (0 a 4)
    range(6) -> genera i numeri da (0 a 5)
    range(2, 7, 2) -> genera i numeri da (2, 4, 7)
    
    
    print('ciao')
    print('ciao')
    print('ciao')
    print('ciao')
    print('ciao')
    print('ciao')

    for valore default(i) in range(numero(5)):
        print(f'messagio: {i}')
    
"""
for i in range(5):
    print(f'Sono il numero: {i}')


# esempio 1
studenti = ["Maio", "Luca", "Luigi", "Andrea", "Rudy", "Fabrice"]

for studente in studenti:
    print(f'Mi chiamo : {studente}')


"""
numeri = [1, 2, 5, 9]
for numero in numeri:
    print()
""" 
numeri = 5

print(f'\nTavolo di multiplicazione {numeri}\n')
for i in range(1, 12):
    risultato = numeri * i
    print(f"{numeri} x {i} = {risultato}")
    
print(f'\nTavolo di multiplicazione Completa da 1 a 12\n')
for riga in range(1, 13):
    for colonna in range(1, 13):
        risultato = riga * colonna
        print(f'{riga} x {colonna} = {risultato}', end='\n')
    print()
