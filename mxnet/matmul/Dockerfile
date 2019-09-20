FROM nvcr.io/nvidia/mxnet:18.03-py3


# Set the working directory to /app
WORKDIR /

COPY ./matmul.py /
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
