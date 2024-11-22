import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import yfinance as yf

børser = {
    "Chicago Board of Trade (CBOT)": ".CBT",
    "Chicago Mercantile Exchange (CME)": ".CME",
    "ICE Futures US": ".NYB",
    "New York Commodities Exchange (COMEX)": ".CMX",
    "New York Mercantile Exchange (NYMEX)": ".NYM",
    "Buenos Aires Stock Exchange (BYMA)": ".BA",
    "Vienna Stock Exchange": ".VI",
    "Australian Stock Exchange (ASX)": ".AX",
    "Cboe Australia": ".XA",
    "Euronext Brussels": ".BR",
    "Sao Paolo Stock Exchange (BOVESPA)": ".SA",
    "Canadian Securities Exchange": ".CN",
    "Cboe Canada": ".NE",
    "Toronto Stock Exchange (TSX)": ".TO",
    "TSX Venture Exchange (TSXV)": ".V",
    "Santiago Stock Exchange": ".SN",
    "Shanghai Stock Exchange": ".SS",
    "Shenzhen Stock Exchange": ".SZ",
    "Colombia Stock Exchange": ".CL",
    "Prague Stock Exchange Index": ".PR",
    "Nasdaq OMX Copenhagen": ".CO",
    "Egyptian Exchange Index (EGID)": ".CA",
    "Nasdaq OMX Tallinn": ".TL",
    "Cboe Europe": ".XD",
    "Euronext": ".NX",
    "Nasdaq OMX Helsinki": ".HE",
    "Euronext Paris": ".PA",
    "Berlin Stock Exchange": ".BE",
    "Bremen Stock Exchange": ".BM",
    "Dusseldorf Stock Exchange": ".DU",
    "Frankfurt Stock Exchange": ".F",
    "Hamburg Stock Exchange": ".HM",
    "Hanover Stock Exchange": ".HA",
    "Munich Stock Exchange": ".MU",
    "Stuttgart Stock Exchange": ".SG",
    "Deutsche Boerse XETRA": ".DE",
    "Collectable Indices": ".REGA",
    "Athens Stock Exchange (ATHEX)": ".AT",
    "Hong Kong Stock Exchange (HKEX)": ".HK",
    "Budapest Stock Exchange": ".BD",
    "Nasdaq OMX Iceland": ".IC",
    "Bombay Stock Exchange": ".BO",
    "National Stock Exchange of India": ".NS",
    "Indonesia Stock Exchange (IDX)": ".JK",
    "Euronext Dublin": ".IR",
    "Tel Aviv Stock Exchange": ".TA",
    "EuroTLX": ".TI",
    "Italian Stock Exchange": ".MI",
    "Tokyo Stock Exchange": ".T",
    "Boursa Kuwait": ".KW",
    "Nasdaq OMX Riga": ".RG",
    "Nasdaq OMX Vilnius": ".VS",
    "Malaysian Stock Exchange": ".KL",
    "Mexico Stock Exchange (BMV)": ".MX",
    "Euronext Amsterdam": ".AS",
    "New Zealand Stock Exchange (NZX)": ".NZ",
    "Oslo Stock Exchange": ".OL",
    "Philippine Stock Exchange Indices": ".PS",
    "Warsaw Stock Exchange": ".WA",
    "Euronext Lisbon": ".LS",
    "Qatar Stock Exchange": ".QA",
    "Bucharest Stock Exchange": ".RO",
    "Singapore Stock Exchange (SGX)": ".SI",
    "Johannesburg Stock Exchange": ".JO",
    "Korea Stock Exchange": ".KS",
    "KOSDAQ": ".KQ",
    "Madrid SE C.A.T.S.": ".MC",
    "Saudi Stock Exchange (Tadawul)": ".SAU",
    "Nasdaq OMX Stockholm": ".ST",
    "Swiss Exchange (SIX)": ".SW",
    "Taiwan OTC Exchange": ".TWO",
    "Taiwan Stock Exchange (TWSE)": ".TW",
    "Stock Exchange of Thailand (SET)": ".BK",
    "Borsa İstanbul": ".IS",
    "Dubai Financial Market": ".AE",
    "Aquis Exchange AQSE": ".AQ",
    "Cboe UK": ".XC",
    "London Stock Exchange": ".L",
    "London Stock Exchange (alternative)": ".IL",
    "Caracas Stock Exchange": ".CR",
    "Ho Chi Minh City Stock Exchange": ".VN",
}

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
finn_aksje_knapp = tk.Button(input_div, text="Finn aksje", command=plot_graf, bg="#005B96", fg="#fff")

aksje_input.grid(row=1, column=1, padx=2, pady=2)
finn_aksje_knapp.grid(row=1, column=4)

børs_boks = ttk.Combobox(root, values=list(børser.keys()))
børs_boks.pack()

graf_div = tk.Frame(root)
graf_div.pack()

canvas = FigureCanvasTkAgg(fig, master=graf_div)
canvas.get_tk_widget().pack()

tk.mainloop()