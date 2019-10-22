import pytest
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import mechanize
import http.cookiejar
import time
import random

# ===== some globals used in this pytest suite to make things easier =========

server_addr = "http://127.0.0.1:5000"
login_url = server_addr + "/login"
register_url = server_addr + "/register"
spellcheck_url = server_addr + "/spell_check"
logout_url = server_addr + "/logout"

user_name = 'user_' + str(random.randint(1,100000))

# == some helper functions used in this pytest suite to make things easier ==

def getElementById(text, eid):
	soup = BeautifulSoup(text, "lxml")
	result = soup.find(id.eid)
	return result

# ==========================================================================	
def register(user, pwd, two_fa):

    br = mechanize.Browser()
    br.set_debug_http(False)
    br.set_handle_refresh(False)
    br.set_handle_robots(False)

    cj = http.cookiejar.CookieJar()
    br.set_cookiejar(cj)

    br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'),
                     ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                     ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),
                     ('Accept-Language', 'en-US,en;q=0.8,fr;q=0.6'),
                     ('Connection', 'keep-alive')
                    ]
    response = br.open(register_url)                
    if response.code != 200:
        return 'failure'

    br.select_form(nr = 0)
    br.form['username'] = user
    br.form['password'] = pwd
    br.form['phone'] = two_fa
    resp = br.submit()
    if resp.code != 200:
        return 'failure'
    
    resp = resp.read().decode('UTF-8')
    soup = BeautifulSoup(resp, 'lxml')
    result = soup.find(id='success').text
    
    br.close()
    return result

# ==========================================================================	
def login(user, pwd, two_fa):

    br = mechanize.Browser()
    br.set_debug_http(False)
    br.set_handle_refresh(False)
    br.set_handle_robots(False)

    cj = http.cookiejar.CookieJar()
    br.set_cookiejar(cj)

    br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'),
                     ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                     ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),
                     ('Accept-Language', 'en-US,en;q=0.8,fr;q=0.6'),
                     ('Connection', 'keep-alive')
                    ]
    response = br.open(login_url)                
    if response.code != 200:
        return 'failure'

    soup = BeautifulSoup(response.read().decode('UTF-8'), 'lxml')
    # print(soup.prettify())

    br.select_form(nr = 0)
    br.form['username'] = user
    br.form['password'] = pwd
    br.form['phone'] = two_fa
    resp = br.submit()
    if resp.code != 200:
        return 'failure'
    
    resp = resp.read().decode('UTF-8')
    soup = BeautifulSoup(resp, 'lxml')
    # print(soup.prettify())
    result = soup.find(id='result').text

    br.close()    
    return result

# ==========================================================================
def spellcheck(user, pwd, two_fa, words_to_check):

    br = mechanize.Browser()
    br.set_debug_http(False)
    br.set_handle_refresh(False)
    br.set_handle_robots(False)

    cj = http.cookiejar.CookieJar()
    br.set_cookiejar(cj)

    br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'),
                     ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                     ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),
                     ('Accept-Language', 'en-US,en;q=0.8,fr;q=0.6'),
                     ('Connection', 'keep-alive')
                    ]
    response = br.open(login_url)                
    if response.code != 200:
        return 'failure'

    soup = BeautifulSoup(response.read().decode('UTF-8'), 'lxml')
    # print(soup.prettify())

    br.select_form(nr = 0)
    br.form['username'] = user
    br.form['password'] = pwd
    br.form['phone'] = two_fa
    resp = br.submit()
    if resp.code != 200:
        return 'failure'
    
    resp = resp.read().decode('UTF-8')
    soup = BeautifulSoup(resp, 'lxml')
    # print(soup.prettify())
    result = soup.find(id='result').text

    if result == 'success.':
        response = br.open(spellcheck_url)
        if response.code != 200:
            return 'failure'

        soup = BeautifulSoup(response.read().decode('UTF-8'), 'lxml')
        # print(soup.prettify())

        br.select_form(nr = 0)
        br.form['input_content'] = words_to_check
        resp = br.submit()
        if resp.code != 200:
            return 'failure'
        
        resp = resp.read().decode('UTF-8')
        soup = BeautifulSoup(resp, 'lxml')
        # print(soup.prettify())
        
        output_words = soup.find("textarea", id="textout").string
        misspelled_words = soup.find("textarea", id="misspelled").string
    
    br.close()
    return output_words, misspelled_words

