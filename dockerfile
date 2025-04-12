FROM python:alpine
ADD main.py .
RUN pip install worldnewsapi
CMD ["python", "./main.py"]