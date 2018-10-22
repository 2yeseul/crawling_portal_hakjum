# C:\Users\vdiuser\Downloads\chromedriver_win32
from selenium import webdriver

driver = webdriver.Chrome('C:\chromedriver.exe')
driver.implicitly_wait(5)

driver.get('https://acm.sungshin.ac.kr/proweb/index1280.jsp')
#driver.switch_to_frame('body_Frame')
#driver.switch_to_frame(driver.find_element_by_tag_name('body_frame'))
#print('enter the id and pw')
#user_id = input()
#user_pw = input()
#driver.find_element_by_xpath('//*[@id="saveId"]').click()
driver.find_element_by_name('userId').send_keys('20152917')
driver.find_element_by_name('passwd').send_keys('skdisk17~')

driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td[3]/table/tbody/tr[2]/td[5]/img').click()
#driver.find_element_by_xpath('//*[@id="homeLink"]').click()

driver.switch_to_frame('leftFrame')
driver.find_element_by_xpath('//*[@id="parent2_3"]').click()
#driver.switch_to_frame('session_frame')
#driver.switch_to_frame('receiver_frame')
#receiver_frame

driver.find_element_by_xpath('//*[@id="subMenu21"]').click()