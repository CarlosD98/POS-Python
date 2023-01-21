import tkinter as tk
import pandas as pd
from pandastable import Table

window = tk.Tk()
window.geometry('1600x900+10+10')
window.title('Control de guias')
label = tk.Label(text="CODIGO")
entry  = tk.Entry()
label.pack()
entry.pack()

DataSource = pd.read_csv("data/fedex.csv")

df = pd.DataFrame({
    'Codigo':[],
    'Nombre':[],
    'Direccion':[],
    'Celular':[]
})

frameTable = tk.Frame(window)
frameTable.pack(fill='both',expand=True)

pt = Table(frameTable, dataframe = df)
pt.redraw()
pt.show()

window.mainloop()

def updateTable():
    df.add()
    pt.redraw()
