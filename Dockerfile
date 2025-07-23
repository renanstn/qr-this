FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x start_server.sh
EXPOSE 5000
CMD ["./start_server.sh"]
