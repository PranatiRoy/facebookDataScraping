cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
import time
import pandas as pd
from bs4 import BeautifulSoup # for the beautiful soup we have to send the source code for the page.
from selenium import webdriver
browser=webdriver.Chrome(cd)
browser.get("https://www.facebook.com/login")
un=browser.find_element_by_xpath('//input[@id="email"]') #locate the element and click
un.send_keys("09903350540") #send input to that
passwrd=browser.find_element_by_xpath('//input[@id="pass"]')
passwrd.send_keys("jhal@char")
sign_in=browser.find_element_by_xpath('//button[@id="loginbutton"]')
sign_in.click( )


time.sleep(10)


browser.get("https://www.facebook.com/pronoti.maity.9/friends")

time.sleep(4)

total_friends= (browser.find_element_by_xpath('//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh sq6gx45u j5wam9gi knj5qynh q66pz984"]')).text
total_friends=int(total_friends)

i=0

while (i<total_friends):
	time.sleep(1)
	pgsource=browser.page_source # return the source code
	ref=BeautifulSoup(pgsource,'html.parser') #it refers to the soup element /translated element
	selection_all=ref.findAll('div',{'class':"bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr"})
	i=len(selection_all)
	browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	time.sleep(0.1)
	browser.execute_script('window.scrollTo(0,0);')
	time.sleep(0.1)
	
print(len(selection_all))

url_list=[]
name_list=[]

for i in selection_all:
	r=i.find('span',{'class':"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb mdeji52x jagab5yi g1cxx5fr lrazzd5p oo9gr5id"})
	try:
		n=r.text
		name_list.append(n)
	except:
		name_list.append("nothing found")
		pass	
	
	q=i.find('a',{'class':"oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8"})
	try:
		profile_link=q.get('href')
		url_list.append(profile_link)
	except:
		url_list.append("nothing found")
		pass	
	



dict1={'Name':name_list,'Profile_Link_url':url_list}
df=pd.DataFrame(dict1)
df.to_csv("C:\\Users\\Pranati\\facebook_database.csv")

print("Done")

