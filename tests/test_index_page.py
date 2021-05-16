import requests
import app

main_url = 'http://127.0.0.1:5000/'

def test_index_status_code():
    r = requests.get(url=main_url)
    assert r.status_code == 200