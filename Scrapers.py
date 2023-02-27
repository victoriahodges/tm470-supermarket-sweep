import scrapy
class Tesco_spider(scrapy.Spider):
    name = 'tesco'
    allowed_domains = ['https://www.tesco.com']
    start_urls=["https://www.tesco.com/groceries/en-GB/search?query=apples"]
    # def __init__(self,searches):
    #     assert type(searches)==list
    #     # root='https://www.tesco.com/groceries/en-GB/search?query='
    #     # start_urls = []
    #     # for search in searches:
    #     #     tmp=root + search
    #     #     start_urls.append(tmp)
        
        
    def parse(self,response):
        for product in response.css("li.product-list--list-item"):
           yield {
              prices:,product.css("p.-price__text::text")
              prices_per:,product.css("p.beans-price__text::text")
           }


        
    