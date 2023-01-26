ARG BASE_IMAGE=python:3.9-slim
FROM $BASE_IMAGE as runtime-environment

#
WORKDIR /code

#
COPY ../requirements.txt /code/requirements.txt

#
RUN pip install --upgrade -r /code/requirements.txt

#
COPY app /code/app

#
EXPOSE 80
EXPOSE 5000
#
CMD ["uvicorn", "app.fastApi:app", "--host", "0.0.0.0", "--port", "80"]