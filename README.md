# Take My Form

Take My Form is a easy to implement endpoint for your HTML forms.
Perfect for your static/jamstack sites.

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
When the form submits to the server it checks origin URL and does a manual CORS validation by comparing the sending email address with the domain of the webbsite.
If the domain of the sending email and webbsite domain are not the same the submission will fail.
If they are the same it will send the email.

It's as simple as this.


## How to run it
Take My Form is currently in beta (it works).
Create a docker image out of it, or run it in python venv with:

### The simple (not recomended, only for testing)
```bash
pip install "uvicorn[standard]"
uvicorn main:app --host 0.0.0.0 --port 80
```

### The proper way (with reverse proxy)
Get yourself a reverse proxy, like nginx or traefik.
Set it up to point to your chosen port, here we have chosen 8080.

```bash
pip install "uvicorn[standard]"
uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8080
```

`--proxy-headers` will tell uvicorn to trust the headers sent by your reverse proxy





## TODO
- [ ] Build docker container
- [ ] Docker-compose file with reverse proxy
- [ ] Implement static CORS
- [ ] Implement validation process for sending emails
    - This will allow the server make use of emails with different domain to the website the form is in
- [ ] Probably more