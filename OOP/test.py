import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# ── Palette colori ──────────────────────────────
BG      = "#0d0d0d"
SURFACE = "#1a1a1a"
SIDEBAR = "#111111"
ACCENT  = "#00bcd4"
TEXT    = "#e0e0e0"
MUTED   = "#555555"
COLORS  = ["#00bcd4","#4caf50","#ff9800","#e91e63","#9c27b0"]

plt.rcParams.update({
    "figure.facecolor": SURFACE,
    "axes.facecolor":   "#141414",
    "axes.edgecolor":   "#333",
    "axes.labelcolor":  MUTED,
    "text.color":       TEXT,
    "xtick.color":      MUTED,
    "ytick.color":      MUTED,
    "grid.color":       "#222",
    "grid.alpha":       0.5,
    "font.family":      "sans-serif",
    "font.size":        9,
})

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard Matplotlib – Tkinter Desktop App")
        self.configure(bg=BG)
        self.state("zoomed")            # finestra massimizzata
        self.vista_corrente = tk.StringVar(value="Dashboard")
        self._build_layout()
        self._show_view("Dashboard")

    # ── Layout principale ────────────────────────
    def _build_layout(self):
        # Sidebar sinistra
        self.sidebar = tk.Frame(self, bg=SIDEBAR, width=180)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo
        tk.Label(self.sidebar, text="◆", fg=ACCENT, bg=SIDEBAR,
                font=("Arial", 24)).pack(pady=(20,4))
        tk.Label(self.sidebar, text="DATA DASH", fg=TEXT, bg=SIDEBAR,
                font=("Arial", 13, "bold")).pack()
        tk.Label(self.sidebar, text="Matplotlib + Tkinter",
                fg=MUTED, bg=SIDEBAR, font=("Arial", 8)).pack(pady=(0,16))

        # Separatore
        tk.Frame(self.sidebar, bg="#222", height=1).pack(fill="x", padx=16)

        # Voci di navigazione
        tk.Label(self.sidebar, text="GRAFICI", fg=MUTED, bg=SIDEBAR,
                font=("Arial", 8), anchor="w").pack(
                fill="x", padx=16, pady=(16,4))

        self.nav_buttons = {}
        voci = [
            ("■", "Dashboard"),
            ("—", "Linee"),
            ("▮", "Barre"),
            ("●", "Torta"),
            ("·", "Scatter"),
            ("▒", "Istogramma"),
            ("~", "Area"),
        ]
        for icona, nome in voci:
            btn = tk.Button(
                self.sidebar, text=f"  {icona}  {nome}",
                fg=TEXT, bg=SIDEBAR, activebackground="#1e1e1e",
                activeforeground=ACCENT, relief="flat",
                font=("Arial", 11), anchor="w",
                command=lambda n=nome: self._show_view(n)
            )
            btn.pack(fill="x", padx=8, pady=1)
            self.nav_buttons[nome] = btn

        # Versione
        tk.Label(self.sidebar, text="v2.0 • matplotlib",
                fg=MUTED, bg=SIDEBAR, font=("Arial", 7)).pack(
                side="bottom", pady=10)

        # Area principale
        self.main = tk.Frame(self, bg=BG)
        self.main.pack(side="right", fill="both", expand=True)

        # Header
        header = tk.Frame(self.main, bg=BG)
        header.pack(fill="x", padx=20, pady=12)
        self.title_lbl = tk.Label(header, text="Dashboard",
            fg=TEXT, bg=BG, font=("Arial", 20, "bold"))
        self.title_lbl.pack(side="left")

        # Badge librerie
        for lib in ["Matplotlib", "NumPy", "Tkinter"]:
            tk.Label(header, text=lib, fg=ACCENT, bg=BG,
                    font=("Arial", 8)).pack(side="right", padx=4)

        # Canvas container
        self.canvas_frame = tk.Frame(self.main, bg=BG)
        self.canvas_frame.pack(fill="both", expand=True, padx=10)

    # ── Navigazione ─────────────────────────────
    def _show_view(self, nome):
        # Evidenzia bottone attivo
        for n, btn in self.nav_buttons.items():
            btn.config(bg="#1e1e1e" if n==nome else SIDEBAR,
                       fg=ACCENT if n==nome else TEXT)
        self.title_lbl.config(text=nome)

        # Pulisce canvas precedente
        for w in self.canvas_frame.winfo_children():
            w.destroy()

        # Costruisce il grafico
        metodo = getattr(self, f"_view_{nome.lower()}", self._view_dashboard)
        fig = metodo()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    # ── Vista Dashboard (6 grafici) ──────────────
    def _view_dashboard(self):
        fig, axes = plt.subplots(3, 2, figsize=(14, 9))
        fig.tight_layout(pad=3.0)
        np.random.seed(42)
        mesi = ['Gen','Mar','Mag','Lug','Set','Nov']

        # Linee
        ax = axes[0][0]
        for i, c in enumerate(COLORS[:3]):
            ax.plot(mesi, np.random.randint(80,200,6), 'o-',
                   color=c, label=chr(65+i), linewidth=1.8)
        ax.set_title("Trend Vendite Mensili"); ax.legend(); ax.grid(True)

        # Barre
        ax = axes[0][1]
        reg = ['Nord','Sud','Est','Ovest','Centro']
        fat = [340,210,180,420,290]; obj = [300,250,200,380,310]
        x = np.arange(5); w=0.35
        ax.bar(x-w/2, fat, w, color=ACCENT, label="Reale")
        ax.bar(x+w/2, obj, w, color="#333", label="Obiettivo")
        ax.set_xticks(x); ax.set_xticklabels(reg)
        ax.set_title("Fatturato vs Obiettivo (k€)"); ax.legend()

        # Torta donut
        ax = axes[1][0]
        ax.pie([35,20,18,15,12],
              labels=['Tech','Finance','Health','Energy','Retail'],
              colors=COLORS, autopct='%1.0f%%',
              wedgeprops=dict(width=0.6, edgecolor=SURFACE, linewidth=2))
        ax.set_title("Quote di Mercato")

        # Scatter
        ax = axes[1][1]
        inv = np.random.uniform(0,100,150)
        pro = inv * 0.8 + np.random.normal(0,12,150)
        sc = ax.scatter(inv, pro, c=np.random.rand(150),
                        s=np.random.uniform(20,200,150),
                        cmap='plasma', alpha=0.7)
        z=np.polyfit(inv,pro,1); p=np.poly1d(z)
        ax.plot(np.sort(inv), p(np.sort(inv)), '--', color="#f9e2af", lw=2)
        ax.set_title("Investimento vs Profitto")
        fig.colorbar(sc, ax=ax)

        # Istogramma
        ax = axes[2][0]
        vals = np.clip(np.random.normal(7.2,1.5,500), 0, 10)
        ax.hist(vals, bins=20, color="#cba6f7", edgecolor=SURFACE, alpha=0.85)
        ax.axvline(vals.mean(),   color="#f38ba8", lw=2, linestyle="--",
                   label=f"Media {vals.mean():.1f}")
        ax.axvline(np.median(vals), color="#a6e3a1", lw=2, linestyle=":",
                   label=f"Mediana {np.median(vals):.1f}")
        ax.set_title("Soddisfazione Clienti (0-10)"); ax.legend()

        # Area stackplot
        ax = axes[2][1]
        t = np.linspace(0, 4*np.pi, 300)
        A = 0.5+0.5*np.sin(t*0.8)
        B = 0.5+0.5*np.sin(t*0.8+np.pi/3)
        C = 0.5+0.5*np.sin(t*0.8+2*np.pi/3)
        ax.stackplot(t, A, B, C, labels=['A','B','C'],
                    colors=[ACCENT,"#4caf50","#555"], alpha=0.8)
        ax.set_title("Segnale Multi-canale"); ax.legend(loc="upper right")

        return fig

    # ── Viste singole ───────────────────────────
    def _view_linee(self):
        fig, ax = plt.subplots(figsize=(12,7))
        mesi = ['Gen','Feb','Mar','Apr','Mag','Giu',
                'Lug','Ago','Set','Ott','Nov','Dic']
        np.random.seed(1)
        for i,c in enumerate(COLORS[:3]):
            y = np.random.randint(80,220,12)
            ax.plot(mesi,y,'o-',color=c,lw=2,ms=5,label=f"Serie {i+1}")
            ax.fill_between(mesi,y,alpha=0.05,color=c)
        ax.set_title("Trend Annuale",fontsize=14); ax.legend(); ax.grid(True)
        return fig

    def _view_barre(self):
        fig, ax = plt.subplots(figsize=(12,7))
        cat = ['Q1','Q2','Q3','Q4']
        for i,c in enumerate(COLORS[:3]):
            ax.bar(np.arange(4)+i*0.25, np.random.randint(100,500,4),
                  0.25, color=c, label=f"Prodotto {i+1}")
        ax.set_xticks(np.arange(4)+0.25); ax.set_xticklabels(cat)
        ax.set_title("Vendite per Trimestre",fontsize=14); ax.legend()
        return fig

    def _view_torta(self):
        fig, ax = plt.subplots(figsize=(10,8))
        ax.pie([30,25,20,15,10],
              labels=['A','B','C','D','E'], colors=COLORS,
              autopct='%1.1f%%', startangle=90,
              wedgeprops=dict(width=0.55,edgecolor=SURFACE,linewidth=2),
              textprops=dict(color=TEXT))
        ax.set_title("Distribuzione Portfolio",fontsize=14)
        return fig

    def _view_scatter(self):
        fig, ax = plt.subplots(figsize=(12,7))
        np.random.seed(5)
        for c in COLORS:
            x = np.random.normal(50,20,80)
            y = x * 0.7 + np.random.normal(0,10,80)
            ax.scatter(x,y,color=c,alpha=0.6,s=60)
        ax.set_title("Correlazione Multi-cluster",fontsize=14)
        ax.set_xlabel("Variabile X"); ax.set_ylabel("Variabile Y")
        return fig

    def _view_istogramma(self):
        fig, ax = plt.subplots(figsize=(12,7))
        np.random.seed(7)
        dati = np.clip(np.random.normal(7,2,1000),0,10)
        ax.hist(dati,bins=30,color=COLORS[4],edgecolor=SURFACE,alpha=0.9)
        ax.axvline(dati.mean(),color=COLORS[2],lw=2,linestyle="--",
                   label=f"μ={dati.mean():.2f}")
        ax.set_title("Distribuzione NPS",fontsize=14); ax.legend()
        return fig

    def _view_area(self):
        fig, ax = plt.subplots(figsize=(12,7))
        t = np.linspace(0,4*np.pi,400)
        segnali = [0.5+0.5*np.sin(t*0.8+i*np.pi/3) for i in range(4)]
        ax.stackplot(t,*segnali,
                    labels=[f"Canale {i+1}" for i in range(4)],
                    colors=COLORS, alpha=0.75)
        ax.set_title("Segnali Multi-canale",fontsize=14)
        ax.legend(loc="upper right")
        return fig

if __name__ == "__main__":
    Dashboard().mainloop()