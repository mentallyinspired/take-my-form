from fastapi import FastAPI, Form, Request, HTTPException
from app.helpers import check_email, check_origin, get_allowed_origins, create_config_file
from app.sender import Sender

create_config_file()

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
    
    # Check that the origin domain is in our list
    if not check_origin(request.headers.get("origin"), ALLOWED_URLS):
        raise HTTPException(status_code=400, detail="Invalid origin domain")


    if not check_email(email):
        raise HTTPException(status_code=400, detail="Invalid form email")
    if not check_email(to_mail):
        raise HTTPException(status_code=400, detail="Invalid target email")
    

    try:
        sender = Sender()
        sender.send_mail(to_email=to_mail, name=name, email=email, message=message, subject=subject)
        return("success")
    except:
        raise HTTPException(status_code=400, detail="Mail client error")
    
