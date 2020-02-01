from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import json

what_are_you_finding = "HR"
link = "https://www.linkedin.com/uas/login"
link2 = f"https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22by%3A0%22%5D&facetIndustry=%5B%2296%22%2C%224%22%2C%226%22%5D&keywords={what_are_you_finding}&origin=FACETED_SEARCH"
browser = webdriver.Chrome()
browser.get(link)
mail = browser.find_element_by_css_selector("#username")
mail.send_keys("email")
password = browser.find_element_by_css_selector("#password")
password.send_keys("password")
sign_in_button = browser.find_element_by_xpath("//div[@id='app__container']/main[@role='main']//form[@action='/checkpoint/lg/login-submit']//button[@class='btn__primary--large from__button--floating']")
sign_in_button.click()
browser.get(link2)
time.sleep(4)
count_pages = 20
buttons = len(browser.find_elements_by_xpath("//button[contains(@aria-label, 'Установить')]"))

while buttons == 0:
    count_pages += 1
    browser.get(
            f"https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22by%3A0%22%5D&facetIndustry=%5B%2296%22%2C%224%22%5D&keywords=recruiter&origin=FACETED_SEARCH&page={count_pages}")
    time.sleep(4)
    buttons = len(browser.find_elements_by_xpath("//button[contains(@aria-label, 'Установить')]"))

    while count_pages <= 100 and (len(browser.find_elements_by_xpath("//button[contains(@aria-label, 'Установить')]")) != 0):
            buttons = len(browser.find_elements_by_xpath("//button[contains(@aria-label, 'Установить')]"))
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            if buttons == 0:
                break
            browser.execute_script("return arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                           browser.find_element_by_xpath("(//button[contains(@aria-label, 'Установить')])[1]"))
            time.sleep(0.3)
            print(buttons)
            button_contact = browser.find_element_by_xpath("(//button[contains(@aria-label, 'Установить')])[1]")
            button_contact.click()
            time.sleep(0.2)
            button_contact_2 = browser.find_element_by_xpath("//button[contains(@aria-label, 'Отправить')]")
            button_contact_2.click()
            buttons = len(browser.find_elements_by_xpath("//button[contains(@aria-label, 'Установить')]"))
            time.sleep(0.2)




