from bs4 import BeautifulSoup
from tkinter import *
import threading
import time
import requests


def update():
    while True:
        try:
            url = "https://countrymeters.info/ru/World"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            result = soup.find_all("td", class_="counter")
            result = str(result[0])
            lbl.configure(text=result[34:47])
            time.sleep(1)
        except:
            pass
def main():
    trd1 = threading.Thread(target=update)
    trd1.start()
    time.sleep(1)
    trd2 = threading.Thread(target=update)
    trd2.start()
    time.sleep(1)
    trd3 = threading.Thread(target=update)
    trd3.start()
    time.sleep(1)
    trd4 = threading.Thread(target=update)
    trd4.start()
    time.sleep(1)
    trd5 = threading.Thread(target=update)
    trd5.start()
    time.sleep(1)
    trd6 = threading.Thread(target=update)
    trd6.start()
   
window = Tk()
window.title("Waiting 8 Billions")
window.geometry("300x100")
lbl = Label(window, text="Let's count people!")
lbl.place(relx=0.35, rely=0.27)
btn = Button(window, text="Start!", command=main)
btn.place(relx=0.4, rely=0.47)
window.mainloop()
