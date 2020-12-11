from tkinter import * 

def expressions(nombres):
    global operateur
    operateur = operateur + str(nombres)
    text_input.set(operateur)

def q():
    racine.destroy()

if __name__ == '__main__':
  racine = Tk()
  operateur = ""
  text_input = StringVar()


    #boutons numéraires
  bouton1 = Button(racine, text = " 1 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69")          
  bouton1.grid(column = 0, row = 3) 

  bouton2 = Button(racine, text = " 2 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69")          
  bouton2.grid(column = 1, row = 3) 

  bouton3 = Button(racine, text = " 3 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69")
  bouton3.grid(column = 2, row = 3) 

  bouton4 = Button(racine, text = " 4 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69")
  bouton4.grid(column = 0, row = 2) 

  bouton5 = Button(racine, text = " 5 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69")
  bouton5.grid(column = 1, row = 2) 

  bouton6 = Button(racine, text = " 6 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69") 
  bouton6.grid(column = 2, row = 2) 

  bouton7 = Button(racine, text = " 7 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69")
  bouton7.grid(column = 0, row = 1) 

  bouton8 = Button(racine, text = " 8 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69")
  bouton8.grid(column = 1, row = 1) 

  bouton9 = Button(racine, text = " 9 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69")
  bouton9.grid(column = 2, row = 1)

  ecran = Entry(racine, text = "Saisir...", width = 25, textvariable = text_input)
  ecran.grid(column =0, row = 0, columnspan = 4)

  bouton0 = Button(racine, text = " 0 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69")
  bouton0.grid(column = 1, row = 4)

  blankbutton = Button(racine, text = "   ", state = 'disabled', height = 2, width = 4,
                       bg = "gray69")
  blankbutton.grid(column = 0, row = 4)

  virg = Button(racine, text = " . ", activebackground = "black", height = 2, width = 4,
                 bg = "gray69")
  virg.grid(column = 2, row = 4)

  plus = Button(racine, text = " + ", activebackground = "gray90",
                height = 2, width = 4, bg = "gray50")
  plus.grid(column = 3, row = 1)

  minus = Button(racine, text = " - ", activebackground = "gray90",
                height = 2, width = 4, bg = "gray50")
  minus.grid(column = 3, row = 2)

  mul = Button(racine, text = " x ", activebackground = "gray90",
              height = 2, width = 4, bg = "gray50")
  mul.grid(column = 3, row = 3)

  div = Button(racine, text = " / ", activebackground = "gray90",
                     height = 2, width = 4, bg = "gray50")
  div.grid(column = 3, row = 4)
    
  equal = Button(racine, text = " = ", activebackground = "gray90", height = 1, width = 4,
                 bg = "gray50")
  equal.grid(column = 3, row = 5)

  quitter = Button(racine, text = "quitter", command = q, height =1, width = 15)
  quitter.grid(column = 0, row = 5, columnspan = 3)
   
  racine.configure(bg = "gray10")
  racine.mainloop()
