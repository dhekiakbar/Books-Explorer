import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com"]

    def parse(self, response):
        category_url = response.css("div.side_categories > ul.nav > li > ul > li > a")

        for category in category_url:
            category_name = category.css("a::text").get().strip()
            link = response.urljoin(category.css("a::attr(href)").get())
            yield scrapy.Request(
                url=link,
                callback=self.parse_category,
                meta={"category": category_name}
            )
    
    def parse_category(self, response):
        category_name = response.meta["category"]

        for books in response.css("article.product_pod"):
            yield {
                'name': books.css("h3 > a::attr(title)").get(),
                'category': category_name,
                'stock': books.css("p.instock.availability::text").re_first(r"\w.*\w"),
                'price': books.css("div.product_price > p.price_color::text").get()
            }

        # FIXED PAGINATION
        next_page = response.css("li.next > a::attr(href)").get()
        if next_page is not None:
            yield scrapy.Request(
                url=response.urljoin(next_page),
                callback=self.parse_category,
                meta={'category': category_name}
            )
