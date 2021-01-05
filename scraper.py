import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from utils import create_driver


class Three_Scraper:
    def __init__(self):
        self.three_roaming_url = 'http://www.three.co.uk/Support/Roaming_and_International/Roaming_Abroad/Destinations#countries2'

        self.countries = {
            'Brazil': {},
            'South Africa': {},
            'Portugal': {},
            'Chile': {},
            'Iceland': {},
            'China': {},
            'Madagascar': {}
        }

    def run(self):
        try:
            self.driver = create_driver(True)

            print('Loading initial page')
            self.driver.get(self.three_roaming_url)
            WebDriverWait(self.driver, 10) \
                .until(EC.element_to_be_clickable((By.ID, 'countries2-cont')))

            self.build_country_url_list()

            print('Getting charge information')
            for country in self.countries:
                self.get_charges(country)

            self.close_driver()
            return self.countries

        except:
            # Would put catch for something like Sentry here
            traceback.print_exc()
            self.close_driver()

    def build_country_url_list(self):
        print('Retrieving URLs for each country')

        for country in self.countries:
            url = self.get_country_url(country)
            self.countries[country]['url'] = url

    def get_country_url(self, country):
        xpath_ref = "//a[contains(.,'" + country + ".')]"
        country_link_elem = self.driver.find_element_by_xpath(xpath_ref)
        country_url = country_link_elem.get_attribute('href')
        return country_url

    def get_charges(self, country):
        print(f'Parsing charge information for {country}')

        self.countries[country]['costs'] = {
            'call_to_uk': None,
            'text_to_uk': None,
            'receive_call': None,
            'internet_data': None,
        }

        self.driver.get(self.countries[country]['url'])
        WebDriverWait(self.driver, 10) \
            .until(EC.element_to_be_clickable((By.CLASS_NAME, 'roaming-charges')))

        self.read_table(country)

    def check_if_go_roam_area(self):
        xpath_ref = "//a[contains(.,'Go Roam')]"
        try:
            country_link_elem = self.driver.find_element_by_xpath(xpath_ref)
            return True
        except NoSuchElementException:
            return False

    def read_table(self, country):
        if self.check_if_go_roam_area():
            table_rows = self.driver.find_elements_by_css_selector('.roaming-charges > table tr')
            cell_pos = 1
        else:
            table_elem = self.driver.find_element_by_css_selector('.roaming-charges-table > tbody')
            table_rows = table_elem.find_elements_by_css_selector('tr')
            cell_pos = 0

        for row in table_rows:
            header = row.find_element_by_css_selector('th')
            data_cells = row.find_elements_by_css_selector('td')

            if header and len(data_cells):
                if header.text.startswith('Calling a UK number'):
                    self.countries[country]['costs']['call_to_uk'] = data_cells[cell_pos].text
                if header.text.startswith('Texts to UK'):
                    self.countries[country]['costs']['text_to_uk'] = data_cells[cell_pos].text
                if header.text.startswith('Receiving calls from any number'):
                    self.countries[country]['costs']['receive_call'] = data_cells[cell_pos].text
                if header.text.startswith('Using internet and data'):
                    self.countries[country]['costs']['internet_data'] = data_cells[cell_pos].text

    def close_driver(self):
        # Geckodriver doesn't auto garbage collect on mac,
        # so must ensure driver is closed manually
        if hasattr(self, 'driver'):
            self.driver.quit()
            del self.driver
