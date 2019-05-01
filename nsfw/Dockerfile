FROM bvlc/caffe:cpu

RUN apt-get update && apt-get install -y wget zip

# Set the working directory to /app
WORKDIR /

# Install any needed packages
RUN pip install matplotlib pillow

COPY ./classify_nsfw.py /
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
