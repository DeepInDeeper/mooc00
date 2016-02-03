from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from dytt.items import DyttItem

class dyttSpider(Spider):
	name = "dytt"
	allowed_domains = ["dytt8.net"]
	start_urls = ["http://www.dytt8.net"]

	def parse(self,response):
		sel = Selector(response)
		item = DyttItem()

		dyurl=sel.xpath('//div[@class="co_content2"]').xpath('.//a[contains(@href,"gndy")]/@href').extract()
		dynaming=response.xpath('//div[@class="co_content2"]').xpath('.//a[contains(@href,"gndy")]/text()').extract()

		item['link'] = [n.encode('utf-8') for n in dyurl]

		item['dyName'] = [n.encode('utf-8') for n in dynaming]
		
		return item


