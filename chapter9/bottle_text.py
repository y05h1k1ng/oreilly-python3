import requests

resp = requests.get('http://localhost:9999/echo/yoshiking')

if resp.status_code == 200 and resp.text == 'Say hello to my little friend: yoshiking':
    print('It worked! That almost never happens!')
else:
    print('Argh, got this:', resp.text)