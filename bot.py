from selenium import webdriver
import chromedriver_binary
from pathlib import Path
from like import likePosts
from message import sendMessage
from random import choice

commentsPath = 'comments.txt'
messagesPath = 'messages.txt'
tagsPath = 'tags.txt'

with open(commentsPath, encoding="utf8") as f:
    comments = [line.rstrip() for line in f]
print(comments)       
       
with open(messagesPath, encoding="utf8") as f:
    messages = [line.rstrip() for line in f]
print(messages)  

with open(tagsPath, encoding="utf8") as f:
    tags = [line.rstrip() for line in f]
print(tags)  


home = str(Path.home())
chromeOptions = webdriver.chrome.options.Options()
chromeProfileDir = home + "\\AppData\\Local\\Google\\Chrome\\New User"
print(chromeProfileDir)
chromeOptions.add_argument("user-data-dir="+chromeProfileDir)


driver = webdriver.Chrome(options=chromeOptions)

usernameList = []
comment = ""

for tag in tags:
  usernames = likePosts(driver, tag, 5, choice(comments))
  for username in usernames:
    if(username not in usernameList):
      usernameList.append(username)

print(usernameList)
for name in usernameList:
  sendMessage(driver, name, choice(messages))


