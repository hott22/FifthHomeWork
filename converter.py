import requests
from tkinter import *

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
win = Tk()
win.title("Курс валют")
win.config(bg='red')
win.geometry('400x400+700+100')
label_1 = Label(win, text='Доллар США',
                        bg = 'blue', # цвет фона
                        fg = 'black', # цвет шрифта
                        font = ('Arial', 10, 'bold'), # тип шрифта
                        padx = 40, # Отступы по X
                        pady = 10
                        )
label_1.place(x=10, y=20)
label_2 = Label(win, text=data['Valute']['USD']['Value'], bg = 'black', fg = 'blue', font = ('Arial', 10, 'bold'),
                    padx = 40, pady = 10)
label_2.place(x=200, y=20)
label_3 = Label(win, text = 'Евро', bg = 'yellow', fg = 'green', font = ('Arial', 10, 'bold'), padx = 40, pady = 10)
label_3.place(x = 10, y = 100)
label_4 = Label(win, text=data['Valute']['EUR']['Value'], bg = 'magenta', fg = 'cyan', font = ('Arial', 10, 'bold'),
                    padx = 40, pady = 10)
label_4.place(x = 200, y = 100)
win.mainloop()