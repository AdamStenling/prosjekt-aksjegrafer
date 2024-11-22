import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import yfinance as yf


fig = plt.figure()

def plot_graf():
    try:
        fig.clear()
        ticker = aksje_input.get()
        aksje = yf.Ticker(ticker)
        aksjenavn = aksje.info['longName']
        aksje_data = yf.download(ticker, start="2020-01-01", end="2025-01-01")
        plt.plot(aksje_data["Close"])
        plt.xlabel("Dato")
        plt.ylabel(f"Aksjepris i {aksje.info["currency"]}")
        plt.legend([aksjenavn])
        plt.grid(True)
        canvas.draw()
    except KeyError:
        aksje_input.delete(0, tk.END)
        aksje_input.insert(0, "Finner ikke ticker")
        aksje_input.config({"fg": "Red"})

# For å tvangslukke programmet 
def on_close():
    root.quit()
    root.destroy()

root = tk.Tk()

# Slet med at programmet ikke ville lukke seg, så fant denne løsningen på nett
root.protocol("WM_DELETE_WINDOW", on_close)

overskrift_div = tk.Frame(root)
overskrift_div.pack()

overskrift = tk.Label(overskrift_div, text="Finn grafen til din askje!", font=("Arial", 18))
overskrift.pack()

input_div = tk.Frame(root)
input_div.pack()

aksje_input = tk.Entry(input_div)
aksje_input.insert(0, "Skriv inn ticker")
finn_aksje_knapp = tk.Button(input_div, text="Finn aksje", command=plot_graf)

aksje_input.grid(row=1, column=1, padx=2)
finn_aksje_knapp.grid(row=1, column=4)

graf_div = tk.Frame(root)
graf_div.pack()

canvas = FigureCanvasTkAgg(fig, master=graf_div)
canvas.get_tk_widget().pack()

tk.mainloop()