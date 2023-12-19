FROM python:3.10
EXPOSE 5002
RUN mkdir -p /opt/Kulaktandyruu_bot
WORKDIR /opt/Kulaktandyruu_bot

RUN mkdir -p /opt/Kulaktandyruu_bot/requirements
ADD requirements.txt /opt/Kulaktandyruu_bot/

COPY . /opt/Kulaktandyruu_bot/

RUN pip install -r requirements.txt
CMD ["python", "/opt/Kulaktandyruu_bot/main.py"]