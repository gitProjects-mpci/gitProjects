import tkinter as tk 

def q():
    racine.destroy()

if __name__ == '__main__':
    racine = tk.Tk()
#boutons numéraires
    bouton1 = tk.Button(racine, text = " 1 ", activebackground = "black",
                         height = 2, width = 4, bg = "gray69"          
                       )
    bouton1.grid(column = 0, row = 3) 

    bouton2 = tk.Button(racine, text = " 2 ", activebackground = "black",
                         height = 2, width = 4, bg = "gray69"          
                       )
    bouton2.grid(column = 1, row = 3) 

    bouton3 = tk.Button(racine, text = " 3 ", activebackground = "black",
                         height = 2, width = 4, bg = "gray69"          
                       )
    bouton3.grid(column = 2, row = 3) 

    bouton4 = tk.Button(racine, text = " 4 ", activebackground = "black",
                         height = 2, width = 4, bg = "gray69"          
                       )
    bouton4.grid(column = 0, row = 2) 

    bouton5 = tk.Button(racine, text = " 5 ", activebackground = "black",
                         height = 2, width = 4, bg = "gray69"          
                       )
    bouton5.grid(column = 1, row = 2) 

    bouton6 = tk.Button(racine, text = " 6 ", activebackground = "black",
                         height = 2, width = 4, bg = "gray69"          
                       ) 
    bouton6.grid(column = 2, row = 2) 

    bouton7 = tk.Button(racine, text = " 7 ", activebackground = "black",
                         height = 2, width = 4, bg = "gray69"          
                       )
    bouton7.grid(column = 0, row = 1) 

    bouton8 = tk.Button(racine, text = " 8 ", activebackground = "black",
                         height = 2, width = 4, bg = "gray69"          
                       )
    bouton8.grid(column = 1, row = 1) 

    bouton9 = tk.Button(racine, text = " 9 ", activebackground = "black",
                         height = 2, width = 4, bg = "gray69"          
                       )
    bouton9.grid(column = 2, row = 1)

    ecran = tk.Entry(racine, text = "Saisir...", width = 24)
    ecran.grid(column =0, row = 0, columnspan = 4)

    bouton0 = tk.Button(racine, text = " 0 ", activebackground = "black",
                         height = 2, width = 4, bg = "gray69"
                       )
    bouton0.grid(column = 1, row = 4)

    blankbutton = tk.Button(racine, text = "   ", state = 'disabled',
                             height = 2, width = 4, bg = "gray69"
                           )
    blankbutton.grid(column = 0, row = 4)

    virg = tk.Button(racine, text = " . ", activebackground = "black",
                      height = 2, width = 4, bg = "gray69"
                    )
    virg.grid(column = 2, row = 4)

#opérateurs

    plus = tk.Button(racine, text = " + ", activebackground = "gray90",
                      height = 2, width = 4, bg = "gray50"
                    )
    plus.grid(column = 3, row = 1)

    minus = tk.Button(racine, text = " - ", activebackground = "gray90",
                       height = 2, width = 4, bg = "gray50"
                     )
    minus.grid(column = 3, row = 2)

    mul = tk.Button(racine, text = " x ", activebackground = "gray90",
                     height = 2, width = 4, bg = "gray50"
                   )
    mul.grid(column = 3, row = 3)

    div = tk.Button(racine, text = " / ", activebackground = "gray90",
                     height = 2, width = 4, bg = "gray50"
                   )
    div.grid(column = 3, row = 4)
    
    equal = tk.Button(racine, text = " = ", activebackground = "gray90",
                       height = 1, width = 4, bg = "gray90"
                     )
    equal.grid(column = 3, row = 5)
    quitter = tk.Button(racine, text = "quitter", command = q, height =1, width = 15)
    quitter.grid(column = 0, row = 5, columnspan = 3)
   
    racine.configure(bg = "gray10")
    racine.title("Calculatrice")
    racine.mainloop()