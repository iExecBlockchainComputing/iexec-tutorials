# Use an official Python runtime as a parent image
FROM python:3.6-slim

RUN apt-get update && apt-get install -y wget zip

# Set the working directory to /app
WORKDIR /

# Install any needed packages
RUN pip install scikit-learn matplotlib

# Add program file and data management
COPY svm_classification_paramstudy.py /.
COPY ./entrypoint.sh /.
RUN chmod +x /entrypoint.sh

# Run app.py when the container launches
ENTRYPOINT ["/entrypoint.sh"]
