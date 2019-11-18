from tensorflow/tensorflow:latest-gpu

RUN apt-get update
RUN apt-get install bc
COPY workflow.sh .
COPY cifar10* ./
ENTRYPOINT ["/workflow.sh"]
	   