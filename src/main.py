import tkinter as tk
import pandas as pd
from pandastable import Table
from os import listdir
from os.path import isfile, join

dataFolder="data/"

def submit(event):
    search()
def renderDropdown():
    files = [fn for fn in listdir(dataFolder)
            if any(fn.endswith(ext) for ext in ["csv"])]
    
    input = tk.OptionMenu( window,dropdown, *files,)
    dropdown.set("fedex.csv")
    input.pack()
    input.place(x= 200, y=8)

def renderCodeInput():

    label = tk.Label(text="Código de barras")
    entry  = tk.Entry(textvariable=barCode)
    label.pack()
    entry.pack()
    label.place(x=300,y=8)
    entry.bind('<Return>', submit)


window = tk.Tk()
barCode = tk.StringVar()
dropdown= tk.StringVar()
window.geometry('1200x900+10+10')
window.title('Control de guias')
DataSource = "fedex.csv"
renderCodeInput()
renderDropdown()
df = pd.DataFrame({
    'Codigo':[''],
    'Nombre':[''],
    'Direccion':[''],
    'Celular':['']
})

frameTable = tk.Frame(window, height=100)
frameTable.pack(fill='x',expand=False)

table = Table(frameTable, dataframe = df)
table.show()

def search():
    Data = pd.read_csv(dataFolder+dropdown.get())
    query = "Codigo == " + barCode.get()
    res = Data.query(query)
    if not res.empty:
        if df.loc[0].Codigo == '':
            df.loc[0]= res.iloc[0]
        else:
            df.loc[len(df)]= res.iloc[0]
        table.redraw()
        table.autoResizeColumns()

window.mainloop()

    