from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = "myshobicrawler"
    allowed_domains = ["ebooks.com"]
    start_urls = ["https://www.ebooks.com/"]


    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
    )

    def parse(self, response):
        container = response.css('.container')

        # Extract site header information
        site_header = container.css('.site-header')
        logo_url = site_header.css('.brand-logo img::attr(src)').get()
        members_count = site_header.css('.slogan span::text').get()
        ebooks_count = site_header.css('.slogan span small::text').get()

        # Extract search box information
        search_box = container.css('.searchbox input#term::attr(placeholder)').get()

        # Extract mobile search bar information
        mobile_search_bar = container.css('#mobile-search-bar a::text').getall()

        # Extract footer information
        footer = container.css('.information')
        country_flag = footer.css('#CountryChangeFlag img::attr(src)').get()
        privacy_link = footer.css('a[href*="privacy/"]::attr(href)').get()
        copyright_link = footer.css('a[href*="copyright/"]::attr(href)').get()
        terms_link = footer.css('a[href*="terms/"]::attr(href)').get()
        affiliates_link = footer.css('a[href*="affiliates/"]::attr(href)').get()
        authors_link = footer.css('a[href*="sell-your-ebooks-on-ebooks-com/"]::attr(href)').get()
        publishers_link = footer.css('a[href*="pi.ebooks.com"]::attr(href)').get()
        facebook_link = footer.css('.sprite-facebook::attr(href)').get()
        twitter_link = footer.css('.sprite-twitter::attr(href)').get()

        # You can further process and yield the extracted data here
        yield {
            'logo_url': logo_url,
            'members_count': members_count,
            'ebooks_count': ebooks_count,
            'search_box': search_box,
            'mobile_search_bar': mobile_search_bar,
            'country_flag': country_flag,
            'privacy_link': privacy_link,
            'copyright_link': copyright_link,
            'terms_link': terms_link,
            'affiliates_link': affiliates_link,
            'authors_link': authors_link,
            'publishers_link': publishers_link,
            'facebook_link': facebook_link,
            'twitter_link': twitter_link,
        }



