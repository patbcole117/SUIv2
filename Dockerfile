FROM python:alpine3.7
COPY . /sui
WORKDIR /sui
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]