# ==========================================================================
def logout(user, pwd, two_fa):

    br = mechanize.Browser()
    br.set_debug_http(False)
    br.set_handle_refresh(False)
    br.set_handle_robots(False)

    cj = http.cookiejar.CookieJar()
    br.set_cookiejar(cj)

    br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'),
                     ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                     ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),
                     ('Accept-Language', 'en-US,en;q=0.8,fr;q=0.6'),
                     ('Connection', 'keep-alive')
                    ]
    response = br.open(login_url)                
    if response.code != 200:
        return 'failure'

    soup = BeautifulSoup(response.read().decode('UTF-8'), 'lxml')
    # print(soup.prettify())

    br.select_form(nr = 0)
    br.form['username'] = user
    br.form['password'] = pwd
    br.form['phone'] = two_fa
    resp = br.submit()
    if resp.code != 200:
        br.close()
        return 'failure'
    
    resp = resp.read().decode('UTF-8')
    soup = BeautifulSoup(resp, 'lxml')
    # print(soup.prettify())
    result = soup.find(id='result').text

    if result == 'success.':
        response = br.open(logout_url)
        if response.code != 200:
            br.close()
            return 'failure'

        soup = BeautifulSoup(response.read().decode('UTF-8'), 'lxml')
        # print(soup.prettify())
        if (soup.h3.string == "Abhijit's Awesome Spell Checker"):
            result = 'success'
        else:
            result = 'failure'
    
    br.close()
    return result

    
# ==========================================================================
def test_server_is_alive():
# ==========================================================================
    error = False
    desc = "Test Case #1: test_server_is_alive() - Test if Flask server is running\n"
    err_result = result = ""
    try:
        resp = requests.get(server_addr)
        resp.raise_for_status()
    except HTTPError as http_err:
        error = True
        err_result += "HTTP error occurred\n"
    except Exception as err:
        error = True
        err_result += "Other error occurred\n"
    else:
        result += "Success!!! - Server is running at: " + server_addr
    print(desc + result + err_result)
    assert (not error), "Test Failed: " + err_result


# ==========================================================================
def test_valid_prelogin_pages():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #2: test_valid_prelogin_pages() - Test if all prelogin pages can be accessed\n"
    PAGES = ["/", "/home", "/login", "/register"]
    for page in PAGES:
        try:
            resp = requests.get(server_addr + page)
        except Exception as err:
            error = True        
            err_result += "Error accessing pre-login page: " + page + "\n"
        else:
            result += "Success!: " + page + " found\n"
    print(desc + result + err_result)
    assert (not error), err_result


# ==========================================================================    
def test_invalid_prelogin_page_redirects():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #3: test_invalid_prelogin_pages() - Test if authenticated pages redirect to approp. pre-login pages before login\n"
    
    # /logout => /home & /spell_check => /login
        
    try:
        resp = requests.get(server_addr + "/logout")
    except Exception as err:
        error = True
        err_result += "Error! Not directed to /home or server is down\n"
    else:
        soup = BeautifulSoup(resp.text, 'lxml')
        home_hdr = soup.h3.text
        if home_hdr == "Abhijit's Awesome Spell Checker":
            result += "/logout correctly re-directed to /home - header found: [" + home_hdr + "]\n"
        else:
            error = True
            err_result += "Error! Not directed to /home\n"            
        
    try:
        resp = requests.get(server_addr + "/spell_check")
    except Exception as err:
        error = True
        err_result += "Error! Not directed to /login or server is down\n"
    else:
        soup = BeautifulSoup(resp.text, 'lxml')
        login_hdr = soup.legend.text
        if login_hdr == "Log In":
            result += "/spell_check correctly re-directed to /login - header found: [" + login_hdr + "]\n"
        else:
            error = True
            err_result += "Error! Not directed to /login\n"
        
    print(desc + result + err_result)
    assert (not error), err_result


# ==========================================================================
def test_register_with_valid_creds():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #4: test_register_with_valid_creds() - Register a new user with valid creds\n"
    user_name = "testcase_4_user"
       
    if register(user_name, '12345678', '9083593333') != 'success':
        err_result = "Registration failed for user: <" + user_name + ">"
        error = True
    else:
        result = "Successfully registered user: <" + user_name + ">"
        
    print(desc + result + err_result) 
    assert (not error), err_result

    
# ==========================================================================
def test_register_with_duplicate_username():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #5: test_register_with_duplicate_username() - Register using existing user name - unique constraint violation\n"
    user_name = "testcase_4_user"
    
    if register(user_name, '12345678', '9083593333') == 'success':
        err_result = "Registration succeeded erroneously for duplicate user: <" + user_name + ">"
        error = True
    else:
        result = "Success! - Registration failed for duplicate user name as expected"
        
    print(desc + result + err_result)
    assert (not error), err_result


