FROM python:3.7-alpine
COPY script /script
WORKDIR /script
RUN apk update && \
    apk add --no-cache binutils && \
    pip install --no-cache-dir pyinstaller
RUN pip install --no-cache-dir tweepy && \
    pyinstaller -F main.py

FROM alpine
COPY --from=0 /script/dist/main /script/screen_name.list /
