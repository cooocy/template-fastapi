FROM docker.io/python:latest

RUN mkdir /workspace
WORKDIR /workspace

COPY requirements.txt .

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY . .

ENTRYPOINT python3 src/main.py
