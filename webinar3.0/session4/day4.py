# gui
# dropdown
import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.geometry('500x500')

# tkvar = tk.StringVar(root)

# choices = {'pizza', 'burger', 'french fries'}
# tkvar.set('choose a dish')

# popMenu = tk.OptionMenu(root, tkvar, *choices)
# popMenu.pack()

# root.mainloop()


# message box

# response = tkm.askquestion("Teckat", "Do you like this course")
# print(response)

# if(response == 'yes'):
#     tkm.showinfo("Teckat", "Thank you for your support")

# else:
#     tkm.showinfo(
#         "teckat", "We will take your feedback as a postive response to improve our services")


# self adjusting widget

# labelx = tk.Label(root, bg="red")
# labelx.pack(fill=tk.X)

# labely = tk.Label(root, bg="blue")
# labely.pack(side=tk.LEFT, fill=tk.Y)

# root.mainloop()

# drawing on canvas

# create a canvas

canvas = tk.Canvas(root, height=300, width=300, bg="white")
canvas.pack()

canvas.create_line(100, 100, 200, 100)
canvas.create_line(200, 100, 200, 200)
canvas.create_line(200, 200, 100, 200)
canvas.create_line(100, 200, 100, 100)

root.mainloop()
