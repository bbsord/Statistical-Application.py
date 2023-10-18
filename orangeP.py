import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

class mainOrange:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Orange')
        self.parent.geometry('1200x700')
        self.parent.resizable(0,0)
        self.parent.configure(background = "#F0F0F8")

        cnt = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="bianca76",
            database="appstatistic"
        )

        crs = cnt.cursor()

        crs.execute("SELECT an,carteleO, abonamenteO FROM furnizori")
        col1=Label(self.parent,width=10,text='AN',borderwidth=1, relief='ridge',anchor='center',bg='orange')
        col1.grid(row=0,column=0)
        col2=Label(self.parent,width=18,text='CARTELE PREPLATITE',borderwidth=1, relief='ridge',anchor='center',bg='orange')
        col2.grid(row=0,column=1)
        col3=Label(self.parent,width=12,text='ABONAMENTE',borderwidth=1, relief='ridge',anchor='center',bg='orange')
        col3.grid(row=0,column=2)
        i=1
        for user in crs: 
            for j in range(len(user)):
                e = Entry(self.parent, width=10, fg='orange',bg='#F0F0F8', border=0) 
                e.grid(row=i, column=j)
                e.insert(END, user[j])
                
            i=i+1
            print()

        info = """Descopera operatorul de telecomunicatii Orange România.
                 Orange România S.A. este cel mai mare operator GSM din România. 
                 Până în aprilie 2002, Orange a operat sub brand-ul Dialog.
                 Având o acoperire 3G a populației de 98%, Orange România oferă posibilitatea de a alege între planuri de abonamente flexibile, 
                ce pot fi personalizate, și cartele PrePay.
                 Orange se află în competiție directă cu Vodafone pentru cei 13,7 milioane de utilizatori de telefonie mobilă din România.
        """
        infoL = tk.Label(self.parent,  text=info, font=('Microsoft YaHei UI Light',10, 'bold')
                            ,fg='orange',  bg='#F0F0F8')
        infoL.place(x=0, y=500)

        self.fotoO = Image.open("orange.png")
        self.foto1O = self.fotoO.resize((420,420), Image.ANTIALIAS)
        self.orangeFoto = ImageTk.PhotoImage(self.foto1O)
        imagL=tk.Label(self.parent, image= self.orangeFoto, bg='#F0F0F8')
        imagL.image = self.orangeFoto
        imagL.place(x=700, y= 70)

        button_close = tk.Button(self.parent, text="Back to start", border=0, 
                        bg='#F0F0F8',fg='orange',activebackground='#F0F0F8', activeforeground='orange', command= self.redirect_main)
        button_close.place(x=1100, y=650)

    def redirect_main(self):
        from dataview import mainData, ImageLoader
        self.parent.withdraw()
        data_page_window = tk.Toplevel() 
        mainData(data_page_window) 