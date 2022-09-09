import scrapy, requests
from scrapy import Request


def send_msg(text):
   token = "5663097801:AAH8FJmqavokiPJoxg3H4XQVVtQuqYfhEJU"
   chat_id = '240372740'
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
   results = requests.get(url_req)


def clean_spaces(input):
    return input.replace('\n', '').replace('\r', '').strip('\n').strip()


class S2sgeSpider(scrapy.Spider):
    name = 's2sge'
    allowed_domains = ['ss.ge']

    def start_requests(self):
        yield Request('https://ss.ge/en/real-estate/l/Flat/For-Rent?PrcSource=1&RealEstateStatus=2%2C453&CommercialRealEstateType=&PriceType=false&CurrencyId=1&PriceTo=700&Context.Request.Query%5BQuery%5D=&IndividualEntityOnly=true&&Sort.SortExpression=%22OrderDate%22+DESC')

    def parse(self, response):
        #urls = response.xpath('//a[contains(@href, "/en/real-estate")]/@href').extract()

        ads_selectors = response.xpath('//div[@class="latest_article_each "]')
        for ad in ads_selectors:
            url = response.urljoin(ad.xpath('.//div[@class="latest_desc"]/div/a/@href').extract_first())
            price = ad.xpath('.//div[@class="latest_price"]/text()').re_first("\d+")
            location = ad.xpath('.//div[@class="StreeTaddressList"]/a/text()').extract_first()

            message = f"\n {price} \n {clean_spaces(location)} \n {url}"
            #message = url + '##' + price + "##" + location

            send_msg(message)
            pass
