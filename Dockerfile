# Every docker image has to start from another image
# ex. from ubuntu
FROM python:3.11-alpine 
COPY . . 
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "iss"]