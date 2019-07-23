"""
    This Object models the payment page.
"""

import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import time
from .Base_Page import Base_Page
#from page_objects.Cart_Page import Cart_Page

class Payment_Object(Base_Page):


    #Locators
    PAY_WITH_CARD = locators.PAY_WITH_CARD
    PAY_WITH_CARD_TITTLE = locators.PAY_WITH_CARD_TITTLE
    EMAIL =  locators.EMAIL
    CARD_NUMBER = locators.CARD_NUMBER
    EXPIRY_DATE = locators.EXPIRY_DATE
    CVC_NUMBER  = locators.CVC_NUMBER
    ZIPCODE =  locators.ZIPCODE
    CHECKBOX_TICK = locators.CHECKBOX_TICK
    MOBILE_NUMBER = locators.MOBILE_NUMBER
    SUBMIT_BUTTON = locators.SUBMIT_BUTTON
    PAYMENT_SUCESS_TITTLE = locators.PAYMENT_SUCESS_TITTLE
    IFRAME_NAME= locators.IFRAME_NAME


    def go_to_payment_frame(self):
        result_flag = self.click_payment_button()
        time.sleep(10)

        result_flag &= self.switch_to_frame()
        time.sleep(10)
        #result_flag = self.verify_frame()   
        return result_flag

    @Wrapit._screenshot
    def click_payment_button(self):
        "Click Payment button"
        result_flag = self.click_element(self.PAY_WITH_CARD)
        self.conditional_write(result_flag,
        positive="Clicked on the Pay with card button",
        negative="Could not click on the button")
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def switch_to_frame(self):
        "Switch to frame"
        #time.sleep(5)
        result_flag = self.switch_frame(self.IFRAME_NAME)
        time.sleep(5)
        return result_flag 
        

    @Wrapit._screenshot
    def verify_frame(self):
        "Verify automation is on the frame"
        result_flag = self.smart_wait(5,self.PAY_WITH_CARD_TITTLE) #pylint: disable=no-member
        self.conditional_write(result_flag,
        positive="Automation is on the Frame",
        negative="Automation is not able to locate the Frame Title.")
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_email_field(self,email_field):
        "set email on the iframe"
        result_flag = self.set_text(self.EMAIL,email_field)
        self.conditional_write(result_flag,
        positive='Set the email to: %s'%email_field,
        negative='Failed to set email',
        level='debug')
        return result_flag


    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_expiry_date(self,expiry_date):
        "set expiry date on the iframe"
        result_flag = self.set_text(self.EXPIRY_DATE,expiry_date)
        self.conditional_write(result_flag,
        positive='Set the expiry date to: %s'%expiry_date,
        negative='Failed to expiry date number',
        level='debug')
        return result_flag 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_card_number(self,card_number):
        "set email on the iframe"
        result_flag = self.set_text(self.CARD_NUMBER,card_number)
        self.conditional_write(result_flag,
        positive='Set the card number to: %s'%card_number,
        negative='Failed to set card number',
        level='debug')
        return result_flag   

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_cvc_number(self,cvc_number):
        "set CVC number on the iframe"
        result_flag = self.set_text(self.CVC_NUMBER,cvc_number)
        self.conditional_write(result_flag,
        positive='Set the cvc_number to: %s'%cvc_number,
        negative='Failed to set cvc_number',
        level='debug')
        return result_flag   
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_zip_code(self,zip_code):
        "set zip code on the iframe"
        time.sleep(3)
        result_flag = self.set_text(self.ZIPCODE,zip_code)
        self.conditional_write(result_flag,
        positive='Set the zip_code to: %s'%zip_code,
        negative='Failed to set zip_code',
        level='debug')
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_mobile_number(self,mobile_number):
        "set mobile_number on the iframe"
        result_flag = self.set_text(self.MOBILE_NUMBER,mobile_number)
        self.conditional_write(result_flag,
        positive='Set the mobile_number to: %s'%mobile_number,
        negative='Failed to set mobile_number',
        level='debug')
        return result_flag 





    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_checkbox(self):
        "check checkbox on the iframe"
        result_flag = self.click_element(self.CHECKBOX_TICK)
        self.conditional_write(result_flag,
        positive='clicked the checkbox',
        negative='Failed to click checkbox',
        level='debug')
        return result_flag
    

      
    

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_submit(self):
        "Submit button on the iframe"
        result_flag = self.click_element(self.SUBMIT_BUTTON)
        self.conditional_write(result_flag,
        positive='clicked the submit button',
        negative='Failed to click submit buton',
        level='debug')
        return result_flag



    def populate_frame(self,email_field,card_number,expiry_date,cvc_number,zip_code,mobile_number):
        "Enter the details"
        result_flag =self.set_email_field(email_field)
        result_flag &=self.set_card_number(card_number)
        result_flag &=self.set_expiry_date(expiry_date)
        result_flag &=self.set_cvc_number(cvc_number)
        result_flag &=self.set_zip_code(zip_code)
        #result_flag &=self.click_checkbox()
        #result_flag &=self.set_mobile_number(mobile_number)
        result_flag &=self.click_submit()
    
        return result_flag