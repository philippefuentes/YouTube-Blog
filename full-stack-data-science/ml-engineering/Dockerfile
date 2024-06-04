# start from python base image
FROM python:3.10

# coompatibility lambda
WORKDIR /var/task

# add requirements file to image
COPY ./requirements.txt .

# install python libraries
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# add python code
COPY ./app/ ./app

# set environment variable for Hugging Face cache directory pointing to AWS EFS volume mounted at /mnt/efs
# test download hf model dans le container
# ENV HF_HOME=/code/app/data

# specify default commands
CMD ["fastapi", "run", "app/main.py", "--port", "80"]