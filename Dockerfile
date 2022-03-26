FROM python
EXPOSE 8080
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3","main.py"]