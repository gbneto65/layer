
import tkinter as tk
from PIL import ImageTk, Image

screen_x = int(800)
screen_y = int(600)
genetic_list = ['Hyline-W36', 'Hyline-Brown', 'other']
genetic_listbox_x1 = screen_x*.15
genetic_listbox_y1 = screen_y * .07

screen = tk.Tk()
screen.minsize(screen_x, screen_y)
screen.iconbitmap('layer_egg.ico')
screen.title("Layers Economics Evaluator")

lbl_descrip = tk.Label(screen,
                    text='Data Input - Layer A',
                    fg="gray",
                    font=(None, 12)
                       )
lbl_descrip.place(x=screen_x / 4 - 50,
                  y=screen_y * .02
                  )

lbl_descrip = tk.Label(screen,
                  text='Data Input - Layer B',
                  fg="gray",
                  font=(None, 12),
                       )
lbl_descrip.place(x=screen_x / 1.4 - 50,
                  y=screen_y * .02
                  )

""" list box from genetic"""
genetic_listbox = tk.Listbox(screen,
                             height=3,
                             selectmode = 'SINGLE',
                             bg = 'white',
                             yscrollcommand = True,
                             )
for item in genetic_list :
    genetic_listbox.insert(tk.END, item)

genetic_listbox.place(x=genetic_listbox_x1,
                      y=genetic_listbox_y1
                      )

a = genetic_listbox.get(tk.ANCHOR)
print(a)

#img = ImageTk.PhotoImage(Image.open('layer_egg.png'))
#panel = Label(screen, image=img)
#panel.place(x=screen_x - 100, y=screen_y * .03)

screen.eval('tk::PlaceWindow . center')


screen.mainloop()

