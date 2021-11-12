import requests
import tkinter as tk


def getNews():
    api_key = "f9ce68a95d4544c29eb19c07b2174f09"
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=" + api_key
    news = requests.get(url).json()

    articles = news["articles"]
    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + str(i + 1) + "." + my_articles[i] + "\n"

    label.config(text=my_news)


canvas = tk.Tk()
canvas.geometry("1200x900")
canvas.configure(bg="#ffffff")
canvas.title("News App")

button = tk.Button(canvas, font=24, text="Reload", command=getNews)
button.pack(pady=20)

label = tk.Label(canvas, font=18, justify="left")
label.pack(pady=20)

getNews()

canvas.mainloop()
