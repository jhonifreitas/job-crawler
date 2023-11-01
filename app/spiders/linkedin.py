import scrapy
from scrapy.utils.response import open_in_browser


class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ["linkedin.com"]
    api_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search'

    def _getUrl(self, start = 0):
        params = {
            'keywords': 'angular',
            'location': 'Brazil',
            'f_TPR': 'r86400', # Last 24h
            'f_WT': 2, # Remote
            'start': start,
        }

        url = self.api_url

        for index, paramName in enumerate(params):
            paramValue = params[paramName]
            typeParam = '?' if index == 0 else '&' 
            url += f'{typeParam}{paramName}={paramValue}'

        return {'url': url, 'params': params}
    
    def start_requests(self, start = 0):
        obj = self._getUrl(start)
        yield scrapy.Request(url=obj['url'], callback=self.parse_jobs, meta=obj['params'])

    def parse_jobs(self, response):
        jobs = response.css("li")
        jobLength = len(jobs)

        print('\n### JOBS ###')
        print(f'{jobLength}\n')
        
        for job in jobs:
            link = job.css(".base-card__full-link::attr(href)").get().strip()
            
            if link:
                yield scrapy.Request(url=link, callback=self.parse_job)

        if jobLength == 25:
            start = response.meta['start'] + 25
            obj = self._getUrl(start)
            yield scrapy.Request(url=obj['url'], callback=self.parse_jobs, meta=obj['params'])

    def parse_job(self, response):
        yield open_in_browser(response)
