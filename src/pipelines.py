# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from datetime import datetime
from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter
from src.items import SchoolItem
from scrapy.utils.project import get_project_settings


class ValidateItemPipeline:
    def process_item(self, item, spider):
        return item


class JsonLinesExportPipeline:

    def __init__(self):

        #consume project settings
        settings = get_project_settings()
        #collect the defined path
        dir_path = settings.get('DATA_OUT','./data')

        d = datetime.now().isoformat(timespec='seconds').replace(':', '_')
        #create a new directory for each run
        if not os.path.isdir(os.path.join(dir_path, d)):
            os.mkdir( f'{os.path.join(dir_path, d)}')

        self.out_path = os.path.join(dir_path, d)

    def open_spider(self, spider):

        self.file = open(os.path.join(self.out_path, 'data.jsonl'), 'wb')
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf8', ensure_ascii=False)
        self.exporter.start_exporting()
        
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        
    def process_item(self, item, spider):
        if isinstance(item, SchoolItem):
            self.exporter.export_item(item)
        return item