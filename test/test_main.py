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
        "https://test.test/api/submit/name@testmail.com",
        headers={"origin": "https://your.domain"},
        data=form)
    assert response.status_code == 400
    ## Sucess if we reach "Mail client error"
    assert response.json() == {"detail": "Mail client error"}
    
    

def test_submit_wrong_origin():
    response = client.post(
        "https://test.test/api/submit/name@testmail.com",
        headers={"origin": "https://another.domain"},
        data=form)
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid origin domain"}
    
    
def test_submit_wrong_mail():
    response = client.post(
        "https://test.test/api/submit/name@testmail",
        headers={"origin": "https://your.domain"},
        data=form)
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid target email"}

def test_submit_incorect_form_email():
    response = client.post(
        "https://test.test/api/submit/name@testmail.com",
        headers={"origin": "https://your.domain"},
        data=form_bad)
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid form email"}