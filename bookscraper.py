from tkinter import *
from bs4 import BeautifulSoup
import requests
import webbrowser

root = Tk()

root.title("Bookscraping GUI by Abir Islam")
root.iconbitmap("bookscraperGUI/book_icon.png")

# Framing
frame = LabelFrame(root, text="Search here", padx=5, pady=5)
frame.grid(row=3, column=0)

# all elements on the GUI
message = Label(root, text="If you have any issues or want to provide feedback, please reach out").grid(row=0, column=0)
message2 = Label(root, text="You can view other projects on my website at https://abirislam.github.io/").grid(row=1, column=0)
spacer = Label(root, text=" ").grid(row=2, column=0)
searchBoxLabel = Label(frame, text="Enter Book Title: ").grid(row=3, column=0)
searchMsgLabel = Label(frame, text=" ")
searchMsgLabel.grid(row=5, column=0)
searchBox = Entry(frame, width=45)
searchBox.grid(row=4, column=0)

def callback(url):
    webbrowser.open_new(url)

def search():
    searchMsg = "Searching for " + searchBox.get() +"..."
    searchMsgLabel.config(text=searchMsg)
    searchMsgLabel.grid(row=5, column=0)

    string_concat = "https://libgen.is/search.php?req=" + searchBox.get() + "&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
    html_text = requests.get(string_concat).text

    soup = BeautifulSoup(html_text, 'lxml')
    links = soup.find_all('a', title="this mirror", limit=5)
    counter = 1

    for link in links:
        link_href = link["href"]
        herewego = str(counter) + ". " + link_href
        result = Label(frame, text=herewego)
        result.grid(row=5 + counter, column=0)
        result.bind("<Button-1>", lambda e: callback(link_href))
        print(herewego)
        counter += 1

    # print(links["href"])
    # results.config(text=links["href"])


searchButton = Button(frame, text="Search", padx=5, pady=5, command=search, fg="darkgreen").grid(row=4, column=1)

root.mainloop()
