import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
#from formprincipal import mainform

class mainVodafone:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Vodafone')
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

        crs.execute("SELECT an,carteleV, abonamenteV FROM furnizori")
        col1=Label(self.parent,width=10,text='AN',borderwidth=1, relief='ridge',anchor='center',bg='red4')
        col1.grid(row=0,column=0)
        col2=Label(self.parent,width=18,text='CARTELE PREPLATITE',borderwidth=1, relief='ridge',anchor='center',bg='red4')
        col2.grid(row=0,column=1)
        col3=Label(self.parent,width=12,text='ABONAMENTE',borderwidth=1, relief='ridge',anchor='center',bg='red4')
        col3.grid(row=0,column=2)
        i=1
        for user in crs: 
            for j in range(len(user)):
                e = Entry(self.parent, width=10, fg='red4',bg='#F0F0F8', border=0) 
                e.grid(row=i, column=j)
                e.insert(END, user[j])
                
            i=i+1
            print()

        info = """Descopera operatorul de telecomunicatii Vodafone România.
                 Vodafone România a fost înființată în anul 1997 și a devenit rapid unul dintre principalii jucători de pe piața telecomunicațiilor din țară. 
                 Compania a investit semnificativ în infrastructură și tehnologie pentru a oferi servicii de înaltă calitate și acoperire extinsă în întreaga țară.
                 Portofoliul de servicii al Vodafone România include planuri de telefonie mobilă cu opțiuni flexibile și beneficii suplimentare, 
                servicii de internet mobil pentru acces rapid la internet pe dispozitive mobile, 
                servicii fixe, cum ar fi telefonia fixă și internetul fix,
                precum și servicii de televiziune prin cablu și satelit. 
                 Compania oferă, de asemenea, servicii personalizate pentru segmentul business, inclusiv soluții de comunicații integrate, 
                servicii de conectivitate și soluții de securitate cibernetică.
                 In tabelul pus la dispozitie se regasesc date cu privire la numarul de utilizatori care au ales serviciile companiei.
        """
        infoL = tk.Label(self.parent,  text=info, font=('Microsoft YaHei UI Light',10, 'bold')
                            ,fg='red4',  bg='#F0F0F8')
        infoL.place(x=0, y=500)

        self.fotoV = Image.open("vdf.png")
        self.foto1V = self.fotoV.resize((420,420), Image.ANTIALIAS)
        self.vodafoneFoto = ImageTk.PhotoImage(self.foto1V)
        imagL=tk.Label(self.parent, image= self.vodafoneFoto, bg='#F0F0F8')
        imagL.image = self.vodafoneFoto
        imagL.place(x=700, y= 70)

        button_close = tk.Button(self.parent, text="Back to start", border=0, 
                        bg='#F0F0F8',fg='red4',activebackground='#F0F0F8', activeforeground='red4', command= self.redirect_main)
        button_close.place(x=1100, y=650)

    def redirect_main(self):
        from dataview import mainData
        self.parent.withdraw()
        data_page_window = tk.Toplevel() 
        mainData(data_page_window) 

"""root= Tk() 
gui = mainVodafone(root)
root.mainloop()"""