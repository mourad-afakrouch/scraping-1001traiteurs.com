import scrapy
from scrapy.http.request import Request



# this will extract data by  regions 

class Traiteur(scrapy.Spider):
	name = "my_scraper1"


	# First Start Url
	start_urls = ["https://www.1001traiteurs.com"]

	def parse(self, response):

		#extracting regions urls 
		urls =  response.xpath("//div[contains(@class, 'div-cadre')]/div/a/@href").extract()


		for url in urls:
			# add the scheme, eg http://..
			url  =  'https://www.1001traiteurs.com'+ url

			# go access to every region Url 
			yield Request(url=url, callback=self.parse_details)

	def parse_details(self, response):

		# extrtact  traiteurs Urls from the current page 
		liens = response.xpath("//div[contains(@class, 'vig-list-d')]/div[contains(@class,'left res-1')]//@href").extract()
		

		for lien in liens:
			# add the scheme, eg http://..
			lien = "https://www.1001traiteurs.com"+ str(lien)
			
			# go access to every traiteur Url 
			yield Request(url=lien, callback=self.parse_info)





	def parse_info(self, response):

		# now we are in the traiteur page , we can scrape anything we want 

		Titre =  response.xpath("//div[contains(@class, 'd-contact-traiteur-titre')]/text()").extract()
		tel_1  = response.xpath("//div[contains(@class, 'd-contact-traiteur-tel')]/text()").extract_first()
		website = response.xpath("//span[contains(@class, 'd-contact-libelle')]//@href").extract()
		tel_2  = response.xpath("//div[contains(@class, 'd-contact-traiteur-tel')]/text()")[-1].extract()
		langues= response.xpath("//div[contains(@class, 'd-contact-traiteur-langues')]//text()").extract()
		yield{


				'langues':langues,
				'website':website,
				'tel_2':tel_2,
				'tel_1':tel_1,
				'name':Titre,

				
				}
		"""
		 execute this command   (scrapy crawl my_scraper1 -o file.json)   and  Voilà :)
		 it will create  file.json 

		 that contains all scraped data



