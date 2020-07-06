FROM python:3.7

ENV PYTHONUNBUFFERED 1

# create target folder
# RUN mkdir -p /python_server

# create and set working directory
WORKDIR /python_server

# copy everything (code) in this folder : "." to target folder : "/python_server in container"
COPY . /python_server 

# Now in the container "/python_server" dir
# install requirements
RUN pip install -r requirements.txt

# Run python server => if we use "entrypoint" in docker-compose.yml to run docker-entrypoint.sh, the command below will be ignored.
# CMD ["python", "manage.py" ,"makemigrations"]
# CMD ["python", "manage.py", "migrate", "--noinput"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]