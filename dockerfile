FROM python:3
RUN git clone https://github.com/perezmatias/Maquina-de-cafe.git
WORKDIR /Maquina-de-cafe
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]