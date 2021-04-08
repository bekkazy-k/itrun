import requests
r = requests.get('https://github.com/bekkazy-k/itrun/tree/Daniiar')
print(r.status_code)
print(r.text)