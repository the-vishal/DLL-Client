import bs4 as bs
import urllib.request
import re
import urllib
import time
from tkinter import*
from tkinter import messagebox
import os
import subprocess


def location():
    newpath = r'C:/Users/Vishal/Downloads/DLL Files'
    if not os.path.exists(newpath):
        os.mkdir(newpath)


def goto_file():
    subprocess.Popen('explorer,"C:/Users/Vishal/Documents/DLL Files" ')


def fetch():
    global file
    file = e.get()
    if (len(file)>0):
     location()
     try:
        urllib.request.urlopen('https://www.google.com/')
     except (urllib.request.URLError):
        messagebox.showerror("Network Error","Please check Internet Connection")
    else:
        messagebox.showerror("Empty Field","File name field cannot be empty.")
    try:
      global sauce
      sauce = urllib.request.urlopen('https://www.dll-files.com/' + file + '.dll.html').read()
    except(urllib.request.HTTPError):
        messagebox.showerror("File not Found", "Sorry no with that name exist in Database.")


    soup = bs.BeautifulSoup(sauce, 'lxml')
    a = []


    for url in soup.find_all('a', ):
        a.append(url.get("href"))

    pattern = r"(download)/([\w\d]+)"

    k = []
    for i in a:
        find = re.findall(pattern, i)
        if find:
            print(i)
            k.append(i)



    p = urllib.request.URLopener()
    p.retrieve("https://www.dll-files.com" + k[0], 'C:/Users/Vishal/Downloads/DLL Files/'+file + ".dll")

    '''def loading():
        c = 0
        while c < 5:
            time.sleep(1)
            print("..")
            c += 1



    loading()'''
    messagebox.showinfo("Download Complete",
                        "File successfully downloaded to File location : /Downloads/DLL Files.")
    print("File Downloaded Successfully")



    # print(urls.text)
    # print(url)
    # browser.quit

client = Tk()
client.wm_title("DLL - Client")
client.config(background = "#9370db")
client.geometry('560x330')

f=Frame(client,height = 510, width = 600)
f.grid(row=0,column=0,padx=8,pady=5)

photo0=PhotoImage(file='CaptuJPG.gif')
lable = Label(f,image=photo0)
lable.grid(row=0,column=0,padx=10,pady=2)

photo2 = PhotoImage(file='Capt.gif')
lbl=Label(f,image=photo2)
lbl.grid(row=11,column=0,padx=1,pady=20)

e=Entry(f,width=80)
e.grid(row=1,column=0,padx=10,pady=2)
e.get()

photo=PhotoImage(file='ico.gif')
photo1=PhotoImage(file='Cap.gif')

but = Button(f,text='Download',image=photo1,command=fetch)
but.grid(row=10,column=0,padx=40,pady=2)

search =Button(f,image=photo,command=fetch)
search.grid(row=1,column=1,padx=10,pady=2)

intro=Label(f,text='Contact Info : mail007tovishal@gmail.com')
intro.grid(row=13,column=0,padx=10)


client.mainloop()

# ------------------------------------- Completed to requirement --------------------------------------------