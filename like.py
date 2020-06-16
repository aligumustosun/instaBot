from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By   
WebDriverWait = webdriver.support.wait.WebDriverWait

import time
def likePosts(driver,tag, likeCount, comment):
  usernames = []
  postText = "https://www.instagram.com/explore/tags/"
  usernameXPath = "/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div/a"
  customPostText = postText + tag
  driver.get(customPostText)
  post = driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div[1]/div/div/div[1]/div[1]")
  post.click()
  likeButtonXPath = "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button"
  nextPostButtonClassName = "coreSpriteRightPaginationArrow"
  commentTextXPath = "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea"
  for x in range(likeCount):
    username = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, usernameXPath)))
    usernames.append(username.text)
    if(comment != ""):
      WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, commentTextXPath))).click()
      commentInput = driver.find_element_by_xpath(commentTextXPath)
      commentInput.send_keys(comment)
      commentInput.send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, likeButtonXPath))).click()
    time.sleep(1)
    if(x!=likeCount-1):
      WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, nextPostButtonClassName))).click()    
  return usernames


