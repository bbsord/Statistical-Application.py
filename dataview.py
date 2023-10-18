import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from orangeP import mainOrange
from telekomP import mainTelekom
from vodafoneP import mainVodafone

class ImageLoader:
    def __init__(self):
        self.image_references = {}  

    def load_image(self, image_path):
        image = Image.open(image_path)
        resized_image = image.resize((150, 150), Image.ANTIALIAS)
        photo_image = ImageTk.PhotoImage(resized_image)
        return photo_image

    def get_image(self, image_path):
        if image_path not in self.image_references:
            self.image_references[image_path] = self.load_image(image_path)
        return self.image_references[image_path]

class mainData:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('View Data')
        self.parent.geometry('1200x700')
        self.parent.resizable(0,0)
        self.parent.configure(background = "white")
       
        self.image_loader = ImageLoader()

        self.orange_foto = self.image_loader.get_image("orange.png")
        orangeB = tk.Button(self.parent, text = "Orange", image = self.orange_foto, border=0, command =self.orangeP)
        orangeB.pack()
        orangeB.place(x=200, y=280)
        

        foto2 = Image.open("telekom.png")
        foto2R = foto2.resize((150,150), Image.ANTIALIAS)
        self.telekom_foto = ImageTk.PhotoImage(foto2R)
        telekomB = tk.Button(self.parent, text = "Telekom", image = self.telekom_foto, border=0, command =self.telekomP)
        telekomB.place(x=550, y=280)

        foto3 = Image.open("vdf.png")
        foto3R = foto3.resize((150,150), Image.ANTIALIAS)
        self.vodafone_foto = ImageTk.PhotoImage(foto3R)
        vodafoneB = tk.Button(self.parent, text = "Vodafone", image = self.vodafone_foto, border=0, command =self.vodafoneP)
        vodafoneB.place(x=900, y=280)

        button_close = tk.Button(self.parent, text="Back to start", border=0, 
                        bg='white',fg='black',activebackground='white', activeforeground='black', command= self.redirect_main)
        button_close.place(x=1100, y=650)
    
    def orangeP(self):
        orangeWindowData  = tk.Toplevel()
        mainOrange(orangeWindowData)
        self.parent.withdraw()
    
    def telekomP(self):
        telekomWindowData  = tk.Toplevel()
        mainTelekom(telekomWindowData)
        self.parent.withdraw()
    
    def vodafoneP(self):
        vdfWindowData  = tk.Toplevel()
        mainVodafone(vdfWindowData)
        self.parent.withdraw()

    def redirect_main(self):
        from formprincipal import mainform
        self.parent.withdraw()
        start_page_window = tk.Toplevel() 
        mainform(start_page_window) 
        
        

    


"""root= Tk() 
gui = mainData(root)
root.mainloop()"""

"""cnt = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="bianca76",
            database="appstatistic"
        )

        crs = cnt.cursor()

        crs.execute("SELECT * FROM user limit 0,10")
        i=0 
        for user in crs: 
            for j in range(len(user)):
                e = Entry(parent, width=10, fg='blue') 
                e.grid(row=i, column=j)
                e.insert(END, user[j])
                
            i=i+1
            print()# line break at the end of one row"""