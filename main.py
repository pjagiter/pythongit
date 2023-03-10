# This is a sample Python script.
import webbrowser
import requests

#pageurl = 'https://github.com'
#date = 20150101
#small change
pageurl = input("podaj adres strony: ")
date = input("podaj date np. 20230130")
url = 'http://archive.org/wayback/available?url=' + pageurl + '&timestamp=' + str(date)
response = requests.get(url)
d = response.json()

page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

