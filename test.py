import time
from selenium import webdriver
driver = webdriver.Firefox() #create new firefox window

#redirect std out to python script which tells if a social media page (facebook, twitter, tumblr pintrest)

def isSocialMedia():

	start = time.time()
	totalTime = 0
	tempTime = 0
	wrongPage = False
	FBstarting = time.time()
	TWTstarting = time.time()
	TBLRstarting = time.time()
	PINstarting = time.time()
	YTstarting = time.time()
		
	while(True):
		if ('facebook' or 'twitter'or 'youtube') in driver.current_url:
			start = time.time()
			wrongPage = True
			print "You're on the wrong page!"
		else:
			wrongPage = False
			totalTime += time.time() - start
			
		time.sleep(5)
		
		print driver.current_url
		print totalTime
	

if __name__ == "__main__":
	isSocialMedia()
    
    
    
    
    #use driver.switch_to.window('localhost') ?? 
    #use .close to close any social media websites? c
    	#twitter, tumblr, youtube, reddit
    	#if on page for more than 3 minutes, send message. 
    	
