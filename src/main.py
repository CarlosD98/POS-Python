import tkinter as tk
import pandas as pd
from pandastable import Table
from os import listdir
from os.path import isfile, join

dataFolder="data/"

files = [fn for fn in listdir(dataFolder)
        if any(fn.endswith(ext) for ext in ["csv"])]


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

def submit(event):
    search()


def renderInputs(Frame:tk.Frame):
    source = tk.OptionMenu( Frame,dropdown, *files,)
    label = tk.Label(Frame, text="Código de barras")
    entry  = tk.Entry(Frame, textvariable=barCode)
    label.pack(side=tk.LEFT,padx=5,pady=10)
    entry.pack(side=tk.LEFT, padx=5, pady=10)
    entry.bind('<Return>', submit)
    dropdown.set("fedex.csv")
    source.pack(side=tk.RIGHT,padx=5,pady=10)

def renderButtons(Frame:tk.Frame):
    return


window = tk.Tk()
barCode = tk.StringVar()
dropdown= tk.StringVar()
window.geometry('1200x900+10+10')
window.title('Control de guias')
DataSource = "fedex.csv"
frameInputs = tk.Frame(window, height = 50, background='red')
renderInputs(frameInputs)
frameInputs.pack(fill='x')
tk.Frame(window, height = 15, background='black').pack(fill=tk.BOTH)
df = pd.DataFrame({
    'Codigo':[''],
    'Nombre':[''],
    'Direccion':[''],
    'Celular':['']
})

frameTable = tk.Frame(window, height=100)
frameTable.pack(side=tk.LEFT,fill='both',expand=True,)
table = Table(frameTable, dataframe = df)
table.show()
frameButtons = tk.Frame(window,width=200,background='green')
# renderButtons(frameButtons)
frameButtons.pack(fill='y', side=tk.RIGHT)
window.mainloop()
   