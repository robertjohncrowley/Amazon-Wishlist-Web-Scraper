FROM python:3
ADD wishlist_scrape.py /
COPY requirements.txt ./
RUN pip3 install --no-cache-die -r requirements.txt
COPY . .
CMD [ "python", "./wishlist_scrape.py" ]