from scrapy.exceptions import DropItem
from bilispider.db_util import *

class BilispiderPipeline(object):
    def open_spider(self, spider):
        DB_Util.init_db()  # 表不存在时候,初始化表结构

    def process_item(self, item, spider):
        if not item['av']:
            raise DropItem('av_id is null.{0}'.format(item))
        else:
            session = DB_Util.get_session()
            video_info = Video()
            video_info.neeq_code = item['neeq_code']
            video_info.neeq_name = item['neeq_name']
            video_info.industry = item['industry']
            video_info.region = item['region']
            video_info.list_date = item['list_date']
            video_info.broker = item['broker']
            video_info.trade_type = item['trade_type']
            session.add(video_info)
            session.commit()
        return item