# ==========================================================================
def test_register_with_invalid_password():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #6: test_register_with_invalid_password() - Register using a password less than 8 chars\n"
    user_name = "testcase_6_user"
            
    if register(user_name, '1234567', '9083593333') == 'success':
        err_result = "Registration succeeded erroneously with password of invalid length for user: <" + user_name + ">"
        error = True
    else:
        result = "Success! - Registration failed for invalid password as expected"

    print(desc + result + err_result)
    assert (not error), err_result


# ==========================================================================
def test_register_with_invalid_2fa():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #7: test_register_with_invalid_2fa() - Register using an invalid 2fa phone number\n"
    user_name = "testcase_7_user"
       
    if register(user_name, '12345678', '0001112222') == 'success':
        err_result = "Registration succeeded erroneously with invalid phone number (2fa) for user: <" + user_name + ">"
        error = True
    else:
        result = "Success! - Registration failed for invalid 2fa (phone no.) as expected"
    
    print(desc + result + err_result)
    assert (not error), err_result


# ==========================================================================
def test_login_with_valid_creds():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #8: test_login_with_valid_creds() - Login using valid registered user creds\n"
    user_name = "testcase_4_user"
    
    if login(user_name, '12345678', '9083593333') != 'success.':
        err_result = "Login failed for user: <" + user_name + ">"
        error = True
    else:
        result = "Success! - user: <" + user_name + "> Logged in successfully"
        
    print(desc + result + err_result)
    assert (not error), err_result


# ==========================================================================
def test_login_with_invalid_username():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #9: test_login_with_invalid_username() - Login using unregistered user name\n"
    user_name = "unregistered_user"
      
    if login(user_name, '12345678', '9083593333') == 'success.':
        err_result = "Login succeeded erroneously for unregistered user: <" + user_name + ">"
        error = True
    else:
        result = "Success! - Login failed for invalid user name as expected"
        
    print(desc + result + err_result)
    assert (not error), err_result   


# ==========================================================================
def test_login_with_invalid_password():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #10: test_login_with_invalid_password() - Login using invalid password for a registered user\n"
    user_name = "testcase_4_user"
    
    if login(user_name, 'bad_password', '9083593333') == 'success.':
        err_result = "Login succeeded erroneously with invalid password for registered user: <" + user_name + ">"
        error = True
    else:
        result = "Success! - Login failed for invalid password as expected"

    print(desc + result + err_result)
    assert (not error), err_result
    
    
# ==========================================================================
def test_login_with_invalid_2fa():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #11: test_login_with_invalid_2fa() - Login using invalid 2fa (phone no.) for a registered user\n"
    user_name = "testcase_4_user"
    
    if login(user_name, '12345678', '9080000000') == 'success.':
        err_result = "Login succeeded erroneously with invalid 2fa (phone no,) registered user: <" + user_name + ">"
        error = True
    else:
        result = "Success! - Login failed for invalid 2fa (phone no.) as expected"

    print(desc + result + err_result)
    assert (not error), err_result
    
    
# ==========================================================================
def test_logout_after_valid_login():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #12: test_logout_after_valid_login() - Log out of a valid session to be redirected to home page\n"
    user_name = "testcase_4_user"

    if logout(user_name, '12345678', '9083593333') != 'success':
        err_result = "Logout failed to redirect to /home for user: <" + user_name + ">"
        error = True
    else:
        result = "Success! - Logout successfully closed session and redirected user to home page"
        
    print(desc + result + err_result)    
    assert (not error), err_result


# ==========================================================================
def test_spell_check_service():
# ==========================================================================
    error = False
    err_result = result = ""
    desc = "Test Case #13: test_spell_check_service() - Call spell_check service and validate output text and misspelled words\n"
    user_name = "testcase_4_user"
    
    input_words = "one onne two twoo three thre four foure dont worrie bei happpy 1234567890 $elephant$ %mon*key"
    misspelled_expected = "onne, twoo, thre, foure, dont, worrie, bei, happpy, mon*key"
    output_words = misspelled_words = ""

    output_words, misspelled_words = spellcheck(user_name, '12345678', '9083593333', input_words)
    print("=================")
    print("Input Words to be spell checked <inputtext>: " + input_words)
    print("Output Content <textout>: " + output_words)
    print("Expected Misspelled Words <misspelled_expected>: " + misspelled_expected)
    print("Misspelled Words <misspelled>: " + misspelled_words)
    print("=================")
        
    if input_words != output_words:
        error = True
        err_result += "Output text does not match input words to be spell checked"
    else:
        result += "Success! - Input Words in element id <inputtext> match Output Words in element id <textout>\n"

    if misspelled_expected != misspelled_words:
        error = True
        err_result += "Misspelled words identified do not match the expected list"
    else:
        result += "Success! - Misspelled Words identified by spell_check program (a.out) match the expected misspelled words\n"
    
    print(desc + result + err_result)    
    assert (not error), err_result
