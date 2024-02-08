FROM osgeo/gdal:ubuntu-small-3.6.3
RUN apt-get update && apt-get -y install python3-pip --fix-missing
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
CMD ["python", "plaatsen_in_nederland.py"]
