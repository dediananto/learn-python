import requests

hasil = requests.get('https://digitalskola.com')

print(hasil.status_code)
# print(hasil.text)