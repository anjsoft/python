from bs4 import BeautifulSoup
import urllib
import time
namelist=[]
def readName():
    with open('five-num-dict.txt','r') as f:
        for line in f:
             namelist.append(line[:-1]+'.com')
        # print(namelist)
def save( name):
    f = open('domain-5-num.txt','a')
    f.write(name+'\n')
    f.close()

def check(name):
    text = urllib.urlopen("http://whois.chinaz.com/"+name)
    print text.read()
    exit(0)
    # text = text.read().decode("gb2312").encode("utf-8")
	# text = text.replace(" encoding=\"gb2312\"?>"," encoding=\"utf-8\"?>")
	# print text
	# doc = xml.dom.minidom.parseString(text)
	# res= doc.getElementsByTagName("original")[0].firstChild.data
	# print  res
	# print res[:3]
	# if res[:3]=='210':
	#     print name+' ok'
	#     save(name)

if __name__ == '__main__':
    # readName()
    # for name in namelist:
    #     check(name)
    check("anjsoft.com")
