FROM python:alpine3.7
COPY . /SUI
WORKDIR /SUI
RUN pip install -r requirements.txt
EXPOSE 50300
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]