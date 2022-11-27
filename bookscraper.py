from tkinter import *

root = Tk()
root.title("Bookscraping GUI by Abir Islam")
root.iconbitmap("/Users/abir/Documents/personal-projects/bookscraperGUI/book_icon.png")

# all elements on the GUI
message = Label(root, text="If you have any issues or want to provide feedback, please reach out").grid(row=0, column=0)
message2 = Label(root, text="You can view other projects on my website at https://abirislam.github.io/").grid(row=1, column=0)
spacer = Label(root, text=" ").grid(row=2, column=0)
searchBoxLabel = Label(root, text="Enter Book Title: ").grid(row=3, column=0)
searchBox = Entry(root, width=45)
searchBox.grid(row=4, column=0)

#TODO work on search function
def search():
    searchMsg = "Searching for " + searchBox.get()
    searchMsgLabel = Label(root, text=searchMsg)
    searchMsgLabel.grid(row=3, column=0)

searchButton = Button(root, text="Search", padx=5, pady=5, command=search, fg="darkgreen").grid(row=4, column=1)

root.mainloop()
