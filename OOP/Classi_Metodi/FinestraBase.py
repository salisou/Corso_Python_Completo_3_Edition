import tkinter as tk # importa la libreria che ci permette di creare applicazioni desktop

class FinestraBase:
    def __init__(self, titolo="App Tkionter", larghezza=800, altezza=600):
        self.root = tk.Tk()
        self.root.title(titolo)
        self.root.geometry(f'{larghezza}x{altezza}')
        self.root.resizable(False, False)
        
        # richiamata del motodo crea_ui
        self.crea_ui()
    
    def crea_ui(self):
        label = tk.Label(
            self.root,
            text="Benvenuti",
            font=("Segoe UI", 20)
        )
        
        label.pack(pady=20)
     
    def avvia(self):
        self.root.mainloop()
    