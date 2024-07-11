import os
import pathlib
import pytest
import re

@pytest.fixture
def my_server_name():
    if 'CODESPACES' in os.environ:
        return 'localhost'
    else:
        os.popen('cp /var/www/html/oauth-basic-tutorial/index.html .').read()
        server_name = os.popen("sudo apachectl -S | grep -o -P '\\S+wmdd4950.com'").read()
        if not pathlib.Path('server_name.txt').is_file():
            f = open('server_name.txt','w')
            f.write(server_name)
            f.close()
        return open('server_name.txt').read().strip()

def test_file_exists(my_server_name):
    with open('index.html') as f:
        content = f.read()
        assert len(content) > 0, "index.html must exist"
        
def test_client_id(my_server_name):
    with open('index.html') as f:
        content = f.read()
        assert '467933425294328' not in content, "you must use your own client id"
        
def test_google_login(my_server_name):
    with open('index.html') as f:
        content = f.read()
        assert 'https://accounts.google.com/o/oauth2/v2/auth' in content, (
            "must redirect to google login")

def test_google_token(my_server_name):
    with open('index.html') as f:
        content = f.read()
        assert 'https://oauth2.googleapis.com/token' in content, (
            "must use google token")

def test_http(my_server_name):
    if 'CODESPACES' in os.environ:
        content = os.popen(f'curl --head -s {my_server_name}').read()
    else:
        content = os.popen(f'curl --head -s https://{my_server_name}/oauth-basic-tutorial/').read()
    assert '200' in content
