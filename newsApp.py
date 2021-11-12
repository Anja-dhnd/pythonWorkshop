import requests
import tkinter as tk


def getNews():
    api_key = "f9ce68a95d4544c29eb19c07b2174f09"
    url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=" + api_key
    news = requests.get(url).json()


canvas = tk.Tk()
canvas.geometry("1200x900")
canvas.title("News App")

button = tk.Button(canvas, font=24, text="Reload", command=getNews)
button.pack(pady=20)

label = tk.Label(canvas, font=18, justify="left")
label.pack(pady=20)

canvas.mainloop()
