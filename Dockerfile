FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

#EXPOSE 5000
EXPOSE 8000

#make container executable
#what commands do you want to run when you create a container out of your docker image
# runs 'python3 index.py' inside of docker container
#ENTRYPOINT [ "python3" ]
#CMD ["index.py"]
ENTRYPOINT [ "gunicorn" ]
CMD ["app:server"]