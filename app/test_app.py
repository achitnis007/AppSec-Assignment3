import pytest
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError


server_addr = "http://127.0.0.1:5000"
server_login = server_addr + "/login"

def getElementById(text, eid):
	soup = BeautifulSoup(text, "lxml")
	result = soup.find(id.eid)
	return result
	
# def login(uname, pword, twofactor, session=None):
	# addr = server_login
	# if session is None:
		# session = requests.Session()
		
	# test_creds = ("username": uname, "password": pword, "phone":twofactor)
	# r = session.post(addr, data=test_creds)
	# print("h1")
	# print(r)
	# print("h2")
	# success = getElementById(r.text, "result")
	# assert (success != None), "Missing id -'result' in your login response"
	# return "success" in success.text
    

def test_server_is_alive():
    error = 1
    result = "Test Case #1: Test if Flask server is running\n"
    try:
        resp = requests.get(server_addr)
        resp.raise_for_status()
    except HTTPError as http_err:
        result = result + "HTTP error occurred\n"
    except Exception as err:
        result = result + "Other error occurred\n"
    else:
        error = 0
        result = "Success!!! - Server is running at: " + server_addr
    # assert error == 0, result
    return result

# def test_page_exists():
    # error = 0
    # result = "Test Case #2: Test if all pages can be accessed\n"
    # PAGES = ["", "/login", "/register"]
    # for page in PAGES:
        # try:
            # resp = requests.get(server_addr + page)
        # except Exception as err:
            # result = result + "Exception: Flask webserver is not running at: "+server_addr + "\n"
        # else:
           # result = result + 'Success!: ' + page + ' found'
    # assert error == 1, result