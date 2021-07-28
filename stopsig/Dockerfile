From python:3.9.6
RUN pip install flask==1.1.1
copy ./server.py /server.py
ENV PORT 80
STOPSIGNAL SIGINT
CMD ["python","-u","/server.py"]
