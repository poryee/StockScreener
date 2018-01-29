# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.exporters import CsvItemExporter
import csv



class AiscreenerPipeline(object):
    def __init__(self):
        self.csvwriter = csv.writer(open('FinancialData.csv', 'w', newline=''))
        self.headers_written = False

    def process_item(self, item, spider):
        if not self.headers_written:
            header_keys = item.fields.keys()
            self.csvwriter.writerow(
                ["Symbol", "Name", "Currency", "Price", "Year Low",
                 "Year High", "Marketcap", "PE Ratio", "Book Value",
                 "PB Ratio", "Divident", "PEG"])

            self.headers_written = True

        info=item['name'][0].split('-')
        self.csvwriter.writerow([info[0], info[1], item['currency'][0].replace("Currency in ",""), item['price'], item['year_low'][0], item['year_high'][0], item['marketcap'][0], item['pe_ratio'][0], item['bookvalue'][0], item['pb_ratio'][0], item['trailingdivident'][0], item['PEG'][0]])
        return item