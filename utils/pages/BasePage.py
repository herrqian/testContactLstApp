from typing import Union

from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.constants.common import *


class BasePage(object):
    def __init__(self, driver: Union[Chrome, Firefox, Edge], logger):
        """
        Initialize BaseClass.
        """
        self.driver = driver
        self.logger = logger

    def wait_element_to_be_clickable(self, driver, element_method: str, element_to_wait, wait_time=40) -> WebElement:
        """
        Method to wait till element to be clickable.
        :param driver: driver
        :param element_method: Method used to find locator (XPATH, ID, CSS_SELECTOR, etc)
        :param element_to_wait: Element to wait.
        :param wait_time: time to wait
        :return element: returns element if found successfully else None
        """
        element = None
        if element_method.upper() == LOCATE_BY_XPATH:
            element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, element_to_wait)))
        elif element_method.upper() == LOCATE_BY_ID:
            element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.ID, element_to_wait)))
        elif element_method.upper() == LOCATE_BY_CLASS:
            element = WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable((By.CLASS_NAME, element_to_wait)))
        elif element_method.upper() == LOCATE_BY_CSS_SELECTOR:
            element = WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, element_to_wait)))
        elif element_method.upper() == LOCATE_BY_LINK_TEXT:
            element = WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable((By.LINK_TEXT, element_to_wait)))
        else:
            self.logger.info("Pass valid method to find locator")
        return element

    def wait_element_to_be_visible(self, driver, element_method, element_to_wait, wait_time=40) -> WebElement:
        """
        Method to wait till element to be visible.
        :param driver: driver
        :param element_method: Method used to find locator (XPATH, ID, CSS_SELECTOR, etc)
        :param element_to_wait: Element to wait
        :param wait_time: Time to wait
        :return element: returns element if found successfully else None
        """
        element = None
        if element_method.upper() == LOCATE_BY_XPATH:
            element = WebDriverWait(driver, wait_time).until(
                EC.visibility_of_element_located((By.XPATH, element_to_wait)))
        elif element_method.upper() == LOCATE_BY_ID:
            element = WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.ID, element_to_wait)))
        elif element_method.upper() == LOCATE_BY_CLASS:
            element = WebDriverWait(driver, wait_time).until(
                EC.visibility_of_element_located((By.CLASS_NAME, element_to_wait)))
        elif element_method.upper() == LOCATE_BY_CSS_SELECTOR:
            element = WebDriverWait(driver, wait_time).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, element_to_wait)))
        elif element_method.upper() == LOCATE_BY_LINK_TEXT:
            element = WebDriverWait(driver, wait_time).until(
                EC.visibility_of_element_located((By.LINK_TEXT, element_to_wait)))
        else:
            self.logger.info("Pass valid method to find locator")
        return element

    def find_element(self, driver, element_method, element_to_find, retry=2, wait_time=40) -> WebElement:
        """
        Method to find the element.
        :param driver: driver
        :param element_method: Method used to find locator (XPATH, ID, CSS_SELECTOR, etc)
        :param element_to_find: element to find
        :param retry: Number of times to find element
        :param wait_time: Time to wait
        :return element: returns element if found successfully else None
        """
        element = None
        if element_method.upper() == LOCATE_BY_XPATH:
            element = driver.find_element(By.XPATH, element_to_find)
        elif element_method.upper() == LOCATE_BY_ID:
            element = driver.find_element(By.ID, element_to_find)
        elif element_method.upper() == LOCATE_BY_CLASS:
            element = driver.find_element(By.CLASS_NAME, element_to_find)
        elif element_method.upper() == LOCATE_BY_CSS_SELECTOR:
            element = driver.find_element(By.CSS_SELECTOR, element_to_find)
        elif element_method.upper() == LOCATE_BY_LINK_TEXT:
            element = driver.find_element(By.LINK_TEXT, element_to_find)
        else:
            self.logger.info("Pass valid method to find locator")
        return element
