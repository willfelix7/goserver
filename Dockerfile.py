FROM debian:stable-slim
COPY main.py main.py
COPY books/ books/
RUN <<EOF
apt-get update
apt-get install -y python3
EOF
CMD ["python3", "main.py"]
