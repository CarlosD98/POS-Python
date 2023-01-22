import tkinter as tk
import pandas as pd
from pandastable import Table
from os import listdir
from tkinter import filedialog

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


def deleteSelectedRow():
    table.deleteRow()
    

def clearTable():
    df.drop(df.index,inplace=True)
    table.redraw()
    

def exportToExcel():
    filePath = filedialog.asksaveasfile()
    # creating an output excel file
    resultExcelFile = pd.ExcelWriter(filePath.name+'.xlsx')

    # converting the csv file to an excel file
    df.to_excel(resultExcelFile, index=False)

    # saving the excel file
    resultExcelFile.save()

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

deleteRowBtn = tk.Button(text="Eliminar fila seleccionada", command=deleteSelectedRow)
clearBtn = tk.Button(text="Limpiar registros", command=clearTable)
exportExcelBtn =tk.Button(text="Exportar a Excel",command=exportToExcel )
deleteRowBtn.pack()
clearBtn.pack()
exportExcelBtn.pack()
frameButtons = tk.Frame(window,width=200,background='green')
# renderButtons(frameButtons)
frameButtons.pack(fill='y', side=tk.RIGHT)
window.mainloop()
   