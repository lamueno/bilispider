import scrapy


class BilispiderItem(scrapy.Item):
    av = scrapy.Field()
    title = scrapy.Field()
    channel = scrapy.Field()
    post_time = scrapy.Field()
    coin = scrapy.Field()
    favorite = scrapy.Field()
    his_rank = scrapy.Field()
    now_rank = scrapy.Field()
    comments = scrapy.Field()
    share = scrapy.Field()
    replay = scrapy.Field()
    uploader = scrapy.Field()
    tag_list = scrapy.Field()
    description = scrapy.Field()

