from tkinter import *
from methods import get_input
import requests
import json
root = Tk()
def get():
    inp = search_material.get()
    print(inp)
    url = f"https://newsapi.org/v2/everything?q={inp}&from=2022-02-21&sortBy=popularity&apiKey=fb358baaf0a349cea5135ebf84961e87"
    print(url)
    response_api = requests.get(url)
    data = response_api.text
    parse_json = json.loads(data)   

search_material = StringVar()
root.geometry("500x500")
root.resizable(False,False)
root.title("News")
search = Entry(root,textvariable=search_material,font=("default",20),width=19)
search.place(x=200,y=45)
l1 = Label(root,text="News",font=("default",20))
l1.pack()
l2 = Label(root,text="Enter the topic you want to search:",font=("default",9))
l2.place(x=0,y=50)
root.bind('<Return>',lambda event:get())

root.mainloop()
