import os
import sys

from selenium import webdriver


def create_driver(headless):
    gecko_options = webdriver.FirefoxOptions()

    if headless:
        gecko_options.add_argument("-headless")

    driver = webdriver.Firefox(
        executable_path=_get_driver_path(),
        options=gecko_options
    )

    return driver


def _get_driver_path():
    slash = ''
    driver_path = os.path.dirname(os.path.abspath(__file__))

    if sys.platform == "win32" or sys.platform == "cygwin":
        slash = "\\geckodriver\\geckodriver_win"
        driver_path += slash
    elif sys.platform == "darwin":
        slash = "/geckodriver/geckodriver_mac"
        driver_path += slash
        os.chmod(driver_path, 755)  # Ensures permission to use Geckodriver
    elif sys.platform == "linux" or sys.platform == "linux2":
        slash = "/geckodriver/geckodriver_linux"
        driver_path += slash
        os.chmod(driver_path, 755)  # Ensures permission to use Geckodriver

    return driver_path
