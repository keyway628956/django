from urllib.request import urlopen

url = "https://www.google.com/doodles/json/2020/7?hl=zh_TW"

response = urlopen(url)
print(response.read())
