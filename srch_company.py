import tkinter as tk
import requests
class Serch_box:
    def __init__(self,w):
        self.w = w
        self.entry = tk.Entry(self.w, width=31)
        self.entry.place(x=10,y=10)

        search_button = tk.Button(self.w, text="Search", command=self.search_symbols)
        search_button.place(x=205,y=6)
        select_button = tk.Button(self.w, text="Confirm",command=self.confirm_symbol)
        select_button.place(x=100,y=197)
        self.results = tk.Listbox(self.w, width=40, height=10)
        self.results.place(x=7,y=31)
        self.selected_company = tk.Text(w, height=1, width=25)
        self.selected_company.place(x=25, y=230)
    def search_symbols(self):
        self.query = self.entry.get()
        if self.query:
            api_key = 'OQTLNXS18F8786IJ'
            url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={self.query}&apikey={api_key}'
            response = requests.get(url)
            data = response.json()
            self.results.delete(0, tk.END)
            for symbol_info in data.get('bestMatches', []):
                symbol = symbol_info.get('1. symbol', '')
                self.results.insert(tk.END, symbol)

    def confirm_symbol(self):
        for i in self.results.curselection():
            self.x = self.results.get(i)
            self.selected_company.insert(tk.END,self.x)

