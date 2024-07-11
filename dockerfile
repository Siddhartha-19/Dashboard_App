FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN python3 -m venv venv

RUN . venv/bin/activate && pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8050

CMD ["sh", "-c", ". venv/bin/activate && python3 freq_adc.py"]