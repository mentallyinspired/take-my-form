from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


form = {
    "name": "Anders Svensson",
    "subject": "Support",
    "email": "anders@gmail.com",
    "message": "I want to support this project"
}

form_bad = {
    "name": "Anders Svensson",
    "subject": "Support",
    "email": "anders@gmail",
    "message": "I want to support this project"
}

def test_submit_good():
    response = client.post(
        "http://domain.com/api/submit/name@domain.com",
        data=form)
    assert response.status_code == 200
    

def test_submit_wrong_domain():
    response = client.post(
        "http://domainer.com/api/submit/name@domain.com",
        data=form)
    assert response.status_code == 400
    
    
def test_submit_wrong_mail():
    response = client.post(
        "http://domain.com/api/submit/name@domainer.com",
        data=form)
    assert response.status_code == 400

def test_submit_incorect_form_email():
    response = client.post(
        "http://domain.com/api/submit/name@domain.com",
        data=form_bad)
    assert response.status_code == 400