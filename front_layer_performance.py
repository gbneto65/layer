
from tkinter import *
#from tkinter import ttk
from PIL import ImageTk, Image

screen_x = int(800)
screen_y = int(600)

genetic_listbox_x1 = screen_x*.15
genetic_listbox_y1 = screen_y * .07

screen = Tk()

screen.minsize(screen_x, screen_y)
screen.iconbitmap('layer_egg.ico')
screen.title("Layers Economics Evaluator")

lbl_descrip = Label(screen,
                    text='Data Input - Layer A',
                    fg="gray",
                    font=(None, 12)
                       )
lbl_descrip.place(x=screen_x / 4 - 50,
                  y=screen_y * .02
                  )

lbl_descrip = Label(screen,
                  text='Data Input - Layer B',
                  fg="gray",
                  font=(None, 12),
                       )
lbl_descrip.place(x=screen_x / 1.4 - 50,
                  y=screen_y * .02
                  )

""" OptionMenu for genetic selection"""
def genetic_selection(event) :
    myLabel = Label(screen, text=select_genetic_option.get()).pack()
    print(myLabel)
    if select_genetic_option.get() == 'W36' :
       print('white eggs')


genetic_options = ['W36', 'brown', "other"]
select_genetic_option = StringVar()
select_genetic_option.set(genetic_options[0])
drop = OptionMenu(screen, select_genetic_option, *genetic_options, command=genetic_selection)
drop.pack()



#img = ImageTk.PhotoImage(Image.open('layer_egg.png'))
#panel = Label(screen, image=img)
#panel.place(x=screen_x - 100, y=screen_y * .03)

screen.eval('tk::PlaceWindow . center')


screen.mainloop()

