# -*- coding: utf-8 -*-

# Scrapy settings for tbls project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tbls'

SPIDER_MODULES = ['tbls.spiders']
NEWSPIDER_MODULE = 'tbls.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tbls (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
    'cookie': 't=26e11ccc68324a60bb8c6654db459023; lLtC1_=1; cookie2=1fc4112a591e9d5d733729113ce3de70; _tb_token_=3310375355e70; _samesite_flag_=true; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5hp1FbH%2B%2BF5QUfRtmaNZ6xeNvGYszzTEalkxx3NNYjigEQoQ2WBBqfagwxOmZJ4lL0TAwa5iSCsJJIy%2FpN6qr7eQ9%2B79TLmD1pGxIwifLOojJrenV8x3Hr9sOjCqnUkjGhHL%2BOJtQ8UEIBDWxd%2BapXalKqviZNBqpBA822a2ut0PCFeeEVjqQxNdTvSgUNUMF3SfEWcKUlTPJnud3Ouu6KXxtomYO2kwVyWr5YO%2FEQ3qO5W3ktSgZLPTUrV2A%3D%3D; thw=cn; cna=0OA1FzTprEkCAXQXeEOomxbL; sgcookie=EiY%2BgmeaxtfmVIjrnpQ%2Fi; unb=2059568441; uc3=nk2=D8q%2FtWbDtlBbLA8%3D&lg2=URm48syIIVrSKA%3D%3D&id2=UUjUI32zDMfuZA%3D%3D&vt3=F8dBxGZvsPZlJvxAjSo%3D; csg=c92d7781; lgc=li983235136; cookie17=UUjUI32zDMfuZA%3D%3D; dnk=li983235136; skt=a0f80337ca94c21d; existShop=MTU4OTk2NTI1OA%3D%3D; uc4=id4=0%40U2o2%2Fqrg7BQqpNyT8g%2FUt2nW7edq&nk4=0%40DemFqE3S3uOdjuMJfnxZEIYLXsl03g%3D%3D; tracknick=li983235136; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=617; _nk_=li983235136; cookie1=AC4CPeoLvzLgErAI0W9VV%2BGPfaLXLNO5oCerdNV1vVM%3D; tfstk=cXlGBjVZfAy623HsPNNsor2_cdvRaFC4qjlITfZZjlPUD6h07sbdLTzJYeqijjBf.; isg=BEFBviFG-1S-Xhcfi39bDAqOUI1bbrVgz2ICnKOXNMinimVc5b0MMdvLbP7Mgk2Y; l=eBE-pZ_HQlZaypE_BO5Zhurza77TiIOfGsPzaNbMiInca6wVtFOm-NQDw4NXSdtjgtfDwExzAHaKsR3y7-zU-AkDBeYCPlUOrYJ9-; mt=ci=31_1; uc1=pas=0&cookie21=URm48syIZJwTkNGk7euL6g%3D%3D&cookie14=UoTUM2nU%2BydTjA%3D%3D&cookie15=URm48syIIVrSKA%3D%3D&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tbls.middlewares.TblsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tbls.middlewares.TblsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tbls.pipelines.TblsPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
