import tkinter as tk
from tkinter import messagebox
import pandas as pd
from pandastable import Table
from os import listdir
from tkinter import filedialog

dataFolder="data/"

files = [fn for fn in listdir(dataFolder)
        if any(fn.endswith(ext) for ext in ["csv"])]

def processBarCode():
    if dropdown.get() == 'fedex.csv':
        return barCode.get()[-12:]
    return barCode.get()

def search():
    Data = pd.read_csv(dataFolder+dropdown.get())
    query = "Codigo == " + processBarCode()
    try:
        res = Data.query(query)
        if not res.empty:
            table.model.df =pd.concat([table.model.df,res],ignore_index=True)
            table.autoResizeColumns()
            table.redraw()
        else:
            messagebox.showerror(message= 
            "No encontre "+barCode.get()+" denro de "+dropdown.get()+" intente en otro csv",
            title="No encontrado")
    except pd.errors.UndefinedVariableError:
        messagebox.showerror(message= 
        "No encontre "+barCode.get()+" denro de "+dropdown.get()+" intente en otro csv",
        title="No encontrado")
    barCode.set('')

def submit(event):
    event
    if (barCode.get() == '' or barCode.get() == None) :
        return 'break'
    search()
    return 'break'

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
    selectedTableIndex = table.getSelectedRow()
    selected=table.model.getRecordAtRow(selectedTableIndex).Codigo
    dfIndex= table.model.df.query('Codigo =='+str(selected)).index
    table.model.df.drop(dfIndex,inplace=True)
    if (len(table.model.df)==0):
        clearTable()
    table.redraw()

def clearTable():
    table.model.df = resetTable()
    table.redraw()
    

def exportToExcel():
    filePath = filedialog.asksaveasfilename()
    print(filePath)
    # creating an output excel file
    resultExcelFile = pd.ExcelWriter(filePath+'.xlsx')

    # converting the csv file to an excel file
    table.model.df.to_excel(resultExcelFile, index=False)

    # saving the excel file
    resultExcelFile.save()
    messagebox.showinfo('Archivo generado', 'Se ha generado el documento de Excel correctamente.')

window = tk.Tk()
barCode = tk.StringVar()
dropdown= tk.StringVar()
window.geometry('1200x900+10+10')
window.title('Control de guias')
DataSource = "fedex.csv"
frameInputs = tk.Frame(window, height = 50, background='AliceBlue' )
renderInputs(frameInputs)
frameInputs.pack(fill='x')
tk.Frame(window, height = 15, background='black').pack(fill=tk.BOTH)
frameTable = tk.Frame(window, height=100)
frameTable.pack(side=tk.LEFT,fill='both',expand=True,)
table = Table(frameTable, dataframe = resetTable())
table.adjustColumnWidths(limit=50)
table.show()
frameButtons = tk.Frame(window,width=200,background='AliceBlue')
renderButtons(frameButtons)
frameButtons.pack(fill='y', side=tk.RIGHT)
window.mainloop()