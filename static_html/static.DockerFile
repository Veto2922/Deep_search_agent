

FROM python:3.13.4-slim-bullseye

WORKDIR /app


# RUN mkdir -p /static_folder
COPY ./static_html/src .

RUN echo "hello" > index.html


# docker build -f DockerFile -t pyapp .
# docker run -it pyapp

# docker build -f DockerFile -t  abelrahman2922/ai-app-test:latest .
# docker push  abelrahman2922/ai-app-test:latest 


# python -m http.server 8000
# docker run -it -p 4000:8000 pyapp
CMD ["python", "-m", "http.server", "8000"]

