import urlparse
from pageobjects.base import selenium_driver

from pageobjects.page import locators
from pageobjects.page import pages
from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class AboutIframeText(BasePageElement):
    def __init__(self):
        pass

    def __set__(self, instance, value):
        driver = selenium_driver.driver
        driver.switch_to_frame(driver.find_elements_by_tag_name('iframe')[0])
        driver.find_elements_by_tag_name('p')[0].send_keys(value)
        driver.switch_to_default_content()


class AboutPageObject(BasePageObject):
    about_iframe_text = AboutIframeText()

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/about/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_class(self.driver, "about-page-text")
        self.assertEqual("Labbler / %s" % pages["dirty-south.name"], self.driver.title)

    def edit_about_click(self):
        self.driver.find_element_by_css_selector("li.edit a").click()
        self.wait_for_element_displayed_by_css(self.driver, "div.text_editor", timeout=5)

    def submit_click(self):
        self.driver.find_element_by_css_selector(locators["about.submit"]).click()

    def save_click(self):
        self.driver.find_element_by_css_selector(locators["about.save"]).click()
