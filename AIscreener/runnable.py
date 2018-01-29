from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from AIscreener.spiders.yahoo import StockSpider


def run():
    #process = CrawlerProcess(get_project_settings())

    settings = get_project_settings()
    #settings.set('FEED_FORMAT', 'json')
    #settings.set('FEED_URI', 'result.json')

    configure_logging()
    runner = CrawlerRunner(settings)
    runner.crawl(StockSpider)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()  # the script will block here until all crawling jobs are finished


if __name__ == '__main__':
    run()