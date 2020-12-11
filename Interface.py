from tkinter import * 


def expression(nombres):
  global operateur
  operateur = operateur + str(nombres)
  text_input.set(operateur)

def q():
  racine.destroy()

def delete():
  operateur = ""
  text_input.set("")





if __name__ == '__main__':
  racine = Tk()
  operateur = ""
  text_input = StringVar()


    #boutons numéraires

  bouton1 = Button(racine, text = " 1 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69", command = lambda:expression(1))          
  bouton1.grid(column = 0, row = 3) 

  bouton2 = Button(racine, text = " 2 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69", command = lambda:expression(2))          
  bouton2.grid(column = 1, row = 3) 

  bouton3 = Button(racine, text = " 3 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69", command = lambda:expression(3))
  bouton3.grid(column = 2, row = 3) 

  bouton4 = Button(racine, text = " 4 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69", command = lambda:expression(4))
  bouton4.grid(column = 0, row = 2) 

  bouton5 = Button(racine, text = " 5 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69", command = lambda:expression(5))
  bouton5.grid(column = 1, row = 2) 

  bouton6 = Button(racine, text = " 6 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69", command = lambda:expression(6)) 
  bouton6.grid(column = 2, row = 2) 

  bouton7 = Button(racine, text = " 7 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69", command = lambda:expression(7))
  bouton7.grid(column = 0, row = 1) 

  bouton8 = Button(racine, text = " 8 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69", command = lambda:expression(8))
  bouton8.grid(column = 1, row = 1) 

  bouton9 = Button(racine, text = " 9 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69", command = lambda:expression(9))
  bouton9.grid(column = 2, row = 1)

  ecran = Entry(racine, text = "Saisir...", width = 30, textvariable = text_input)
  ecran.grid(column =0, row = 0, columnspan = 5)

  bouton0 = Button(racine, text = " 0 ", activebackground = "black", height = 2, width = 4,
                   bg = "gray69", command = lambda:expression(0))
  bouton0.grid(column = 1, row = 4)

  blankbutton = Button(racine, text = "   ", state = 'disabled', height = 2, width = 4,
                       bg = "gray69")
  blankbutton.grid(column = 0, row = 4)

  virg = Button(racine, text = " . ", activebackground = "black", height = 2, width = 4,
                 bg = "gray69", command = lambda:expression("."))
  virg.grid(column = 2, row = 4)

  plus = Button(racine, text = " + ", activebackground = "gray90",
                height = 2, width = 4, bg = "gray50", command = lambda:expression("+"))
  plus.grid(column = 3, row = 1)

  minus = Button(racine, text = " - ", activebackground = "gray90",
                height = 2, width = 4, bg = "gray50", command = lambda:expression("-"))
  minus.grid(column = 3, row = 2)

  mul = Button(racine, text = " x ", activebackground = "gray90",
              height = 2, width = 4, bg = "gray50", command = lambda:expression("x"))
  mul.grid(column = 3, row = 3)

  div = Button(racine, text = " / ", activebackground = "gray90",
                     height = 2, width = 4, bg = "gray50", command = lambda:expression("/"))
  div.grid(column = 3, row = 4)
    
  equal = Button(racine, text = " = ", activebackground = "gray90", height = 1, width = 4,
                 bg = "gray50")
  equal.grid(column = 3, row = 5)

  supr = Button(racine, text = " C ", activebackground = "gray90", height = 2, width = 4,
                 bg = "gray50", command = delete)
  supr.grid(column = 4, row = 1)

  quitter = Button(racine, text = "quitter", command = q, height =1, width = 15)
  quitter.grid(column = 0, row = 5, columnspan = 3)


  racine.title( "Calculatrice") 
  racine.configure(bg = "gray10")
  racine.mainloop()
