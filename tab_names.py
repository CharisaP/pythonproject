import time
from selenium import webdriver
from selenium.webdriver.remote.command import Command
import httplib
import socket
import json
driver = webdriver.Firefox()
totalTimes = {}
 #create new firefox window
socialMedia = ['facebook', 'twitter', 'tumblr', 'pinterest']

def main():
	#create function that appends sites to a dictionary
	
	#edit the value for each site key based on time.
	'''
	with open("filename.txt", "w") as output:
		output.write(...)
	'''
	
	total = 0
	init(totalTimes)
	while (get_status(driver) == "Alive"):
		for page in socialMedia:
			temp = ""
			try:
				temp = driver.current_url
			except:
				pass
			with open("charisa_output.txt","w")	as f:
				json.dump(getMediaTime(page, total), f) 
				
		time.sleep(3)	
			
def get_status(driver):
    try:
        driver.execute(Command.STATUS)
        return "Alive"
    except (socket.error, httplib.CannotSendRequest):
        return "Dead"
def getMediaTime(site, total):
	end = 0
	start = 0
	
	
	temp = ""
	try:
		temp = driver.current_url
	except:
		pass
	if site in temp:
		start = time.time()
		isFacebook = True
		while isFacebook:
			temp = ""
			try:
				temp = driver.current_url
			except:
				pass
			if site in temp:
				pass
			else:
				isFacebook = False
				end = time.time()
		total += end - start
		totalTimes[site] = totalTimes[site] + total
		#print totalTimes
	else:
	
		pass

	return totalTimes
def init(total_times):
	for i in socialMedia:
		totalTimes[i] = 0.0
	
if __name__ == "__main__":
	main()
    
