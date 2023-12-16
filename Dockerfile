FROM python:3.11.1


WORKDIR /app


RUN pip install aiogram==2.25.1

RUN pip install python-dotenv==1.0.0


COPY . git@github.com:PTavadian/test_app.git

CMD [ "python", "bot_telegram.py" ]







