import scrapy

class WishlistSpider(scrapy.Spider):
    name = "wishlist_spider"
    allowed_domains = ["amazon.co.uk"]
    start_urls = [
        "https://www.amazon.co.uk/hz/wishlist/ls/107HD31LKJTN3?ref_=wl_share"
    ]

    def parse(self, response):
        filename = "wishlist.html"
        with open(filename, 'wb') as f:
            f.write(response.body)