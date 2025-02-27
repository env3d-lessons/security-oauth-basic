import os
import pathlib
import pytest
import re

@pytest.fixture
def my_server_name():
    if 'CODESPACES' in os.environ or os.getenv("GITHUB_ACTIONS") == "true":
        return 'localhost'
    else:
        username = os.getlogin()
        current_directory = os.path.basename(os.getcwd())
        if not pathlib.Path('server_name.txt').is_file():
            f = open('server_name.txt','w')
            f.write(f'https://learn.operatoroverload.com/~{username}/{current_directory}/')
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

def test_google_userinfo(my_server_name):
    with open('index.html') as f:
        content = f.read()
        assert 'https://openidconnect.googleapis.com/v1/userinfo' in content, (
            "must use google userinfo endpoint")

def test_http(my_server_name):
    content = os.popen(f'curl --head -s {my_server_name}').read()
    assert '200' in content
