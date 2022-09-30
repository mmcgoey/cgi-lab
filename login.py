#!/usr/bin/env python3

# Note! My code is based off the code from the lab 3 videos on eclass from last year. I followed along with this video and used the same logic


import cgi
import cgitb
from http.cookies import SimpleCookie
cgitb.enable()
from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

storage = cgi.FieldStorage()
username = storage.getfirst("username")
password = storage.getfirst("password")

get_cookie = SimpleCookie(os.environ["HTTP_COOKIE"])

set_cookie_username = None
set_cookie_password = None

if get_cookie.get("username"):
    set_cookie_username = get_cookie.get("username").value
if get_cookie.get("password"):
    set_cookie_password = get_cookie.get("password").value


if set_cookie_username == secret.username and set_cookie_password == secret.password:
    username = set_cookie_username
    password = set_cookie_password

print("Content-Type: text/html")

if username == secret.username and password == secret.password and set_cookie_password == None and set_cookie_password ==None:
    print(f"Set-Cookie: password={password}")
    print(f"Set-Cookie: username={username}")



print()

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:

    print(secret_page(username,password))
else:
    print(after_login_incorrect())
    
