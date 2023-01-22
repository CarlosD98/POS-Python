import tkinter as tk
from tkinter import messagebox
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
    try:
        res = Data.query(query)
        if not res.empty:
            if df.loc[0].Codigo == '':
                df.loc[0]= res.iloc[0]
            else:
                df.loc[len(df)]= res.iloc[0]
            table.redraw()
            table.autoResizeColumns()
        else:
            messagebox.showerror(message= "No encontre "+barCode.get()+" denro de "+dropdown.get()+" intente en otro csv",
            title="No encontrado")
    except pd.errors.UndefinedVariableError:
        messagebox.showerror(message= "No encontre "+barCode.get()+" denro de "+dropdown.get()+" intente en otro csv",
        title="No encontrado")
    barCode.set('')

def submit(event):
    if (barCode.get() == '' or barCode.get() == None) :
        return
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

    deleteRowBtn = tk.Button(Frame,text="Eliminar fila seleccionada", command=deleteSelectedRow)
    clearBtn = tk.Button(Frame,text="Limpiar registros", command=clearTable)
    exportExcelBtn =tk.Button(Frame,text="Exportar a Excel",command=exportToExcel )
    deleteRowBtn.pack(pady=20)
    clearBtn.pack(pady=20)
    exportExcelBtn.pack(pady=20)
    
def resetTable():
    return pd.DataFrame({
    'Codigo':[''],
    'Nombre':[''],
    'Direccion':[''],
    'Celular':['']})


def deleteSelectedRow():
    table.deleteRow()
    

def clearTable():
    table.model.df = resetTable()
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
df = resetTable()
frameTable = tk.Frame(window, height=100)
frameTable.pack(side=tk.LEFT,fill='both',expand=True,)
table = Table(frameTable, dataframe = df)
table.show()
frameButtons = tk.Frame(window,width=200,background='green')
renderButtons(frameButtons)
frameButtons.pack(fill='y', side=tk.RIGHT)
window.mainloop()
   