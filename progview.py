import tkinter as tk
from tkinter import *
import pandas as pd  
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class mainProg:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('View Prediction')
        self.parent.geometry('1400x700')
        self.parent.resizable(0,0)
        self.parent.configure(background = "white")

        engine = create_engine("mysql+pymysql://root:bianca76@localhost/appstatistic")
        cnt = engine.connect()

        qMeanUtR ="SELECT AVG(utilizatoriRez) FROM trafic"
        selectUtR ="SELECT utilizatoriRez FROM trafic"
        qMeanTfR ="SELECT AVG(traficRez) FROM trafic"
        selectTfR ="SELECT traficRez FROM trafic"

        sql_query1 = pd.read_sql(qMeanUtR, cnt)
        sql_selectUtR = pd.read_sql(selectUtR, cnt)
        array_utilRez = sql_selectUtR['utilizatoriRez'].values
        n = np.size(array_utilRez)
        avg_utilRez = sql_query1.iloc[0, 0]
        avg_utilRez = pd.to_numeric(avg_utilRez)

        sql_query2 = pd.read_sql(qMeanTfR, cnt)
        sql_selectTfR = pd.read_sql(selectTfR, cnt)
        array_tfR = sql_selectTfR['traficRez'].values
        avg_traficRez = sql_query2.iloc[0, 0]
        avg_traficRez = pd.to_numeric(avg_traficRez)

        Sxy = np.sum(array_utilRez * array_tfR) - n*avg_utilRez*avg_traficRez
        Sxx = np.sum(array_utilRez * array_utilRez) - n*avg_utilRez*avg_utilRez
        b1 = Sxy/Sxx
        simply_b1 = round(b1, 2)
        b0 = avg_traficRez - b1 * avg_utilRez
        simply_b0 = round(b0, 2)
        pred_tfR = b1 * array_utilRez + b0

        eroare = array_tfR - pred_tfR
        se = np.sum(eroare**2)
        SSt = np.sum((array_tfR-avg_traficRez)**2)
        R2 = 1 - (se/SSt)
        simply_R2 = round(R2, 2)
    
        fig = plt.figure()
        ax = plt.subplot()
        ax.scatter(array_utilRez, array_tfR, label='2006-2021', color = 'red')
        ax.plot(array_utilRez, pred_tfR, label='Preziceri', color = 'blue')
        ax.legend(title="Utilizatori Rezidentiali")

        plot1 = FigureCanvasTkAgg(fig, self.parent)
        plot1.get_tk_widget().grid(row=1,column=1,columnspan=2,padx=30,pady=5)

        label_b1 = tk.Label(self.parent, text="Panta b1 = " + str(simply_b1),
                            bg = 'white', fg='#57a1f8',font=('Microsoft YaHei UI Light', 9, 'bold'))
        label_b1.place(x=100, y= 500)
        label_b0 = tk.Label(self.parent, text="Ordonata de origine b0 = " + str(simply_b0),
                            bg = 'white', fg='#57a1f8',font=('Microsoft YaHei UI Light', 9, 'bold'))
        label_b0.place(x=100, y= 520)
        label_se = tk.Label(self.parent, text="e^2 = " + str(se),
                            bg = 'white', fg='#57a1f8',font=('Microsoft YaHei UI Light', 9, 'bold'))
        label_se.place(x=100, y= 540)
        label_R2 = tk.Label(self.parent, text="R^2 = " + str(simply_R2),
                            bg = 'white', fg='#57a1f8',font=('Microsoft YaHei UI Light', 9, 'bold'))
        label_R2.place(x=100, y= 560)
        
        qMeanUtB ="SELECT AVG(utilizatoriBus) FROM trafic"
        selectUtB ="SELECT utilizatoriBus FROM trafic"
        qMeanTfB ="SELECT AVG(traficBus) FROM trafic"
        selectTfB ="SELECT traficBus FROM trafic"

        sql_queryB = pd.read_sql(qMeanUtB, cnt)
        sql_selectUtB = pd.read_sql(selectUtB, cnt)
        array_utilBus = sql_selectUtB['utilizatoriBus'].values
        nB = np.size(array_utilBus)
        avg_utilBus= sql_queryB.iloc[0, 0]
        avg_utilBus = pd.to_numeric(avg_utilBus)

        sql_queryTrfB = pd.read_sql(qMeanTfB, cnt)
        sql_selectTfB = pd.read_sql(selectTfB, cnt)
        array_tfB = sql_selectTfB['traficBus'].values
        avg_traficBus = sql_queryTrfB.iloc[0, 0]
        avg_traficBus = pd.to_numeric(avg_traficBus)

        SxyB = np.sum(array_utilBus * array_tfB) - nB*avg_utilBus*avg_traficBus
        SxxB = np.sum(array_utilBus * array_utilBus) - nB*avg_utilBus*avg_utilBus
        b1B = SxyB/SxxB
        simply_b1B = round(b1B, 2)
        b0B = avg_traficBus - b1B * avg_utilBus
        simply_b0B = round(b0B, 2)
        pred_tfB = b1B * array_utilBus + b0B

        eroareB = array_tfB - pred_tfB
        seB = np.sum(eroareB**2)
        SStB = np.sum((array_tfB-avg_traficBus)**2)
        R2B = 1 - (seB/SStB)
        simply_R2B = round(R2B, 2)
    
        fig2 = plt.figure()
        ax2 = plt.subplot()
        ax2.scatter(array_utilBus, array_tfB, label='2006-2021', color = 'red')
        ax2.plot(array_utilBus, pred_tfB, label='Previziune', color = 'blue')
        ax2.legend(title="Utilizatori Business")

        plot1 = FigureCanvasTkAgg(fig2, self.parent)
        plot1.get_tk_widget().grid(row=1,column=10,columnspan=2,padx=30,pady=5)

        label_b1B = tk.Label(self.parent, text="Panta b1 = " + str(simply_b1B),
                            bg = 'white', fg='#57a1f8',font=('Microsoft YaHei UI Light', 9, 'bold'))
        label_b1B.place(x=800, y= 500)
        label_b0B = tk.Label(self.parent, text="Ordonata de origine b0 = " + str(simply_b0B),
                            bg = 'white', fg='#57a1f8',font=('Microsoft YaHei UI Light', 9, 'bold'))
        label_b0B.place(x=800, y= 520)
        label_seB = tk.Label(self.parent, text="e^2 = " + str(seB),
                            bg = 'white', fg='#57a1f8',font=('Microsoft YaHei UI Light', 9, 'bold'))
        label_seB.place(x=800, y= 540)
        label_R2B = tk.Label(self.parent, text="R^2 = " + str(simply_R2B),
                            bg = 'white', fg='#57a1f8',font=('Microsoft YaHei UI Light', 9, 'bold'))
        label_R2B.place(x=800, y= 560)

        button_close = tk.Button(self.parent, text="Back to start", border=0, 
                        bg='white',fg='black',activebackground='white', activeforeground='black', command= self.redirect_main)
        button_close.place(x=1300, y=650)

    def redirect_main(self):
        from formprincipal import mainform
        self.parent.withdraw()
        start_page_window = tk.Toplevel() 
        mainform(start_page_window) 
        
"""root= Tk() 
gui = mainProg(root)
root.mainloop()"""

