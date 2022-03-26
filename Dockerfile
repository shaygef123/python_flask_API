FROM python
ENV ACCESS_KEY="aws_key", SECRET_ACCESS_KEY="aws_secret_key"
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3","main.py"]