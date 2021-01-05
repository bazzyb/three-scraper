from pprint import pprint

from scraper import Three_Scraper

if __name__ == '__main__':
    scraper = Three_Scraper()
    country_list = scraper.run()
    pprint(country_list)
