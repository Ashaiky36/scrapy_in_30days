import scrapy

class quotes_pg1_spider(scrapy.Spider):
    name = "quotes_pg1"
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
            
        #using xpath
        first_author_name = quote.xpath('//small[@class="author"/text()]').get()
        self.log(f"first author name is :{first_author_name}")

