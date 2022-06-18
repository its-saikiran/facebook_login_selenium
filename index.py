
from selenium import webdriver  
from time import sleep
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)  
driver.maximize_window()  
driver.get("https://www.facebook.com/") 
driver.find_element_by_xpath('//*[@id="email"]').send_keys("9870230639")
driver.find_element_by_xpath('//*[@id="pass"]').send_keys("enterpassword")
sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click() 
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[4]").click()
action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[3]')
action.move_to_element(firstLevelMenu).perform()
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[3]').click()
sleep(10)
driver.quit()
