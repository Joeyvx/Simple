import requests, json

def gettoken():
    username = raw_input('Facebook username: ')
    password = raw_input('Facebook password: ')
    payload = {'u': username, 'p': password}
    get_token = requests.get('http://gymtranhuynh-winazure.rhcloud.com/token.php', params=payload).json()
    token = get_token['access_token']
    return token;

question = raw_input('Do you have token full privilege? (Y or N) ')

if question.upper() == 'Y':
    token = raw_input('Token: ')
    
else:
    token = gettoken()
    print 'Your token: '+token

print '---'
def imageupload():
	
	payload={
		'method': 'POST',
		'url' : 'https://www.facebook.com/images/fb_icon_325x325.png', #url to image
		'caption': 'Test api',
		'access_token': token
			}
	imapost = requests.post('https://graph.facebook.com/v2.10/me/photos' ,params=payload)
	imapost = imapost.text
	print imapost

imageupload()
	
