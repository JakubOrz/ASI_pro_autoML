ARG BASE_IMAGE=python:3.8-slim
FROM $BASE_IMAGE as runtime-environment

#
COPY src/autocarml/autocarapi/requirements.txt /code/requirements.txt

#
RUN pip install --upgrade -r /code/requirements.txt

#
COPY src/autocarml/autocarapi  /code/app

COPY data/03_models /data/03_models

#
WORKDIR /code

#
EXPOSE 80
EXPOSE 5000
#
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]