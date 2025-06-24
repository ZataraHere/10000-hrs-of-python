from tkinter import *
import requests

class NewsApp:

    def __init__(self):
        #load data 27efca9bdec548989375a08f2353e406
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=27efca9bdec548989375a08f2353e406').json()
        
        #gui
        self.gui()
        
        #load first story
        self.load_news_item(6)

    def gui(self):

        self.root = Tk()
        self.root.title('News Application')
        self.root.geometry('350x500')
        self.root.resizable(0,0)
        self.root.configure(background='white')


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):

        self.clear()

        headline = Label(self.root, text=self.data['articles'][index]['title'],bg = 'white', fg = 'black', wraplength=350, justify='center')
        headline.pack(pady=(10,20))
        headline.config(font=('verdana',16,'bold'))

        description = Label(self.root, text=self.data['articles'][index]['description'],bg = 'white', fg = 'black', wraplength=350, justify='center')
        description.pack(pady=(2,20))
        description.config(font=('verdana',15))

        frame = Frame(self.root, background='white')
        frame.pack(expand=True, fill=BOTH)

        prev = Button(frame, text= 'Prev', bg='black', fg = 'white', width=12, height=3)
        prev.pack(side=LEFT)
        prev.config(font=('verdana',10,'bold'))

        read = Button(frame, text= 'Read more', bg='black', fg = 'white', width=12, height=3)
        read.pack(side=LEFT)
        read.config(font=('verdana',10,'bold'))

        Next = Button(frame, text= 'Next', bg='black', fg = 'white', width=12, height=3)
        Next.pack(side=LEFT)
        Next.config(font=('verdana',10,'bold'))

        
        self.root.mainloop()

news = NewsApp()