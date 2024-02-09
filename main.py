from tkinter import *
from pytube import YouTube
import pyperclip

def copyPast():
    text = SaveEnteryToDownloadLInk()
    pyperclip.copy(text)
# Download Funtions to Download Video 
def Download_video():
    link = SaveEnteryToDownloadLInk()
    print(link)
    yt =YouTube(link).streams.first().download("./")
# Get Input Value 
def SaveEnteryToDownloadLInk():
    value = entry_field.get()
    return value

root = Tk()
root.configure(background="white")
root.geometry("400x300")
# Youtube Lable
youtubeLable = Label(root, text="YouTube Video Downloader", padx=30, pady=30, foreground="red",background="white")
youtubeLable.grid(column=3, row=1, columnspan=2)
# url lable
url_lable = Label(root, text="Enter URL : ", padx=10, foreground="red", pady=20,background="white")
url_lable.grid(column=1, row=2)
# Entery
entry_field = Entry(root, width=30)
entry_field.grid(column=2, row=2, columnspan=3)

# Quit Button
quit_button = Button(root, text="Quit", command=quit,padx=20)
quit_button.grid(column=2, row=3,columnspan=2)
# Download Button
download = Button(root, text="Download", command=Download_video)
download.grid(column=4, row=3,columnspan=4)

    
    # Mainloop
root.mainloop()




# displayFunction()


