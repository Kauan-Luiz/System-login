from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#criando a janela 

window = Tk()
window.title("System - Login") #Titulo da janela 
window.geometry("600x300") #Tamanho da janela
window.resizable(width=False, height=False) #Se pode mexer no tamanho da janela 
window.iconbitmap(default="login/logoicon.ico")

#=============imagens==========
logo = PhotoImage (file="login/logo.png")



leftframe = Frame(window, width=195, height=300, bg="#A9A9A9") 
leftframe.pack(side=LEFT)

rightframe = Frame(window, width=400, height=300, bg="#E0FFFF")
rightframe.pack(side=RIGHT)

logoLabel = Label(leftframe, image=logo, bg="#A9A9A9")
logoLabel.place(x=50, y=100)

userLabel = Label(rightframe, text="Usuario:", bg="#E0FFFF", fg="Black")
userLabel.place(x=40, y=100)

passLabel = Label(rightframe, text="Senha:", bg="#E0FFFF", fg="Black")
passLabel.place (x=40, y=150)

userEntry = ttk.Entry(rightframe, width=30)
userEntry.place(x=120, y=100)

passEntry = ttk.Entry(rightframe, width=30, show="●")
passEntry.place(x=120, y=150)

def login ():
    user = userEntry.get()
    password = passEntry.get()
        
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Passoword = ?)                             
    """,(user, password))
    
    verifylogin = DataBaser.cursor.fetchone()
    try:
        if (user in verifylogin and password in verifylogin):
            messagebox.showinfo(title="Login info", message="Seja Bem-vindo!")
    except:
        messagebox.showerror(title="Login info", message="Usuario ou senha incorreta!")
#button
loginButton = ttk.Button(rightframe, text="Login", width=20, command=login)
loginButton.place(x=60, y=215)


def register():
    #removendo widgets de login   
    loginButton.place(x=601)
    registerButton.place(x=601) 
    #inserindo widgets de registro
    nameLabel = Label(rightframe, text="Nome", bg="#E0FFFF", fg="Black")
    nameLabel.place(x=40, y=50)
    
    nameEntry = ttk.Entry(rightframe, width=30)
    nameEntry.place(x=120, y=50)
    
    emailLabel = Label(rightframe, text="Email", bg="#E0FFFF", fg="Black")
    emailLabel.place(x=40, y=200)
    
    emailEntry = ttk.Entry(rightframe, width=30)
    emailEntry.place(x=120, y=200)
    
    def registerToDatabase():
        name = nameEntry.get()
        email = emailEntry.get()
        user = userEntry.get()
        password = passEntry.get()
        
        if (name == "" and email == "" and user == "" and password == ""):
            messagebox.showerror(title="Erro de Registro", message="Preencha todos os campos.")            
        else:     
            DataBaser.cursor.execute("""
            INSERT INTO users(Name, Email, User, Passoword) VALUES(?, ?, ?, ?)                         
            """, (name, email, user, password))
            DataBaser.conn.commit()
            messagebox.showinfo(title="informações de registro", message="Registrado com sucesso!")
    
    register = ttk.Button(rightframe, text="Registrar-se", width=15, command=registerToDatabase)
    register.place(x=220, y=250)
    
    def backToLogin():
        nameLabel.place(x=601)
        nameEntry.place(x=601)
        emailLabel.place(x=601)
        emailEntry.place(x=601)
        register.place(x=601)
        back.place(x=601)
        
        loginButton.place(x=60, y=215)
        registerButton.place(x=200, y=215)
        
        
        
    back = ttk.Button(rightframe, text="Voltar", width=15, command=backToLogin)
    back.place(x=100, y=250)
    
    
        
           

registerButton = ttk.Button(rightframe, text="Registro", width=20, command=register)
registerButton.place(x=200, y=215)



window.mainloop()


