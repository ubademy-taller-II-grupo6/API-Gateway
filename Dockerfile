FROM python:3.7.4-slim-stretch
WORKDIR /app
COPY ./autenticacion/*.py ./autenticacion/
COPY ./models/*.py ./models/
COPY ./router/*.py ./router/
COPY ./routers/*.py ./routers/
COPY ./schemas/*.py ./schemas/
COPY ./app.py ./
COPY ./requirements.txt ./
COPY ./ubademy-apigateway-firebase-adminsdk-hbeag-c06eb7278c.json ./
ENV PORT=5000
RUN pip install -r requirements.txt
RUN pip install pymongo[srv]
CMD [ "python3", "app.py" ]







