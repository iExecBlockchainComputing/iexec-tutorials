FROM python:3.6-slim

RUN apt-get update && apt-get install -y wget zip gcc tk xvfb libasound2 libnss3-dev libgconf2-4 libgtk2.0-0

# Set the working directory to /app
WORKDIR /

#RUN
RUN cd opt/ && wget https://github.com/plotly/orca/releases/download/v1.2.0/orca-1.2.0-x86_64.AppImage && cd /
RUN chmod +x /opt/orca-1.2.0-x86_64.AppImage
RUN  cd /opt && ./orca-1.2.0-x86_64.AppImage --appimage-extract && cd -
RUN ln -s /opt/orca-1.2.0-x86_64.AppImage /opt/orca

ENV PATH /opt/squashfs-root/app/:$PATH

# Install any needed packages
RUN pip install scikit-learn nilearn matplotlib pandas
RUN pip install statsmodels seaborn plotly ipython psutil
COPY ./cloudcoin.py /
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
