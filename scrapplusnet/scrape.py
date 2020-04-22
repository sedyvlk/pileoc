import hashlib
import mechanize
import requests
br = mechanize.Browser()
page = 'http://192.168.1.254/index.cgi?active%5fpage=9143&active%5fpage%5fstr=page%5fhdesk&req%5fmode=1&mimic%5fbutton%5ffield=submit%5fbutton%5flogin%5fsubmit%3a+%2e%2e&request%5fid=231653539&button%5fvalue='
page = 'http://192.168.1.254/index.cgi?active_page=9143'
br.open(page)
print(br.cookiejar.cookies_for_request())
#br.select_form("form1")
br.select_form("form_contents")
br.set_all_readonly(False)
for control in br.form.controls:
    print(control)
    if control.name.startswith('password_'):
        password_field = control.name
    if control.name == 'auth_key':
        auth_key = control.value
        #control.value = 'H3FPJK6F'
        #print("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))

print(password_field, auth_key)
password = 'H3FPJK6F' + auth_key
p = hashlib.md5(password.encode()).hexdigest()
br['md5_pass'] = p
print(password, p)
#response = br.submit()
#print(response.read())
tok = br['post_token']
print('xxx')
r = requests.post('http://192.168.1.254/index.cgi', data={'md5_pass': p,'active_page': 9143, 'post_token':br['post_token']},cookies={'rg_cookie_session_id':'05db9051443632fb4185840f03c6b71d'})
print(r.content)