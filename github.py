from githubUserInnfo import username, password
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
        
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        
        self.browser.find_element(By.XPATH,"//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.password)
        
        time.sleep(1)
        
        sign_in = self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[13]")
        sign_in.click()
    
    def loadFollowers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR,"div.d-table")
        
        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR,"span.Link--secondary").text)
       
    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        self.loadFollowers() 
        
        # If you have a lot of followers, you can access all follower names by activating the next button.   
        while True:
            links = self.browser.find_element(By.CSS_SELECTOR, "div.pagination").find_elements(By.TAG_NAME,"a")
            
            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()
                    
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        self.loadFollowers()   
                    else:
                        continue
        
github = Github(username, password)
github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)
        