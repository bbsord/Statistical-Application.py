import tkinter as tk
from tkinter import *
from sqlalchemy import create_engine
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class mainMean:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('View Mean')
        self.parent.geometry('1200x700')
        self.parent.resizable(0,0)
        self.parent.configure(background = "white")

        engine = create_engine("mysql+pymysql://root:bianca76@localhost/appstatistic")
        cnt = engine.connect() 

        qMeanCarteleV ="SELECT AVG(carteleV) FROM furnizori"
        sql_query1 = pd.read_sql(qMeanCarteleV, cnt)
        avg_CarteleV = sql_query1.iloc[0, 0]
        avg_CarteleV = pd.to_numeric(avg_CarteleV)

        qMeanCarteleO ="SELECT AVG(carteleO) FROM furnizori"
        sql_query2 = pd.read_sql(qMeanCarteleO, cnt)
        avg_CarteleO = sql_query2.iloc[0, 0]
        avg_CarteleO = pd.to_numeric(avg_CarteleO)

        qMeanCarteleT ="SELECT AVG(carteleO) FROM furnizori"
        sql_query3 = pd.read_sql(qMeanCarteleT, cnt)
        avg_CarteleT = sql_query3.iloc[0, 0]
        avg_CarteleT = pd.to_numeric(avg_CarteleT)

        x = np.array([avg_CarteleV, avg_CarteleO, avg_CarteleT])
        y = ["Cartele Vodafone", "Cartele Orange", "Cartele Telekom"]
        ycolors = ["red","orange", "hotpink"]

        chart = plt.figure()
        ax = plt.subplot()
        pie_chart =ax.pie(x, labels=y, colors = ycolors, autopct='%1.1f%%')
        pie_chart[0][0].set_label(f"({avg_CarteleV})")
        pie_chart[0][1].set_label(f"({avg_CarteleO})")
        pie_chart[0][1].set_color('orange')
        pie_chart[0][2].set_label(f"({avg_CarteleT})")
        ax.set_title("Distributie Cartele")

        canvas = FigureCanvasTkAgg(chart, master= self.parent)
        canvas.get_tk_widget().grid(row=1,column=1,columnspan=2,padx=30,pady=5)


        button_close = tk.Button(self.parent, text="Back to start", border=0, 
                        bg='white',fg='black',activebackground='white', activeforeground='black', command= self.redirect_main)
        button_close.place(x=1100, y=650)

    def redirect_main(self):
        from formprincipal import mainform
        self.parent.withdraw()
        start_page_window = tk.Toplevel() 
        mainform(start_page_window) 

"""root= Tk() 
gui = mainMean(root)
root.mainloop()"""
        