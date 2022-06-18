FROM python:3.9
WORKDIR /code
ENV MAIL_SERVER=smtp.domain.com
ENV FROM_ADDRESS=email@domain.com
ENV PORT=465
ENV PASSWORD=YourPassWord
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
