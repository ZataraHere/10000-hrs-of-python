from tkinter import *
import requests
from urllib.request import urlopen
from PIL import Image, ImageTk
import io
import webbrowser


class NewsApp:

    def __init__(self):
        #load data 27efca9bdec548989375a08f2353e406
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=27efca9bdec548989375a08f2353e406').json()
        
        #gui
        self.gui()
        
        #load first story
        self.load_news_item(0)

    def gui(self):

        self.root = Tk()
        self.root.title('News Application')
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.configure(background='white')


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):

        self.clear()

        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            img = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(img)

        except:
            img_url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.Ib2hnkro8GuHpCODmCS3-gHaKf%26pid%3DApi&f=1&ipt=5fdb415b4b61b112f9b2a5c023f9fd9e43e3a76fceb0292c9193e6a1239f73f5&ipo=images"
            raw_data = urlopen(img_url).read()
            img = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(img)

        
        image_label = Label(self.root, image=photo)
        image_label.pack()

        headline = Label(self.root, text=self.data['articles'][index]['title'],bg = 'white', fg = 'black', wraplength=350, justify='center')
        headline.pack(pady=(10,20))
        headline.config(font=('verdana',16,'bold'))

        description = Label(self.root, text=self.data['articles'][index]['description'],bg = 'white', fg = 'black', wraplength=350, justify='center')
        description.pack(pady=(2,20))
        description.config(font=('verdana',15))

        frame = Frame(self.root, background='white')
        frame.pack(expand=True, fill=BOTH, side=BOTTOM, pady=10)

        if index != 0:

            prev = Button(frame, text= 'Prev', bg='black', fg = 'white', width=12, height=3, command= lambda:self.load_news_item(index-1))
            prev.pack(side=LEFT)
            prev.config(font=('verdana',10,'bold'))

        read = Button(frame, text= 'Read more', bg='black', fg = 'white', width=12, height=3, command=lambda:self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)
        read.config(font=('verdana',10,'bold'))

        if index != len(self.data['articles']) -1:

            Next = Button(frame, text= 'Next', bg='black', fg = 'white', width=12, height=3,command= lambda:self.load_news_item(index+1))
            Next.pack(side=LEFT)
            Next.config(font=('verdana',10,'bold'))

        
        self.root.mainloop()

    def open_link(self, url):
        webbrowser.open(url)

news = NewsApp()