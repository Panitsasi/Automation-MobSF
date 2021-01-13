#!/usr/bin/python3

from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import requests
import sys
import time

name_sample = str(sys.argv[1])

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()

url = "http://localhost:8000"

driver = webdriver.Firefox(firefox_options=fireFoxOptions)
driver.get(url)

def pageContent(url):
   page = requests.get(url)
   return BS(page.content, 'html.parser')


def checkTest():
   check = "wait"
   while check == "wait":
       check_txt = driver.find_element_by_xpath('//textarea[@id="stat"]').text
       if "No Exported Activites found" in check_txt or "Exported Activity testing completed." in check_txt or "No Activites found" in check_txt or "Activity testing completed" in check_txt or "Generating Report...Please Wait!" in check_txt or "Sucessfully created MobSF Dynamic Analysis enviroment." in check_txt:
           check = "continue"
   print("~ RUNNING ~")


soup = pageContent(url)

dynamic_analyzer = soup.find("a", string="DYNAMIC ANALYZER")
url = url + dynamic_analyzer['href']

soup = pageContent(url)
driver.get(url)

android_runtime = driver.find_element_by_xpath('//button[contains(text(), "MobSFy Android Runtime")][@data-target="#mmobsfy"]').click()

android_connect = driver.find_element_by_xpath('//button[contains(text(), "MobSFy!")][@id="mobsfy"]').click()

time.sleep(20)

close_android_runtime = driver.find_element_by_xpath('//button[@class="close"]/span[contains(text(), "×")]').click()

search_sample = driver.find_element_by_xpath('//input[@type="search"][@class="form-control form-control-sm"]').send_keys(name_sample)

package_sample = driver.find_element_by_xpath('//table[@id="DataTables_Table_0"]/tbody/tr/td[3]').text

start_dynamic_analysis = soup.find("a", {"onclick": "dynamic_loader()"})
url = url + start_dynamic_analysis['href']

soup = pageContent(url)
driver.get(url)
time.sleep(10)

select_scripts = driver.find_element_by_xpath('//select[@id="fd_scs"]')
options = [x for x in select_scripts.find_elements_by_tag_name("option")]

for option in options:
   option.click()

load_scripts = driver.find_element_by_xpath("//button[@id='loadscript']").click()

auxiliary = driver.find_elements_by_xpath('//input[@name="auxiliary"][@type="checkbox"]')

for check in auxiliary:
   check.click()

start_instrumentation = driver.find_element_by_xpath('//button[@id="frida_spawn"][@type="submit"]').click()

start_exported_activity_tester = driver.find_element_by_xpath('//a[@id="expactt"][@role="button"]').click()

time.sleep(60)

start_activity_tester = driver.find_element_by_xpath('//a[@id="actt"][@role="button"]').click()

time.sleep(300)

generate_report = driver.find_element_by_xpath('//a[@id="stop"][@role="button"]').click()

time.sleep(60)

driver.quit()

exit(package_sample)