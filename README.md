# scraping-1001traiteurs.com

Hello 

in this document i will show you 
step by step how to scrap this website = www.1001traiteurs.com

after installing scrapy 

C:\Users\MouradSoft\Desktop> scrapy startproject traiteurs

C:\Users\MouradSoft\Desktop> cd .\traiteurs\

PS C:\Users\MouradSoft\Desktop\traiteurs> ls


    Répertoire : C:\Users\MouradSoft\Desktop\traiteurs


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       23/10/2017     10:28                traiteurs
-a----       23/10/2017     10:28            262 scrapy.cfg


PS C:\Users\MouradSoft\Desktop\traiteurs> cd .\traiteurs\
PS C:\Users\MouradSoft\Desktop\traiteurs\traiteurs> ls


    Répertoire : C:\Users\MouradSoft\Desktop\traiteurs\traiteurs

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       20/10/2017     23:38                spiders
d-----       20/10/2017     23:38                __pycache__
-a----       23/10/2017     10:28            288 items.py
-a----       23/10/2017     10:28           1907 middlewares.py
-a----       23/10/2017     10:28            289 pipelines.py
-a----       23/10/2017     10:28           3158 settings.py
-a----       18/05/2017     22:10              0 __init__.py



PS C:\Users\MouradSoft\Desktop\traiteurs\traiteurs> scrapy shell "https://www.1001traiteurs.com"


response.xpath("//li[contains(@class, 'top5-detail')]").extract()

response.xpath("//li[contains(@class, 'top5-detail')]/div[contains(@class, 'titre-top')]//@href").extract()

for ville in response.xpath("//li[contains(@class, 'top5-detail')]/div[co
    ...: ntains(@class, 'titre-top')]//@href"):
    ...:     link = "https://www.1001traiteurs.com"+ ville.extract()



exit()


scrapy shell "https://www.1001traiteurs.com/paris-d.html"

response.xpath("//div[contains(@class, 'vig-list-d')]/div[contains(@class,
   ...:  'left res-1')]//@href").extract()



for traiteur in response.xpath("//div[contains(@class, 'vig-list-d')]/div[contains(@class,'left res-1')]//@href"):
	sublink = "https://www.1001traiteurs.com" + triateur.extract()







