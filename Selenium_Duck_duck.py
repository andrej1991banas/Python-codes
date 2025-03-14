from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

try: 

    opts = Options()
    opts.add_argument("--headless")

    driver = Chrome(options=opts)
    driver.implicitly_wait(5)
    driver.get("https://duckduckgo.com")

    driver.maximize_window()


    search_bar = driver.find_element(By.NAME, "q")
    print(search_bar)
    search_bar.clear()
    search_bar.send_keys("Oveckin")
    # search_bar.send_keys(Keys.RETURN)
    search_bar.submit()

    # If we don't sleep, we don't get the correct window
    time.sleep(2)

    print(driver.current_url)
    driver.get_screenshot_as_file('screenshot.png')

finally:
    driver.quit()
