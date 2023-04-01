# Test Case

# 1-) Open Web Browser (Chrome/firefox/Edge)
# 2-) Open URL https://opensource-demo.orangehrmlive.com/
# 3-) Enter username (Admin)
# 4-) Enter password (admin123)
# 5-) Click on Login
# 6-) Capture title of the home page. (Actual title)
# 7-) Verify title of the page: OrangeHRM  (Expected)
# 8-) Close browser

# bu adımları otomatikleştirmek isterseniz ilk ve en önemli adım
# web sürücü modülünü içe aktarmamız gerektiğidir

from selenium import webdriver

# #Selenium3
# # 1-) Open Web Browser (Chrome/firefox/Edge)
# #driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver=webdriver.Chrome()
# # tarayıcımızı otomatik olarak başlatacak bu chrome sınıfı oluşturucu sürücüyü kullanacak
# # ve tarayıcıyı yeniden başlatacak
# # 2-) Open URL https://opensource-demo.orangehrmlive.com/
# driver.get("https://opensource-demo.orangehrmlive.com/")
# # 3-) Enter username (Admin)
# driver.find_element_by_name("username").send_keys("Admin")
# # 4-) Enter password (admin123)
# driver.find_element_by_id("password").send_keys("admin123")
# # 5-) Click on Login
# driver.find_element_by_class_name("oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
# # 6-) Capture title of the home page. (Actual title)
# actual_title = driver.title
# expected_title = "OrangeHRM"
# # 7-) Verify title of the page: OrangeHRM  (Expected)
# if actual_title == expected_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
# # 8-) Close browser
# driver.close()

#Selenium4
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# 1-) Open Web Browser (Chrome/firefox/Edge)
driver=webdriver.Chrome(service=serv_object)

# # 2-) Open URL https://opensource-demo.orangehrmlive.com/
driver.get("https://opensource-demo.orangehrmlive.com/")
# # 3-) Enter username (Admin)
#driver.find_element(By.NAME,"username").send_keys("Admin")
# # 4-) Enter password (admin123)
#driver.find_element(By.ID,"password").send_keys("admin123")
# # 5-) Click on Login
#driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
# # 6-) Capture title of the home page. (Actual title)
#actual_title = driver.title
#expected_title = "OrangeHRM"
# # 7-) Verify title of the page: OrangeHRM  (Expected)
#if actual_title == expected_title:
#    print("Login Test Passed")
#else:
#    print("Login Test Failed")
# # 8-) Close browser
#driver.close()