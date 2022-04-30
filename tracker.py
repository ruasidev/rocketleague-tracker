from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

search_input = '/html/body/div/div[2]/div[2]/div/main/div[3]/div/div[1]/div/div/div[1]/div[2]/div[1]/form/input'
ones_mmr = '/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div'
ones_rank = '/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div[2]'
twos_mmr = '/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[3]/div/div[2]/div[1]/div'
twos_rank = '/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[2]/div[2]'
threes_mmr = '/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[3]/div/div[2]/div[1]/div'
threes_rank = '/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/div[2]'
extra_mmr = '/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[3]/div/div[2]/div[1]/div'
extra_rank = '/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/div[2]'
user = input("Enter the EPIC ID of the target user: ")


geckodriver = r'geckodriver.exe'
headOption = webdriver.FirefoxOptions()
headOption.add_argument("--headless")
driver = webdriver.Firefox(options=headOption)
driver.get('https://rocketleague.tracker.network/')
try:
    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, search_input))
    )
finally:
    pass

search_button.send_keys(user)
search_button.send_keys(Keys.ENTER)

try:
    ones_mmr = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH , ones_mmr))
    )
finally:
    pass

ones_mmr = ones_mmr.get_attribute('innerHTML')
ones_rank = driver.find_element(By.XPATH, ones_rank).get_attribute('innerHTML')
twos_mmr = driver.find_element(By.XPATH, twos_mmr).get_attribute('innerHTML')
twos_rank = driver.find_element(By.XPATH, twos_rank).get_attribute('innerHTML')
threes_mmr = driver.find_element(By.XPATH, threes_mmr).get_attribute('innerHTML')
threes_rank = driver.find_element(By.XPATH, threes_rank).get_attribute('innerHTML')

if ones_rank[0] == "U":
    ones_mmr = driver.find_element(By.XPATH, twos_mmr).get_attribute('innerHTML')
    ones_rank = driver.find_element(By.XPATH, twos_rank).get_attribute('innerHTML')
    twos_mmr = driver.find_element(By.XPATH, threes_mmr).get_attribute('innerHTML')
    twos_rank = driver.find_element(By.XPATH, threes_rank).get_attribute('innerHTML')
    threes_mmr = driver.find_element(By.XPATH, extra_mmr).get_attribute('innerHTML')
    threes_rank = driver.find_element(By.XPATH, extra_rank).get_attribute('innerHTML')

print("1s: ", ones_rank, "("+ones_mmr, "mmr)")
print("2s: ", twos_rank, "("+twos_mmr, "mmr)")
print("3s: ", threes_rank, "("+threes_mmr, "mmr)")

# driver.save_screenshot(r'C:\Users\Ruasi\OneDrive\Desktop\programming\discord-spammer\spammer-firefox\headless_test.png')
driver.quit()