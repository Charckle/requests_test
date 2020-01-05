import requests

username = "banana"
password = "banana123"

payload = {'user[username]': username, 'user[password]': password}
jar = requests.cookies.RequestsCookieJar()

r = requests.post('https://www.partis.si/user/login', params=payload, cookies=jar)

piskotki = r.history[0].cookies

r = requests.get('https://www.partis.si/prva', cookies=piskotki)

print(r.text)
