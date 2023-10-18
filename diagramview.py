import tkinter as tk
from tkinter import *
import pandas as pd  
from sqlalchemy import create_engine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class mainDiagram:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('View Diagram')
        self.parent.geometry('1200x700')
        self.parent.resizable(0,0)
        self.parent.configure(background = "white")

        engine = create_engine("mysql+pymysql://root:bianca76@localhost/appstatistic")
        cnt = engine.connect()

        query ="SELECT an, carteleO, carteleT, carteleV  FROM furnizori"

        sql_query = pd.read_sql(query, cnt)
        df = pd.DataFrame(sql_query, columns=['an','carteleO','carteleT', 'carteleV'])
        
        fig1= df.plot.line(title="Utilizatori ce aleg cartele",x='an',y='carteleO').get_figure()
        df.plot.line(x='an',y='carteleT', ax = fig1.gca())
        df.plot.line(x='an',y='carteleV', ax = fig1.gca())
        plot1 = FigureCanvasTkAgg(fig1, self.parent)
        plot1.get_tk_widget().grid(row=1,column=1,columnspan=2,padx=30,pady=5)
        
        button_close = tk.Button(self.parent, text="Back to start", border=0, 
                        bg='white',fg='black',activebackground='white', activeforeground='black', command= self.redirect_main)
        button_close.place(x=1100, y=650)

    def redirect_main(self):
        from formprincipal import mainform
        self.parent.withdraw()
        start_page_window = tk.Toplevel() 
        mainform(start_page_window) 

"""root= Tk() 
gui = mainDiagram(root)
root.mainloop()"""
