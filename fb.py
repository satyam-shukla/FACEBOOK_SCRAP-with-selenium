from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome import options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications":1
})

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
driver.get("https://www.facebook.com/")
driver.maximize_window()

email=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
email.send_keys("s1108kushwaha@gmail.com")
sleep(2)
passw=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
passw.send_keys("satyam123123")
passw.submit()
driver.maximize_window()
sleep(5)
profile=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[4]/a').click()
sleep(20)
friends=driver.find_element_by_xpath('//*[@id="mount_0_0_06"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]')
print(friends.text())
friends.click()
# friends=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[1]/div/a/div[1]/div[2]/div/div/div/div/span/span').click()
# sleep(15)
# fff=driver.find_element_by_xpath("//*[@id='mount_0_0_Xu']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[4]").click()
