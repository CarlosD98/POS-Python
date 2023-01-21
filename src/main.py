import tkinter as tk
import pandas as pd
from pandastable import Table

window = tk.Tk()

dataFolder="data/"
DataSource = "fedex.csv"

window.geometry('1600x900+10+10')
window.title('Control de guias')
label = tk.Label(text="CODIGO")
entry  = tk.Entry()
label.pack()
entry.pack()

Data = pd.read_csv("data/fedex.csv")

df = pd.DataFrame({
    'Codigo':["hola"],
    'Nombre':['como'],
    'Direccion':['estas'],
    'Celular':['?']
})

frameTable = tk.Frame(window)
frameTable.pack(fill='both',expand=True)

table = Table(frameTable, dataframe = df)
table.show()

window.mainloop()

def updateTable():
    df.add()
    table.redraw()

def reloadData():
    Data = pd.read_csv(dataFolder+DataSource)

def search():
    res = Data.query()
