import requests, json

def gettoken():
    username = raw_input('Nhap username fb: ')
    password = raw_input('Nhap password fb: ')
    payload = {'u': username, 'p': password}
    get_token = requests.get('http://gymtranhuynh-winazure.rhcloud.com/token.php', params=payload).json()
    token = get_token['access_token']
    return token;

question = raw_input('Ban da co token full quyen chua (Y or N) ')

if question.upper() == 'Y':
    token = raw_input('Nhap token: ')
    
else:
    token = gettoken()
    print 'Token cua ban la: '+token

print '---'
def imageupload():
	
	payload={
		'method': 'POST',
		'url' : 'https://www.facebook.com/images/fb_icon_325x325.png',
		'caption': 'Test api',
		'access_token': token
			}
	imapost = requests.post('https://graph.facebook.com/v2.10/me/photos' ,params=payload)
	imapost = imapost.text
	print imapost

imageupload()
	
