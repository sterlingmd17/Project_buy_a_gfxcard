from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os


#email info for sending email notification
#EMAIL_ADDRESS = os.environ.get('sXXXXXXXXXXXXX')
#EMAIL_PASSWORD = os.environ.get('passsword')
#with smtplib.smtp('smtp.gmail.com', 587) as smtp:
#    smtp.ehlo()
#    smtp.starttls()
#    smtp.ehlo()
#    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#    subject = 'bot ORDER'
#    body = 'Order succesfully placed with BOT'
#    msg = f'subject: {subject}\n\n{body}'

# User info here, make sure its within the ""
email = "*************"
password = "******"
security_code = "*******************"

url = "https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203080"
#url = "https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002"
#driver.get(url)


def do_the_thing():
    driver = webdriver.Chrome()
    driver.get(url)
    try:

        foundButton = False
        attempt = 0
        while not foundButton:

            attempt+=1

            print("tries " + str(attempt))
            
            addtocartbutton = addbutton = driver.find_element_by_class_name("add-to-cart-button")

            if ('btn-disabled' in addtocartbutton.get_attribute('class')):
                print("Still no add to cart")
                time.sleep(4)
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
        driver.find_element_by_xpath("//button[@class = 'btn btn-lg btn-block btn-primary button__fast-track']").click()
        print("Order has been placed!")
        driver.close()


    except Exception as ex:
        print("Purchase failed, im sorry")
        print(ex)
        driver.close()
        do_the_thing()


if __name__ == '__main__':
    do_the_thing()






