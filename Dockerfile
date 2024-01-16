FROM Python:3.12.1
WORKDIR C:/EMQU
COPY . C:/EMQU
RUN pip3 install -r requirements.txt
ENTRYPOINT py .\starter.py