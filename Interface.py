from tkinter import * 


def expression(nombres):
    global operateur
    operateur = operateur + str(nombres)
    text_input.set(operateur)

def egal():
    global operateur
    operateur = str(eval(operateur))
    text_input.set(operateur)
    operateur = ""

def q():
    racine.destroy()

def delete():
    global operateur 
    operateur = ""
    text_input.set(operateur)


if __name__ == '__main__':
    racine = Tk()
    operateur = ""
    text_input = StringVar()

#---------------------------------------------------------------------------------------------------------------------------------------
    #boutons numéraires
    bouton1 = Button(racine, text = " 1 ", activebackground = "black", height = 2, width = 4,bg = "gray69",
                    command = lambda:expression(1)).grid(column = 0, row = 3)
    bouton2 = Button(racine, text = " 2 ", activebackground = "black", height = 2, width = 4,bg = "gray69",
                    command = lambda:expression(2)).grid(column = 1, row = 3) 
    bouton3 = Button(racine, text = " 3 ", activebackground = "black", height = 2, width = 4,bg = "gray69",
                    command = lambda:expression(3)).grid(column = 2, row = 3) 
#---------------------------------------------------------------------------------------------------------------------------------------
    bouton4 = Button(racine, text = " 4 ", activebackground = "black", height = 2, width = 4,bg = "gray69",
                    command =lambda:expression(4)).grid(column = 0, row = 2)
    bouton5 = Button(racine, text = " 5 ", activebackground = "black", height = 2, width = 4,bg = "gray69",
                    command = lambda:expression(5)).grid(column = 1, row = 2) 
    bouton6 = Button(racine, text = " 6 ", activebackground = "black", height = 2, width = 4,bg = "gray69",
                    command = lambda:expression(6)).grid(column = 2, row = 2) 
#---------------------------------------------------------------------------------------------------------------------------------------
    bouton7 = Button(racine, text = " 7 ", activebackground = "black", height = 2, width = 4,bg = "gray69",
                    command = lambda:expression(7)).grid(column = 0, row = 1) 
    bouton8 = Button(racine, text = " 8 ", activebackground = "black", height = 2, width = 4,bg = "gray69",
                    command = lambda:expression(8)).grid(column = 1, row = 1) 
    bouton9 = Button(racine, text = " 9 ", activebackground = "black", height = 2, width = 4,bg = "gray69",
                    command = lambda:expression(9)).grid(column = 2, row = 1)
#---------------------------------------------------------------------------------------------------------------------------------------
    bouton0 = Button(racine, text = " 0 ", activebackground = "black", height = 2, width = 4,bg = "gray69",
                    command = lambda:expression(0)).grid(column = 1, row = 4)
    blankbutton = Button(racine, text = "   ", state = 'disabled', height = 2, width = 4,bg = "gray69").grid(column = 0, row = 4)


    #ecran
    ecran = Entry(racine, text = "Saisir...", width = 31, textvariable = text_input).grid(column =0, row = 0, columnspan = 5)

#---------------------------------------------------------------------------------------------------------------------------------------
    #opérateurs
    virg = Button(racine, text = " . ", activebackground = "black", height = 2, width = 4,bg = "gray69",
                    command = lambda:expression(".")).grid(column = 2, row = 4)
    plus = Button(racine, text = " + ", activebackground = "gray90",height = 2, width = 4, bg = "gray50",
                    command = lambda:expression("+")).grid(column = 3, row = 1)
    minus = Button(racine, text = " - ", activebackground = "gray90",height = 2, width = 4, bg = "gray50",
                    command = lambda:expression("-")).grid(column = 3, row = 2)
    mul = Button(racine, text = " * ", activebackground = "gray90",height = 2, width = 4, bg = "gray50",
                    command = lambda:expression("*")).grid(column = 3, row = 3)
    div = Button(racine, text = " / ", activebackground = "gray90",height = 2, width = 4, bg = "gray50",
                    command = lambda:expression("/")).grid(column = 3, row = 4)
    equal = Button(racine, text = " = ", activebackground = "gray90", height = 1, width = 4,bg = "gray50",
                    command = egal).grid(column = 3, row = 5)
    supr = Button(racine, text = " C ", activebackground = "gray90", height = 2, width = 4,bg = "gray50",
                    command = delete).grid(column = 4, row = 1)

    quitter = Button(racine, text = "quitter", command = q, height =1, width = 15).grid(column = 0, row = 5, columnspan = 3)
#---------------------------------------------------------------------------------------------------------------------------------------
    
    #boucle 
    racine.title( "Calculatrice") 
    racine.configure(bg = "gray10")
    racine.mainloop()