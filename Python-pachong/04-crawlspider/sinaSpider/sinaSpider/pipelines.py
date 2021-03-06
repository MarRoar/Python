# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinaspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class SinaPipeline(object):

	def process_item(self, item, spider):
		sonUrls = item['sonUrls']

		filename = sonUrls[7:-6].replace('/', '_')
		filename += ".txt"

		fp = open(item['subFilename'] + '/' + filename, 'w')
		fp.write(item['content'].encode('utf-8'))
		fp.close()

		return item
