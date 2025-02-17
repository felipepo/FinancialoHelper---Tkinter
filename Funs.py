import tkinter as tk
import pickle

'''
General Functions
	update_Var
	SetMainWindow
	SetGridWeight
	ShowWindow
	showdic
	AddTransaction
	GetMY
	saveData
	loadData
'''
   
def SetGridWeight(col,row,frm, colExceptions =[], rowExceptions = []):
    #Function to set the weight of all the cells from a frame
    for ncol in range(col):
        if ncol in colExceptions:
            continue
        tk.Grid.columnconfigure(frm, ncol, weight=1)
    for nrow in range(row):
        if nrow in rowExceptions:
            continue
        tk.Grid.rowconfigure(frm, nrow, weight=1)

#=========================================================================================
def ShowWindow(frm):
    frm.tkraise()


#=========================================================================================
def showdic(dict):
    for x in dict:
        print (x)
        for y in dict[x]:
            print ('               ',y,':',dict[x][y])
   
#=========================================================================================     
def AddTransaction(objAcc, category, value, date, comment, bankAccount):
    month, year = GetMY(date)
    objAcc.totalAmount += int(value)
    objAcc.transactions["trans"+str(len(objAcc.transactions))] = {
            "Category": category,
            "Value": value,
            "Date": date,
            "Comment": comment,
            "BankAccount": bankAccount,
            "Month": month,
            "Year": year
        }

#=========================================================================================
def GetMY(date):
    months = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
    splitDate = date.split("/")
    month = months[int(splitDate[1])-1]
    year = splitDate[2]
    return month, year

#=========================================================================================
def saveData(data):
    outfile = open("DataBase/data", "wb")
    pickle.dump(data,outfile)
    outfile.close()

#=========================================================================================
def loadData():
    infile = open("DataBase/data", "rb")
    loadedData = pickle.load(infile)
    infile.close()
    return loadedData
