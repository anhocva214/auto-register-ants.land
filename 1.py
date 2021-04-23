from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.ants.land/?t=1480015")

driver.implicitly_wait(1)
btn_start = driver.find_element_by_css_selector('#app > div.beginner-page-wrap > div > div.beginner-btns')
btn_start.click()

input_phone = driver.find_element_by_css_selector('#app > div.vh-100.bg-432af5.van-popup.van-popup--bottom > div > div.flex-sub.white-view.border-radius-top-xl.padding-lg.flex.flex-direction.signInUpModel > div:nth-child(5) > div > div > div > input');
input_phone.clear()
input_phone.send_keys("326255339")

input_password = driver.find_element_by_css_selector('#app > div.vh-100.bg-432af5.van-popup.van-popup--bottom > div > div.flex-sub.white-view.border-radius-top-xl.padding-lg.flex.flex-direction.signInUpModel > div:nth-child(7) > div > div > input');
input_password.clear()
input_password.send_keys("122112")

input_password_confirm = driver.find_element_by_css_selector('#app > div.vh-100.bg-432af5.van-popup.van-popup--bottom > div > div.flex-sub.white-view.border-radius-top-xl.padding-lg.flex.flex-direction.signInUpModel > div:nth-child(9) > div > div > input');
input_password_confirm.clear()
input_password_confirm.send_keys("122112")

time.sleep(1)
print("click register")
btn_register = driver.find_element_by_css_selector('#app > div.vh-100.bg-432af5.van-popup.van-popup--bottom > div > div.flex-sub.white-view.border-radius-top-xl.padding-lg.flex.flex-direction.signInUpModel > button.van-button.van-button--default.van-button--large.margin-bottom-sm.border-radius-sm.font-bold.fs-16.custom-btn.breath-btn')
btn_register.click()

# time.sleep(3)
# print("clear localStorage")
# driver.get('javascript:localStorage.clear();')
# driver.get("https://www.ants.land/?t=1480015")


# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

#app > div.vh-100.bg-432af5.van-popup.van-popup--bottom > div > div.flex-sub.white-view.border-radius-top-xl.padding-lg.flex.flex-direction.signInUpModel > button.van-button.van-button--default.van-button--large.margin-bottom-sm.border-radius-sm.font-bold.fs-16.custom-btn.breath-btn