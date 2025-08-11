import scrapy

class quotes_all_spider(scrapy.Spider):
    name = "quotes_all"
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, reponse):
        for quote in reponse.css("div.quote"):
            #using CSS Selectors
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()


            yield {
            "quote": text,
            "author": author,
            "tags": tags,
        }

        # next_page = reponse.css("li.next a::attr(href)").get()
        # if next_page is not None:
        #     next_page = reponse.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

        next_page = reponse.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield reponse.follow(next_page, callback = self.parse)