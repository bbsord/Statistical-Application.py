import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from dataview import mainData
from meanview import mainMean
from diagramview import mainDiagram
from progview import mainProg

class mainform:
    def __init__(self, parent):
        self.parent = parent
        parent.title('Start page')
        parent.geometry('1200x700+300+200')
        parent.configure(background = "#fff")
        parent.resizable(0,0) 
        
        
        imgbg = Image.open("bgimg.png")
        self.imgbgCopy = imgbg.copy()
        imagBG = ImageTk.PhotoImage(imgbg)
        self.lbImgBG = Label(parent, image = imagBG )
        self.lbImgBG.pack(fill = BOTH, expand= YES)
        self.lbImgBG.bind('<Configure>', self.resize_img)
        
    
        #canvas= Canvas(parent, width= 400, height= 400)
        #canvas.pack(fill=BOTH, expand=True)
        imgCanvas= PhotoImage(file="bgimg.png")
        #canvas.create_image(0, 0, image = imgCanvas, anchor = "nw")
        #canvas.create_text(200, 250, text="Bun venit")
        info = """ Bun venit! 
        Accesati informatiile prin apasarea butoanelor.
        """

        lblTitlu = tk.Label(parent, width=40 , text=info, font=('Microsoft YaHei UI Light',11, 'bold')
                            ,fg='#57a1f8')
        lblTitlu.place(rely=0.5, relx=0.5, anchor=CENTER)

        data_button = tk.Button(parent, width=20, text="Vizualizati datele", font=('Microsoft YaHei UI Light', 13, 'bold'),bg='white',fg='#57a1f8', border = 0, 
                        activebackground='white', activeforeground='#57a1f8', command =self.view_page)
        data_button.place(x=50, y=100)

        prog_button = tk.Button(parent, width=20, text="Vizualizare prognoza", font=('Microsoft YaHei UI Light', 13, 'bold'),bg='white',fg='#57a1f8', border = 0, 
                        activebackground='white', activeforeground='#57a1f8', command =self.prog_page)
        prog_button.place(x=50, y=600)

        medie_button = tk.Button(parent, width=20, text="Calculare medii", font=('Microsoft YaHei UI Light', 13, 'bold'),bg='white',fg='#57a1f8', border = 0, 
                        activebackground='white', activeforeground='#57a1f8', command =self.mean_page)
        medie_button.place(x=960, y=100)

        diagram_button = tk.Button(parent, width=20, text="Vizualizare diagrame", font=('Microsoft YaHei UI Light', 13, 'bold'),bg='white',fg='#57a1f8', border = 0, 
                        activebackground='white', activeforeground='#57a1f8', command =self.diagram_page)
        diagram_button.place(x=960, y=600)
        #logout_button = tk.Button(parent, width=20, text="Logout", font=('Microsoft YaHei UI Light', 13, 'bold'),bg='white',fg='#57a1f8', border = 0, 
        #                activebackground='white', activeforeground='#57a1f8', command =self.login_page)
        #logout_button.place(x=700, y=600)    
        
    def resize_img(self, event):
        nWidth = event.width
        nHeight = event.height

        self.imgbg = self.imgbgCopy.resize((nWidth, nHeight))
        self.imagBG = ImageTk.PhotoImage(self.imgbg)
        self.lbImgBG.configure(image = self.imagBG)


    def view_page(self):
        secWindowData  = tk.Toplevel()
        mainData(secWindowData)
        self.parent.withdraw()

    def mean_page(self):
        secWindowMean  = tk.Toplevel()
        mainMean(secWindowMean)
        self.parent.withdraw()

    def diagram_page(self):
        secWindowDiagram  = tk.Toplevel()
        mainDiagram(secWindowDiagram)
        self.parent.withdraw()

    def prog_page(self):
        secWindowProg  = tk.Toplevel()
        mainProg(secWindowProg)
        self.parent.withdraw()
    
""""root= Tk() 
gui = mainform(root)
root.mainloop()"""

