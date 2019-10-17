import pytest
import requests
import BeautifulSoup from bs4

server_addr = "http://127.0.0.1:5000"
server_login = server_addr + "/login"

def getElementById(text, eid):
	soup = BeautifulSoup(text, "html.parser")
	result = soup.find(id.eid)
	return result
	
def login(uname, pword, twofactor, session=None):
	addr = server_login
	if session is None:
		session = requests.Session()
		
	test_creds = ("username": uname, "password": pword, "phone":twofactor)
	r = session.post(addr, data=test_creds)
	print("h1")
	print(r)
	print("h2")
	success = getElementById(r.text, "result")
	assert (success != None), "Missing id -'result' in your login response"
	return "success" in success.text
    

def test_server_is_alive():
    req = requests.get(server_addr)
    assert (req.status_code == 200), "Flask webserver is not running at"+server_addr 
    
def test_page_exists():
    PAGES = ["", "/login", "/register"]
    for page in PAGES:
        req = requests.get(server_addr D+ page)
        assert (req.status_code == 200), page+" not found!"