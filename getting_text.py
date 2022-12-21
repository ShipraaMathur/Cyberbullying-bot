from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# Access to Twitter

url = r'https://twitter.com/ShivnaniPratik'

chrome_options = Options()
chrome_options.add_argument("use-fake-ui-for-media-stream")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)
time.sleep(10)
# inputField = driver.find_element(By.CSS_SELECTOR,'.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')
# inputField.send_keys(Keys.TAB + Keys.TAB + Keys.TAB)
# inputField.send_keys('MPCyberBullying')
# inputField.send_keys(Keys.ENTER)
# time.sleep(10)
# inputField = driver.find_element(By.CSS_SELECTOR,'r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu')
# time.sleep(5)
# inputField.send_keys('191IT147')
# inputField.send_keys(Keys.ENTER)
time.sleep(15)
notNow = driver.find_element(by=By.CSS_SELECTOR, value='.r-4qtqp9.r-yyyyoo.r-z80fyv.r-dnmrzs.r-bnwqim.r-1plcrui.r-lrvibr.r-19wmn03')
notNow.click()
time.sleep(2)

'''Scrolling Part'''

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
# print(notNow)



timelineSection = driver.find_element(by=By.CSS_SELECTOR, value='section.css-1dbjc4n')
print(timelineSection)
timelineDiv = timelineSection.find_element(By.XPATH,"//div")
print("blahhh")
# print(timelineDiv)
innerDiv = timelineDiv.find_element(By.XPATH,"//div")

# class="css-1dbjc4n"
divList = innerDiv.find_elements(By.XPATH,"//article")
print(len(divList))
textList = []
attrList = []
for i in divList:
    # print(i.text)
    textList.append(i.text)
    # print(i.get_attribute("aria-labelledby"))
    attrList.append(i.get_attribute("aria-labelledby"))

print(textList)
print(len(divList))
divList[3].click()
time.sleep(1000)

# driver.find_elements_by_css_selector("[aria-label=XXXX]")
# r-4qtqp9 r-yyyyoo r-z80fyv r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-19wmn03

# def comment(index):
#   t = driver.find_element(By.CSS_SELECTOR,f'[aria-labelledby={attrList[index]}]')
    # return