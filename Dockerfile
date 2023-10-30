
#base image
FROM python:3.11

#install pipenv
RUN pip install pipenv

#copy filles into new folder /app
COPY . /app

#set working directoty
WORKDIR /app

#install dependancies - including system level (--system) and ensuring
#exact versions (--deploy)
RUN pipenv install --system --deploy

# command used to run flask app
CMD ["python", "app.py"]