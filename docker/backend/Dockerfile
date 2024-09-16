FROM python:3.11-alpine

RUN apk update && apk add python3-dev gcc libc-dev nginx

WORKDIR /app

# COPY ssl/cert.pem /ssl/cert.pem
# COPY ssl/key.pem /ssl/key.pem

# # Set permissions for the certificate and key
# RUN chmod 644 /ssl/cert.pem && \
#     chmod 600 /ssl/key.pem && \
#     chown root:root /ssl/cert.pem && \
#     chown root:root /ssl/key.pem

RUN pip install --upgrade pip
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./ /app
ADD ./docker /app/docker

RUN chmod +x /app/docker/backend/server-entrypoint.sh
