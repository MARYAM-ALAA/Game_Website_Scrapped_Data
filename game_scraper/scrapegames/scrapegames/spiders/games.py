import scrapy


class GamesSpider(scrapy.Spider):
    name = "games"
    allowed_domains = ["sandbox.oxylabs.io"]
    start_urls = ["https://sandbox.oxylabs.io/products"]

    def parse(self, response):
        games = response.xpath('//div[contains(@class,"product-card")]')
        for game in games:
            yield {
                "name": game.xpath('a[contains(@class,"card-header")]/h4[contains(@class,"title")]/text()').extract(),
                "category": game.css('p.category span::text').extract(),
                "price": game.css('div.product-card div.price-wrapper::text').extract(),
                 "link": game.css('div.product-card a.card-header::attr(href)').extract(),
                 "description": game.css('div.product-card p.description::text').extract(),

                # "rate": response.css('div.product-card div.rating').extract(), #مش عارفة اعمل فور لوب عليها
                # "stock": games.css('div.product-card p.in-stock::text').extract(), # ليسته فاضية


            }

            next_page = response.css('li.next a ::attr(href)').get()
            if next_page is not None :
                next_page_url = 'https://sandbox.oxylabs.io' + next_page
                yield  response.follow(next_page_url , callback=self.parse)

