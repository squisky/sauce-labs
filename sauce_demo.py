from selenium import webdriver

sauce_url = "http://username:access_key@ondemand.saucelabs.com:80/wd/hub"

desired_capabilities = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
}

driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=sauce_url)
driver.implicitly_wait(10)

driver.get('http://www.website.com')
assert "title" in driver.title
driver.quit()