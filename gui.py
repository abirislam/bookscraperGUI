from tkinter import *

root = Tk()


# all elements on the GUI
title = Label(root, text="Welcome to the Bookscraping GUI by Abir Islam").grid(row=0, column=0)
message = Label(root, text="If you have any issues or want to provide feedback, please reach out").grid(row=1, column=0)
message2 = Label(root, text="You can view other projects on my website at https://abirislam.github.io").grid(row=2, column=0)
searchBox = Entry(root).grid(row=3, column=0)

#TODO work on search function
def search():
    fooledya = Label(root, text="Sorry this feature is not implemented yet!")
    fooledya.grid(row=4, column=0)


searchButton = Button(root, text="Search", padx=5, pady=5, command=search, fg="darkgreen").grid(row=3, column=1)

root.mainloop()
