import tkinter as tk

# create window

# root = tk.Tk()

# root.mainloop()


# creating label


#  create a window
# root = tk.Tk()
# root.title('test')

# l = tk.Label(root, text="Hello World")
# l.pack()


# l = tk.Label(root, text="Hello World")
# l.pack()


# l = tk.Label(root, text="Hello World")
# l.pack()


# l = tk.Label(root, text="Hello World")
# l.pack()


# root.mainloop()


# grid system

# root = tk.Tk()
# root.geometry('1200x700')

# n = tk.Label(root, text="Name :")
# n.grid(row=0, column=0)

# c = tk.Label(root, text="Class :")
# c.grid(row=1, column=0)

# tk.Label(root, text="age :").grid(row=2, column=0)

# ne = tk.Entry(root)
# ne.grid(row=0, column=1)

# ce = tk.Entry(root)
# ce.grid(row=1, column=1, ipady=20)

# root.mainloop()


# frames

# root = tk.Tk()
# root.geometry('500x500')
# frame1 = tk.Frame(root)
# frame1.pack()

# frame2 = tk.Frame(root)
# frame2.pack(side=tk.BOTTOM)

# l1 = tk.Label(frame1, text="frame1", fg="Red", bg='Yellow')
# l1.pack()

# l2 = tk.Label(frame2, text="frame2")
# l2.pack()

# root.mainloop()


# buttons

# root = tk.Tk()
# root.geometry('500x500')

# b = tk.Button(root, text='click here', bg='#ea405a', fg="white")
# b.pack()

# root.mainloop()


# button click

# root = tk.Tk()

# root.geometry('500x500')

# l = tk.Label(root, text='click button to change')
# l.pack()

# c = 0


# def onClick():
#     global c
#     c = c+1
#     st = "button clicked "+str(c)
#     l['fg'] = "blue"


# b = tk.Button(root, text="click here", command=onClick)
# b.pack()

# root.mainloop()

# entry get on button click

root = tk.Tk()
root.geometry('500x500')


def textentry():
    d = l.get()
    print(d)
    label['text'] = d


l = tk.Entry(root)
l.pack()
tk.Button(root, text='enter text', command=textentry).pack()

label = tk.Label(root)
label.pack()

root.mainloop()
