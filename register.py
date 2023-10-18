import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def register_user():
    if numeEntry.get()=='' or prenumeEntry.get()=='' or mailEntry.get()=='' or usernameEntry.get()=='' or parolaEntry.get()==''or parolaConfirmEntry.get()=='':
        messagebox.showerror('Eroare', 'Toate campurile trebuie completate!')
    elif parolaEntry.get() != parolaConfirmEntry.get():
        messagebox.showerror('Eroare', 'Parolele sunt diferite!')
    elif vrf.get()==0:
        messagebox.showerror('Eroare', 'Acceptati termenii si conditiile!')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root',password='bianca76')
            crs = con.cursor()
        except:
            messagebox.showerror('Eroare', 'Eroare de conectare la baza de date! Incearca din nou')
            return

        crs.execute('use appstatistic')

        query = 'select * from user where username = %s'
        crs.execute(query, (usernameEntry.get()))

        same = crs.fetchone()
        if same != None :
            messagebox.showerror('Eroare', 'Utilizatorul cu acest username exista deja!')
        else:
            query = 'insert into user(nume, prenume, username, email, parola) values (%s,%s,%s,%s,%s)'
            crs.execute(query,(numeEntry.get(), prenumeEntry.get(), usernameEntry.get(), 
                        mailEntry.get(), parolaEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Inregistrare cu succes', 'Inregistrarea a fost realizata cu succes')
            login_page()

def login_page():
    register_window.destroy()
    import login

register_window = Tk()
register_window.title('Register')
register_window.geometry('925x500+300+200')
register_window.configure(bg = "#fff")
register_window.resizable(0,0) 

img = Image.open("mobilelog.jpg")
imgR = img.resize((400,400), Image.ANTIALIAS)
imag = ImageTk.PhotoImage(imgR)
lbImg = tk.Label(register_window, image = imag).place(x = 450, y = 60)

frame = Frame(register_window, width=50, height=20, bg ='white')
frame.place(x = 90, y = 5)

head = tk.Label(frame, text='CREAZĂ PROPRIUL CONT', font=('Microsoft YaHei UI Light', 17, 'bold'), bg='white', fg='#57a1f8')
head.grid(row=0, column=0, pady=20)

numeLabel = Label(frame, text = 'Nume', font=('Microsoft YaHei UI Light', 10, 'bold'),bg='white', fg='#57a1f8')
numeLabel.grid(row=1, column=0, sticky="w", padx=45)
numeEntry = Entry(frame, width = 25, font=('Microsoft YaHei UI Light', 10, 'bold'),bg='#57a1f8', fg='white')
numeEntry.grid(row=2, column=0, sticky="w", padx=45)

prenumeLabel = Label(frame, text = 'Prenume', font=('Microsoft YaHei UI Light', 10, 'bold'),bg='white', fg='#57a1f8')
prenumeLabel.grid(row=3, column=0, sticky="w", padx=45)
prenumeEntry = Entry(frame, width = 25, font=('Microsoft YaHei UI Light', 10, 'bold'),bg='#57a1f8', fg='white')
prenumeEntry.grid(row=4, column=0, sticky="w", padx=45)

usernameLabel = Label(frame, text = 'Username', font=('Microsoft YaHei UI Light', 10, 'bold'),bg='white', fg='#57a1f8')
usernameLabel.grid(row=5, column=0, sticky="w", padx=45)
usernameEntry = Entry(frame, width = 25, font=('Microsoft YaHei UI Light', 10, 'bold'),bg='#57a1f8', fg='white')
usernameEntry.grid(row=6, column=0, sticky="w", padx=45)

mailLabel = Label(frame, text = 'E-mail', font=('Microsoft YaHei UI Light', 10, 'bold'),bg='white', fg='#57a1f8')
mailLabel.grid(row=7, column=0, sticky="w", padx=45)
mailEntry = Entry(frame, width = 25, font=('Microsoft YaHei UI Light', 10, 'bold'),bg='#57a1f8', fg='white')
mailEntry.grid(row=8, column=0, sticky="w", padx=45)

parolaLabel = Label(frame, text = 'Parola', font=('Microsoft YaHei UI Light', 10, 'bold'),bg='white', fg='#57a1f8')
parolaLabel.grid(row=9, column=0, sticky="w", padx=45)
parolaEntry = Entry(frame, width = 25, font=('Microsoft YaHei UI Light', 10, 'bold'),bg='#57a1f8', fg='white')
parolaEntry.grid(row=10, column=0, sticky="w", padx=45)

parolaConfirmLabel = Label(frame, text = 'Confirmare Parola', font=('Microsoft YaHei UI Light', 10, 'bold'),bg='white', fg='#57a1f8')
parolaConfirmLabel.grid(row=11, column=0, sticky="w",padx=45)
parolaConfirmEntry = Entry(frame, width = 25, font=('Microsoft YaHei UI Light', 10, 'bold'),bg='#57a1f8', fg='white')
parolaConfirmEntry.grid(row=12, column=0, sticky="w", padx=45)

vrf = IntVar()
term = Checkbutton(frame, text = 'Sunt de acord cu termenii si conditiile', font=('Microsoft YaHei UI Light', 10, 'bold'),
                    bg='white', fg='#57a1f8', activebackground='white', activeforeground='#57a1f8', cursor='hand2', variable=vrf)
term.grid(row=13, column=0, pady=10)

reg_button = tk.Button(frame, width=17, text="Inregistrare", font=('Microsoft YaHei UI Light', 13, 'bold'),bg='#57a1f8',fg='white', border = 0, 
                        activebackground='#57a1f8', activeforeground='white', command=register_user)
reg_button.grid(row= 14, column= 0 )

log_button = tk.Button(frame, text="Inapoi la login", bg='#57a1f8',fg='white', border = 0, 
                        activebackground='#57a1f8', activeforeground='white', command=login_page)
log_button.grid(row= 15, column= 0, pady=5)

register_window.mainloop()