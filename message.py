from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By   
WebDriverWait = webdriver.support.wait.WebDriverWait
import time

sendNewMessageLink = "https://www.instagram.com/direct/new/"
usernameXPath = "/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input"

#firstUserXPath = "//*[@id=\"f2e5685c134c6c\"]/div"
firstUserXPath = "/html/body/div[2]/div/div/div[2]/div[2]/div/div"
usersClassname = "-qQT3"
nextButtonXPath = "/html/body/div[2]/div/div/div[1]/div/div[2]/div"
messageTextAreaXPath = "//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea"

def sendMessage(driver, username, message):
  driver.get(sendNewMessageLink)
  time.sleep(1)
  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, usernameXPath))).click()
  usernameInput = driver.find_element_by_xpath(usernameXPath)
  usernameInput.send_keys(username)
  usernameInput.send_keys(Keys.ENTER)
  time.sleep(1)
  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, firstUserXPath))).click()
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, nextButtonXPath))).click()
  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, messageTextAreaXPath))).click()
  messageTextInput = driver.find_element_by_xpath(messageTextAreaXPath)
  messageTextInput.send_keys(message)
  messageTextInput.send_keys(Keys.ENTER)



  