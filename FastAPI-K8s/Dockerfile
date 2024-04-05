FROM python:3.9
WORKDIR /app
COPY ./virtualizacion-a3/ /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]