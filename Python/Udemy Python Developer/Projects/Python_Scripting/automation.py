from selenium import webdriver
#this selemium script goes to the website selenium easy and fills in some text, presses a button and then prints the output of that button
chrome_browser = webdriver.Chrome('./chromedriver') #set our chromedriver
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html') #go to this website
show_message_button = chrome_browser.find_element_by_class_name('btn-default') #find the show message button
print(show_message_button.get_attribute('innerHTML')) #print the inner HTML so we know what the button says

user_message = chrome_browser.find_element_by_id('user-message')#find the field where the user can input text

user_message.clear() #clear text in case someone typed something there
user_message.send_keys('Hello') #with send keys we write something to the field
show_message_button.click() #we click on the show message button
output_message = chrome_browser.find_element_by_id('display') #we grab the output message by its ID
print(output_message.text) #and we print its content with .text