# Take My Form

Take My Form is a easy to implement endpoint for your HTML forms.
Perfect for your static/jamstack sites.

It uses FastAPI, smtplib and EmailMessage to take care of everything

Implementation on the frontend is as simple as:
```html
<form action="https://yourdomain.com/api/submit/your@email.com" method="POST">
     <input type="text" name="name" required>
     <input type="text" name="subject" required>
     <input type="email" name="email" required>
     <input type="email" name="message" required>
     <button type="submit">Submit</button>
</form> 
```

## How it works
**On submission**
1. Check if the domain of the sending email and webbsite are the same
2. Submit if the domains are the same, otherwise fail the submission

It's as simple as that.


## How to run it
Take My Form is currently in beta (it works as intended).
Run it in python venv with uvicorn. Dockerfile isn't done yet.

### Config
Add your SMTP config to the `config.ini` file

### The simple (not recomended, only for testing)
```bash
pip install "uvicorn[standard]"
uvicorn main:app --host 0.0.0.0 --port 80
```

### The proper way (with reverse proxy)
Get yourself a reverse proxy, like nginx or traefik.
Set it up to point to your chosen port (8080 in this instance).

```bash
pip install "uvicorn[standard]"
uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8080
```

`--proxy-headers` will tell uvicorn to trust the headers sent by your reverse proxy

### Form action
Point your form `action` to `../api/submit/your@email.com` like:
```html
<form action="https://yourdomain.com/api/submit/your@email.com" method="POST">
```




## TODO
- [ ] Build docker container
- [ ] Docker-compose file with reverse proxy
- [ ] Implement static CORS
- [ ] Implement validation process for sending emails
    - This will allow the server make use of emails with different domain to the website the form is in
- [ ] Probably more