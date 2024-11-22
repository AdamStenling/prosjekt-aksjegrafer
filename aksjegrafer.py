import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import yfinance as yf

børser = {
    "Aquis Exchange AQSE": ".AQ",
    "Athens Stock Exchange (ATHEX)": ".AT",
    "Australian Stock Exchange (ASX)": ".AX",
    "Berlin Stock Exchange": ".BE",
    "Bombay Stock Exchange": ".BO",
    "Borsa İstanbul": ".IS",
    "Boursa Kuwait": ".KW",
    "Bremen Stock Exchange": ".BM",
    "Budapest Stock Exchange": ".BD",
    "Buenos Aires Stock Exchange (BYMA)": ".BA",
    "Cboe Australia": ".XA",
    "Cboe Canada": ".NE",
    "Cboe Europe": ".XD",
    "Cboe UK": ".XC",
    "Canadian Securities Exchange": ".CN",
    "Caracas Stock Exchange": ".CR",
    "Chicago Board of Trade (CBOT)": ".CBT",
    "Chicago Mercantile Exchange (CME)": ".CME",
    "Colombia Stock Exchange": ".CL",
    "Collectable Indices": ".REGA",
    "Deutsche Boerse XETRA": ".DE",
    "Dow Jones Indexes": "",
    "Dubai Financial Market": ".AE",
    "Dusseldorf Stock Exchange": ".DU",
    "Egyptian Exchange Index (EGID)": ".CA",
    "EuroTLX": ".TI",
    "Euronext": ".NX",
    "Euronext Amsterdam": ".AS",
    "Euronext Brussels": ".BR",
    "Euronext Dublin": ".IR",
    "Euronext Lisbon": ".LS",
    "Euronext Paris": ".PA",
    "Frankfurt Stock Exchange": ".F",
    "Hamburg Stock Exchange": ".HM",
    "Hanover Stock Exchange": ".HA",
    "Ho Chi Minh City Stock Exchange": ".VN",
    "Hong Kong Stock Exchange (HKEX)": ".HK",
    "ICE Futures US": ".NYB",
    "Indonesia Stock Exchange (IDX)": ".JK",
    "Italian Stock Exchange": ".MI",
    "Johannesburg Stock Exchange": ".JO",
    "KOSDAQ": ".KQ",
    "Korea Stock Exchange": ".KS",
    "London Stock Exchange": ".L",
    "London Stock Exchange (alternative)": ".IL",
    "Madrid SE C.A.T.S.": ".MC",
    "Malaysian Stock Exchange": ".KL",
    "Mexico Stock Exchange (BMV)": ".MX",
    "Munich Stock Exchange": ".MU",
    "Nasdaq OMX Copenhagen": ".CO",
    "Nasdaq OMX Helsinki": ".HE",
    "Nasdaq OMX Iceland": ".IC",
    "Nasdaq OMX Riga": ".RG",
    "Nasdaq OMX Stockholm": ".ST",
    "Nasdaq OMX Tallinn": ".TL",
    "Nasdaq OMX Vilnius": ".VS",
    "Nasdaq Stock Exchange": "",
    "National Stock Exchange of India": ".NS",
    "New York Commodities Exchange (COMEX)": ".CMX",
    "New York Mercantile Exchange (NYMEX)": ".NYM",
    "New Zealand Stock Exchange (NZX)": ".NZ",
    "Oslo Stock Exchange": ".OL",
    "Philippine Stock Exchange Indices": ".PS",
    "Prague Stock Exchange Index": ".PR",
    "Qatar Stock Exchange": ".QA",
    "Santiago Stock Exchange": ".SN",
    "Sao Paolo Stock Exchange (BOVESPA)": ".SA",
    "Saudi Stock Exchange (Tadawul)": ".SAU",
    "Shanghai Stock Exchange": ".SS",
    "Shenzhen Stock Exchange": ".SZ",
    "Singapore Stock Exchange (SGX)": ".SI",
    "Stock Exchange of Thailand (SET)": ".BK",
    "Stuttgart Stock Exchange": ".SG",
    "Swiss Exchange (SIX)": ".SW",
    "TSX Venture Exchange (TSXV)": ".V",
    "Tel Aviv Stock Exchange": ".TA",
    "Taiwan OTC Exchange": ".TWO",
    "Taiwan Stock Exchange (TWSE)": ".TW",
    "Tokyo Stock Exchange": ".T",
    "Toronto Stock Exchange (TSX)": ".TO",
    "Vienna Stock Exchange": ".VI",
    "Warsaw Stock Exchange": ".WA"
}

fig = plt.figure()

def plot_graf():
    try:
        fig.clear()
        ticker = aksje_input.get()
        børs = børs_boks.get()
        børs_ticker = børser[børs]
        ticker = f"{ticker}{børs_ticker}"
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