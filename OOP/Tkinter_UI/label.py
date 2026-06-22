import tkinter as tk # importa la libreria che ci permette di creare applicazioni desktop

root = tk.Tk()  # finestra proincipale della app

# definizione della dimenzione della finestra
root.geometry("600x450")


# definizione del titolo della pagina 
root.title("Label Form")

# definizione della label(Etichetta non modificabile durante l'esecuzione della app)
lbl = tk.Label(
        root,
        text='Come imparare CSS: guida facile',
        fg="#056970",
        font=('Roboto', 16, 'bold')
    )


# Mostra la label nella finestra
lbl.pack()

lbl1 = tk.Label(
        root,
        text='Imparare CSS ci permette di modificare l\'aspetto e il layout di una pagina web. In…',
        fg="#0E1414",
        font=('Arial', 12)
    )
lbl1.pack(pady=3)


# Disattiva la sizeble della form
root.resizable(False, False)

root.mainloop()


