FROM python
WORKDIR /usr/local/bin
COPY Cherre01.py .
COPY testdb.db .
COPY unit_test.py .
COPY shell.sh .
RUN pip install pandas
RUN pip install flask
RUN chmod a+x shell.sh
EXPOSE 5000
CMD shell.sh



