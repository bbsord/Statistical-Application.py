import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
#from formprincipal import mainform

class mainTelekom:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Telekom')
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

        crs.execute("SELECT an,carteleT, abonamenteT FROM furnizori")
        col1=Label(self.parent,width=10,text='AN',borderwidth=1, relief='ridge',anchor='center',bg='hotpink')
        col1.grid(row=0,column=0)
        col2=Label(self.parent,width=18,text='CARTELE PREPLATITE',borderwidth=1, relief='ridge',anchor='center',bg='hotpink')
        col2.grid(row=0,column=1)
        col3=Label(self.parent,width=12,text='ABONAMENTE',borderwidth=1, relief='ridge',anchor='center',bg='hotpink')
        col3.grid(row=0,column=2)
        i=1
        for user in crs: 
            for j in range(len(user)):
                e = Entry(self.parent, width=10, fg='hotpink',bg='#F0F0F8', border=0) 
                e.grid(row=i, column=j)
                e.insert(END, user[j])
                
            i=i+1
            print()

        info = """Descopera operatorul de telecomunicatii Telekom România.
                 Prima marcă sub care OTE a operat în România a fost Cosmorom,
             iar opțiunea a fost dezvoltarea unei infrastructuri proprii în banda de 1800 MHz.
                 În 2005, după ce rețeaua de acoperire a devenit extinsă, compania a trecut prin primul rebranding,
             lansând denumirea de Cosmote și orientându-se puternic către segmentul clienților de servicii preplătite.
                 Marca Cosmote și-a încetat existența în România la 13 septembrie 2014, 
             în urma fuzionării cu Romtelecom și a rebrandingului celor două în comun sub numele de Telekom Romania.
                 În prezent, Telekom Romania este într-un proces de reorganizare, 
             prin intermediul caruia operatorul ofera internet 4G nelimitat (cartela preplatita si abonament).
        """
        infoL = tk.Label(self.parent,  text=info, font=('Microsoft YaHei UI Light',10, 'bold')
                            ,fg='hotpink',  bg='#F0F0F8')
        infoL.place(x=0, y=500)

        self.fotoT = Image.open("telekom.png")
        self.foto1T = self.fotoT.resize((420,420), Image.ANTIALIAS)
        self.telekomFoto = ImageTk.PhotoImage(self.foto1T)
        imagL=tk.Label(self.parent, image= self.telekomFoto, bg='#F0F0F8')
        imagL.image = self.telekomFoto
        imagL.place(x=700, y= 70)

        button_close = tk.Button(self.parent, text="Back to start", border=0, 
                        bg='#F0F0F8',fg='hotpink',activebackground='#F0F0F8', activeforeground='hotpink', command= self.redirect_main)
        button_close.place(x=1100, y=650)

    def redirect_main(self):
        from dataview import mainData
        self.parent.withdraw()
        data_page_window = tk.Toplevel() 
        mainData(data_page_window) 