import tkinter as tk 
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
from formprincipal import mainform

login_window = Tk()

#mainframe = tk.Frame(login_window , width=300, height=300)

# ----------- FORM ------------- #
login_window.title('Login')
login_window.geometry('925x500+300+200')
login_window.configure(bg = "#fff")
login_window.resizable(0,0)
login_window.deiconify()

img = Image.open("mobilelog.jpg")
imgR = img.resize((400,400), Image.ANTIALIAS)
imag = ImageTk.PhotoImage(imgR)
lbImg = tk.Label(login_window, image = imag)
lbImg.place(x = 450, y = 60)

#Functionalitati
def close_win():
    login_window.destroy() 

def login_user():
    if usernameEntry.get()=='' or parolaEntry.get()=='':
        messagebox.showerror('Eroare', 'Toate campurile trebuie completate!')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root',password='bianca76')
            crs = con.cursor()
        except:
            messagebox.showerror('Eroare', 'Eroare de conectare la baza de date!')
            return
        crs.execute('use appstatistic')
        query = 'select * from user where username = %s and parola = %s'
        crs.execute(query, (usernameEntry.get(), parolaEntry.get()))
        userExists = crs.fetchone()
        if userExists == None:
            messagebox.showerror('Eroare', 'Username sau parola invalida!')
        else:
            mainformwindow = tk.Toplevel()
            mainform(mainformwindow)
            login_window.withdraw() # hide the root
            mainformwindow.protocol("WM_DELETE_WINDOW", close_win) # close the app


def register_page():
    login_window.destroy()
    import register
    
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def parola_enter(event):
    if parolaEntry.get() == 'Parola':
        parolaEntry.delete(0, END)



# ----------- Login Page ------------- #
head = tk.Label(login_window, text='Login', font=('Microsoft YaHei UI Light', 23, 'bold'), bg='white', fg='#57a1f8')
head.place(x = 200, y = 5)

usernameEntry = tk.Entry(login_window, width= 25, fg = 'black', bg = 'white', borde = 0, font =('Microsoft YaHei UI Light', 12))
usernameEntry.place(x = 75, y = 80)    
usernameEntry.insert(0, 'Username') 
usernameEntry.bind('<FocusIn>', user_enter)
frame1 = tk.Frame(login_window, width=370, height = 2, bg = '#57a1f8').place(x=70, y=107)

parolaEntry = tk.Entry(login_window, width= 25, fg = 'black', bg = 'white', borde = 0, font =('Microsoft YaHei UI Light', 12), show='*')
parolaEntry.place(x = 75, y = 150)
parolaEntry.insert(0, 'Parola')
parolaEntry.bind('<FocusIn>', parola_enter)
frame2 = tk.Frame(login_window, width=370, height = 2, bg = '#57a1f8').place(x=70, y=177)

regButton = tk.Button(login_window,text="Login", bg='#57a1f8',fg='white', border=0, 
                        activebackground='#57a1f8', activeforeground='white', cursor='hand2', width=50, command=login_user).place(x=75, y=204)
registerLabel = tk.Label(login_window, 
                    text="Don't have an account? Create one" , 
                    font=('Microsoft YaHei UI Light',10), bg='white', fg='black')
registerLabel.place(x=150, y=270)

loginButton = tk.Button(login_window,  text="Inregistreaza-te", bg='#57a1f8',fg='white', border = 0, 
                        activebackground='white', activeforeground='#57a1f8', command=register_page)
loginButton.place(x=210, y=300)


login_window.mainloop()


