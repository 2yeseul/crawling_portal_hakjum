from selenium import webdriver
import  time
# C:\IEDriverServer.exe
driver = webdriver.Ie('C:\IEDriverServer.exe')
driver.implicitly_wait(5)

driver.get('https://acm.sungshin.ac.kr/proweb/index1280.jsp')
driver.find_element_by_xpath('//*[@id="saveId"]').click()
driver.find_element_by_name('userId').send_keys('20152917')
driver.find_element_by_name('passwd').send_keys('skdisk17~')
driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td[3]/table/tbody/tr[2]/td[5]/img').click()
driver.switch_to_frame('leftFrame')
driver.find_element_by_xpath('//*[@id="parent2_3"]').click()
driver.find_element_by_xpath('//*[@id="subMenu21"]').click()
time.sleep(10)
driver.save_screenshot("score.png")
