from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import JsonItemExporter

class HotelPipeline(object):
    def process_item(self, item, spider):
	    return item
