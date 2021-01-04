from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os


# User info for best buy account login, make sure its within the ""
email = "Your email here"
password = "password"
security_code = "000"

#Desired product URL, Make sure within the "":
url = "https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6436191.p?skuId=6436191"



def do_the_thing():
    driver = webdriver.Chrome()
    driver.get(url)
    try:

        foundButton = False

        while not foundButton:
            
            addtocartbutton = addbutton = driver.find_element_by_class_name("add-to-cart-button")

            if ('btn-disabled' in addtocartbutton.get_attribute('class')):
                print("Still no add to cart")
                time.sleep(3)
                driver.refresh()
                addtocartbutton = addbutton = driver.find_element_by_class_name("add-to-cart-button")
            else:
                foundButton = True

        addtocartbutton.click()
        print("Item added to cart")
        driver.implicitly_wait(10)
        driver.find_element_by_class_name("go-to-cart-button").click()
        driver.implicitly_wait(2)
        driver.find_element_by_xpath("//button[@class = 'btn btn-lg btn-block btn-primary' and @data-track= 'Checkout - Top']").click()
        print("checkout button clicked")
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//input[@name='fld-e']").send_keys(email)
        driver.find_element_by_xpath("//input[@name='fld-p1']").send_keys(password)
        driver.find_element_by_xpath("//button[@type = 'submit' and @data-track = 'Sign In']").click()
        driver.implicitly_wait(2)
        driver.find_element_by_xpath("//a[@class='ispu-card__switch']").click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath("//input[@type='tel' and @id='credit-card-cvv']").send_keys(security_code)
        place_order_test = driver.find_element_by_xpath("//button[@class = 'btn btn-lg btn-block btn-primary button__fast-track']")
        print("Order has been placed!")


    except Exception as ex:
        print("Purchase failed, im sorry")
        print(ex)


if __name__ == '__main__':
    do_the_thing()


# Work in progress for email notification, not sure if it'll be a thing.
#email info for sending email notification
#EMAIL_ADDRESS = os.environ.get('emailaddress')
#EMAIL_PASSWORD = os.environ.get('app_password')
#with smtplib.smtp('smtp.gmail.com', 587) as smtp:
#    smtp.ehlo()
#    smtp.starttls()
#    smtp.ehlo()
#    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#    subject = 'bot ORDER'
#    body = 'Order succesfully placed with BOT'
#    msg = f'subject: {subject}\n\n{body}'


