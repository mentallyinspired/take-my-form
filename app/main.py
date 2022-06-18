from fastapi import FastAPI, Form, Request, HTTPException
from app.helpers import check_email, check_origin
from app.sender import Sender

app = FastAPI()

@app.post("/api/submit/{to_mail}")
async def submit(
    to_mail: str,
    request: Request,
    name: str = Form(),
    subject: str = Form(),
    email: str = Form(),
    message: str = Form()
    ):
    
    origin_url = request.base_url.hostname
    
    if not check_email(email):
        raise HTTPException(status_code=400, detail=f"Email: {email} is invalid")
    
    if check_origin(origin_url, to_mail):
        try:
            sender = Sender()
            sender.send_mail(to_email=to_mail, name=name, email=email, message=message, subject=subject)
            return("success")
        except:
            raise HTTPException(status_code=400, detail="Mail client error")
        
    else:
        raise HTTPException(status_code=400, detail=f"Target email '{to_mail}' is not valid (../api/submit/target@email)")