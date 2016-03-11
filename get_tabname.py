import time
from selenium import webdriver
driver = webdriver.Firefox() #create new firefox window

#redirect std out to python script which tells if a social media page (facebook, twitter, tumblr pintrest)

def isSocialMedia():
	while(driver!=None):
		if 'facebook' in driver.current_url:
			print "You're on the wrong page!"
		time.sleep(5)
		if driver == None:
			exit()
		print driver.current_url
		
	

if __name__ == "__main__":
	isSocialMedia()
    
