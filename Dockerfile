FROM python:3
ADD wishlist_scrape.py /
CMD [ "python", "./wishlist_scrape.py" ]