FROM python:3.9.13-slim@sha256:4169ae884e9e7d9bd6d005d82fc8682e7d34b7b962ee7c2ad59c42480657cb1d as build
WORKDIR app
COPY . .
RUN pip3 install -r requirements.txt && pip3 install mysql-connector-python
EXPOSE 8001
CMD ["python3", "app.py"]
