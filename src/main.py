import tkinter as tk
import pandas as pd
from pandastable import Table
from os import listdir
from os.path import isfile, join

dataFolder="data/"

def renderCodeInput():

    label = tk.Label(text="Código de barras")
    entry  = tk.Entry()
    label.pack()
    entry.pack()
    label.place(x=600, y=3)



window = tk.Tk()
window.geometry('1600x900+10+10')
window.title('Control de guias')
DataSource = "fedex.csv"
renderCodeInput()
files = [fn for fn in listdir(dataFolder)
            if any(fn.endswith(ext) for ext in ["csv"])]
    
clicked = tk.StringVar()
clicked.set("fedex.csv")

drop = tk.OptionMenu( window,clicked, *files,)
drop.pack()
drop.place(x= 450, y=2)

Data = pd.read_csv("data/fedex.csv")
Data.values
df = pd.DataFrame({
    'Codigo':[''],
    'Nombre':[''],
    'Direccion':[''],
    'Celular':['']
})

frameTable = tk.Frame(window, height=100)
frameTable.pack(fill='both',expand=True)

table = Table(frameTable, dataframe = df)
table.show()
def search():
    Data = pd.read_csv(dataFolder+clicked.get())
    query = "Codigo == " + '392975632633'
    res = Data.query(query)
    if not res.empty:
        if df.loc[0].Codigo == '':
            df.loc[0]= res.iloc[0]
        else:
            df.loc[len(df)]= res.iloc[0]
        table.redraw()
def action():
    df.loc[len(df)]=df.loc[0]
    table.redraw()
    print(df.loc[0])

btn =tk.Button(text="add", command=search)
btn.pack()
window.mainloop()

def updateTable():
    df.add()
    table.redraw()




    