import tkinter as tk
window = tk.Tk()
window.title("My first GUI")
window.geometry("300x200")
mylabel = tk.Label(text = "hello")
mylabel.grid(column=0,row=0)
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=0)

def getInput():
    name = nameEntry.get()
    textArea = tk.Text(master=window, height=5, width=5)
    textArea.grid(column=1, row=6)
    answer = " Heyy {monkey}!!!. Yo years old!!! ".format(monkey=name)
    textArea.insert(tk.END, answer)


button_name = tk.Button(window, text = "some text", command=getInput)
button_name.grid(column=1,row=1)

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive' ]
credentials = ServiceAccountCredentials.from_json_keyfile_name('sheets.json', scope)
gc = gspread.authorize(credentials)
#sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/0B6_NUjnLLF6nVVFLMWRGSmhGd1U/edit#gid=287445570')
#worksheet = sheet.get_worksheet(0)
worksheet= gc.open('test').sheet1


out = list()
out = worksheet.col_values(1)
for temp in out:
    print(temp)

mylabel = tk.Label(text = out[0])
mylabel.grid(column=0,row=0)
window.mainloop()

from kivy.app import App

from kivy.uix.label import Label


class FirstKivy(App):

    def build(self):
        return Label(text="Hello Kivy!")


FirstKivy().run()
