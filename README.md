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

1. Clone this git repo
2. Adjust the config
2. Build container
3. Run the container

### Config
Add your SMTP config to the `config.ini` file
The config will go inside the container for now
DO NOT SHARE THE IMAGE: as the image will container your smtp info

### Build docker container
```bash
$ docker build -t take-my-form .
```

### Run it
**docker**
```
$ docker run -d --name take-my-form -p 80:80 take-my-form
```
**docker-compose**
```
$ docker-compose up -d
```

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