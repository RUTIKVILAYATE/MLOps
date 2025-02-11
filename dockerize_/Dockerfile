FROM python:3.8-alpine

# copy all the local files in the app folder over docker 
COPY . /app
# make working directory as app in docker

WORKDIR /app

# run command to install all the dependencies
RUN pip install -r requirements.txt

# and finally run app.py to run flask app itself 
CMD python app.py