import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from telegram_bot import TelegramBot
from mongodb import MongoDB
chrome_driver = webdriver.Chrome()

bot = TelegramBot()
db = MongoDB()


#chrome_driver.get("https://www.welivesecurity.com/la-es/")
#chrome_driver.get("https://www.amazon.com/")
#chrome_driver.get("https://es.aliexpress.com/category/204000316/men-clothing.html?category_redirect=1&spm=a2g0o.best.102.1.30c222aerYFPk2")
#chrome_driver.get("https://best.aliexpress.com")
chrome_driver.get("https://www.backmarket.com/en-us")
print(chrome_driver.title)

topics = [
    "Samsung Galaxy",
    "Lenovo Yoga"
]

for t in topics:
    search_box = chrome_driver.find_element(By.ID, "desktop-searchbar") #Amazon
    #search_box = chrome_driver.find_element(By.ID, "search-key")  # Aliexpress
    #search_box = chrome_driver.find_element(By.ID, "nav-search-field ")

    search_box.send_keys(t)
    #search_button = chrome_driver.find_element(By.CSS_SELECTOR, '#header-nav > div.row.hidden-sm.hidden-xs > form > div > button') blackmarket
   #search_button = chrome_driver.find_element(By.CLASS_NAME, '#nav-belt > div.nav-fill > script:nth-child(3)') Amazon
    #search_button = chrome_driver.find_element(By.CLASS_NAME, '# form-searchbar > div.searchbar-operate-box > input') #Aliexpress
    search_button = chrome_driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.sticky.top-0.z-20.h-\\[10\\.4rem\\].md\\:h-\\[11\\.6rem\\].transition-all.duration-200.ease-in-out > header > div.relative.flex.items-center.justify-between.w-full.px-6.py-4.md\\:px-7.md\\:py-5 > div.flex.items-center.justify-end.md\\:h-\\[3\\.2rem\\].w-full > div.hidden.md\\:mr-4.lg\\:mr-6.md\\:w-full.md\\:block > form > div.flex.items-center.bg-white.text-black.pl-6.rounded-2.overflow-hidden > button:nth-child(3) > svg')
    search_button.click()

    #content = chrome_driver.find_element(By.ID, "root")
    content = chrome_driver.find_element(By.CLASS_NAME, "grid")
    print(content.text)
    text = content.text
    text = text[:4000]
    text = text.lower()
    bot.send_tg_message(text)
    db.insert_blackmarket_text(title=t, text=text)
    time.sleep(2)
    #chrome_driver.get("https://www.amazon.com/s?k=libros+ciberseguridad&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3PII4RBC1BQVX&sprefix=libros+ciberseguridad%2Caps%2C170&ref=nb_sb_noss_2")
    chrome_driver.get("https://www.backmarket.com/en-us")


print("fin")
chrome_driver.close()
