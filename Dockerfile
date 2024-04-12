FROM python3.11

WOKRDIR /registery

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5100



