import requests:
 
URL = 'https://api.telegram.org/bot1169217703:AAFgak3bdsAsBDlr24U19WXt0vg_ifWgcbA'
# Don't forget to change the token key
 
def get_updates(url):
    response = requests.get(url+'getUpdates').json()
    return response['result']
 
 
data = get_updates(url)
 
print(data)
