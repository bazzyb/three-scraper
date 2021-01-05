from utils import create_driver

three_roaming_url = 'http://www.three.co.uk/Support/Roaming_and_international/Roaming_abroad'


def main():
    driver = create_driver(False)

    try:
        driver.get(three_roaming_url)
    except:
        pass
    finally:
        driver.quit()
