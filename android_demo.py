from sauceclient import SauceClient
from selenium import webdriver

sauce_url = "http://username:access_key@ondemand.saucelabs.com:80/wd/hub"

desired_capabilities = {
    'platform': "Linux",
    'browserName': "android",
    'version': "4.4",
    'deviceName': "Samsung Galaxy S4 Emulator",
    'device-orientation': "portrait"
}

driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=sauce_url)
driver.implicitly_wait(10)

driver.get('http://www.website.com')
assert "Title" in driver.title
driver.quit()

sauce_client = SauceClient("username", "access_key")

sauce_client.jobs.update_job(driver.session_id, passed=True)
