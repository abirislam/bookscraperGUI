from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Bookscraping GUI by Abir Islam")
root.iconbitmap("bookscraperGUI/book_icon.png")

# all elements on the GUI
message = Label(root, text="If you have any issues or want to provide feedback, please reach out").grid(row=0, column=0)
message2 = Label(root, text="You can view other projects on my website at https://abirislam.github.io/").grid(row=1, column=0)
spacer = Label(root, text=" ").grid(row=2, column=0)
searchBoxLabel = Label(root, text="Enter Book Title: ").grid(row=3, column=0)
searchMsgLabel = Label(root, text=" ")
searchMsgLabel.grid(row=5, column=0)
searchBox = Entry(root, width=45)
searchBox.grid(row=4, column=0)

# Image stuff, replace of image of book cover later on! TODO
image = ImageTk.PhotoImage(Image.open("bookscraperGUI/books.png"))

#TODO work on search function
def search():
    searchMsg = "Searching for " + searchBox.get()
    searchMsgLabel.config(text=searchMsg)
    searchMsgLabel.grid(row=5, column=0)

def changeBookCover():
    #this will change the book cover, we will add this into search.
    return

searchButton = Button(root, text="Search", padx=5, pady=5, command=search, fg="darkgreen").grid(row=4, column=1)

root.mainloop()
