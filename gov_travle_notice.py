# -*- coding: UTF-8 -*-
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')
import json
import requests
import re
from bs4 import BeautifulSoup

boca_gov_html = requests.get('http://www.boca.gov.tw/lp.asp?ctNode=754&CtUnit=32&BaseDSD=13&mp=1')
data = {}
# ISO_code_html.encoding = 'gb18030'
# print (ISO_code_html.encoding)


boca_soup = BeautifulSoup(boca_gov_html.text, "html.parser") #get text content of the website
boca_table = boca_soup.find("div", attrs={"class": "content_box"}) #find the data table

country_name_content = boca_table.find_all('a')
notice_content = boca_table.find_all('strong')
collection_country_event = boca_table.find_all('li')
for c in collection_country_event:
	if c.find('strong') :				#make sure the notice isn't missing
		if not "-" in c.find('a').text:	#filter borders' notice
			country_name = " ".join(re.findall("[a-zA-Z]+",c.find('a').text))
			notice = c.find('strong').text[:1]
			if "灰" in notice:
				notice_num =0
			elif "黃" in notice:
				notice_num =1
			elif "橙" in notice:
				notice_num =2
			elif "紅" in notice:
				notice_num =3
			print country_name, notice_num
			data[country_name]= notice_num


with open('boca_gov_notice.json', 'w') as outfile:
	json.dump(data, outfile, indent=4)
