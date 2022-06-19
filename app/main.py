from fastapi import FastAPI, Form, Request, HTTPException
from app.helpers import check_email, check_origin, get_allowed_origins
from app.sender import Sender
import configparser, os, json

app = FastAPI()


ALLOWED_URLS = get_allowed_origins()

@app.post("/api/submit/{to_mail}")
async def submit(
    to_mail: str,
    request: Request,
    name: str = Form(),
    subject: str = Form(),
    email: str = Form(),
    message: str = Form()
    ):
    
    # Check that the origin domain is the same as the domain for the mail
    origin_url = request.headers['origin']
    
    if not origin_url in ALLOWED_URLS:
        raise HTTPException(status_code=400, detail=f"Invalid origin domain: {origin_url}")
    
    if not check_email(email):
        raise HTTPException(status_code=400, detail=f"invalid form email: {email}")
    
    if check_origin(origin_url, to_mail):
        try:
            sender = Sender()
            sender.send_mail(to_email=to_mail, name=name, email=email, message=message, subject=subject)
            return("success")
        except:
            raise HTTPException(status_code=400, detail="Mail client error")
        
    else:
        raise HTTPException(status_code=400, detail=f"Invalid target email")
    
