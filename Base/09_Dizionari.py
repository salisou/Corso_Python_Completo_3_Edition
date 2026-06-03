"""
    Dizionari in python 
    
    I dictionary (dizionario) è una struttura che salva dati Chiave - Valore.
    es:
        nome {
            'chiave': 'valore',
            'chiave': 'valore',
            'chiave': 'valore',
            'chiave': 'valore',
            'chiave': 'valore',
            'chiave': 'valore':{
                'chiave': 'valore',
                'chiave': 'valore'
            }
        }
"""  
"""
persona = {
    'nome': 'Mario', # chiave: nome, valore: Marco
    'cognome': 'Ricci',
    'eta': 30,
    'citta': 'Milano',
    'codice_fiscale': 'MRI7894DH45O1P',
    'professione': 'Ingegnere'
}



# Accedere ai valori del dizionario
print(persona['nome'])

# Più sicoro e usare il metodo get() che restituisce Nome se la chiave non esiste
print(persona.get('codice_fiscale')) # Output: MRI7894DH45O1P

# Modificare un valore esistente 
persona['cognome'] = 'Rossi'
print(persona['cognome'])


# Aggiornare una coppia chiave-valore
persona['professione'] = 'Insegnate'
print(persona['professione'])
"""


persone = [
   {
        'nome': 'Mario', # chiave: nome, valore: Marco
        'cognome': 'Ricci',
        'eta': 30,
        'citta': 'Milano',
        'codice_fiscale': 'MRI7894DH45O1P',
        'professione': 'Ingegnere'
    },
    {
        "nome": "Rudy",
        "cognome": "Botosso",
        "eta": 54,
        "citta": "Biella",
        "codice fiscale": "BTTRDY71L15A859E",
        "professione": "Informatico"
    },
    {
        "nome": "Marco",
        "cognome": "Secci",
        "eta": 54,
        "citta": "San Donà di Piave",
        "codice fiscale": "SCCMRC71P22H823A",
        "professione": "Disoccupato"
    },
    {
        'nome':'Andrea',
        'cognome':'Romano',
        'eta': 36,
        'citta': 'Ripatransone',
        'codice_fiscale': 'RNINFEINFIEN',
        'professione': 'Studente'
    },
    {
            'nome': 'Saverio', 
            'cognome': 'Carulli',
            'eta': 34,
            'citta': 'Spinazzola',
            'codice_fiscale': 'CRLSVR92H24O1P',
            'professione': 'Disoccupato'
    },
    {
        'nome': 'Giulia', 
        'cognome': 'Pierro',
        'eta': 25,
        'citta': 'Latina',
        'codice_fiscale': 'PRRGLI7894DH45O1P',
        'professione': 'Studente'
    },
    {
        'nome': 'Fabrice',
        'cognome': 'Cheick',
        'eta': 51,
        'citta': 'Ferrara',
        'codice_fiscale': 'CHKFRC75Z20H231G',      
        'professione': 'Pastore'
    },
    {
        'nome': 'Laura',
        'cognome': 'Ricordi',
        'eta': 33,
        'citta': 'Alessandria',
        'codicefiscale':  'chi lo sa?',
        'professione': 'speriamo hr data analyst'
    },
    {
        'nome': 'Luigia',
        'cognome': 'Valente',
        'eta': 32,
        'citta': 'Avellino',
        'codice_fiscale': 'VLNLGU93R64A783K',
        'professione': 'Receptionist'
    },
    {
        'nome': 'Teresa',
        'cognome': 'Balsamo',
        'eta': 25,
        'citta': 'Roma', 
        'codice_fiscale': 'BLSTRS00H48A024P',
        'professione': 'in_cerca'   
    }
]

"""
print("\n================== Lista persone ==================\n")
for persona in persone:
    print(f"Nome: {persona['nome']}, Cognome: {persona['cognome']}, Età: {persona['eta']}")


# Satmpa tuti gli informazioni di ogni persona in modo leggibile
print("\n\n=====================================================\n")
for persona in persone:
    print(f"------ Studente ------")
    for chiave, valore in persona.items():
        print(f"{chiave}: {valore}")
    print()

# Filtra persone per professione (es: solo "Studente") e stampare in minuscolo
print("\n=======================================================")

print("Persone con professione Studente".upper())

for persona in persone:
    if persona.get('professione', '').upper() == 'Disoccupato'.upper():
        print(f"Nome: {persona['nome']}, Cognome: {persona['cognome']}, Età: {persona['eta']}")
"""

# Calcolare l'età media delle persone
eta_totale = 0
conta = 0

for p in persone:
    eta = p.get('eta')
    
    if isinstance(eta, int) and eta > 0:
        eta_totale += eta
        # ++conta
        # conta += 1
        conta = conta + 1

if conta > 0:
    eta_media = eta_totale / conta
    print(f"Età media: {eta_media:.0f}") # 18.50
else:
    print("Nessun dato volido sull'età")


