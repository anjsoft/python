import xml.dom.minidom
import urllib
name = "baidufff22.com"
text = urllib.urlopen("http://panda.www.net.cn/cgi-bin/check.cgi?area_domain="+name)
# req = urllib.urlopen("http://whois.chinaz.com/"+name)
text = text.read().decode("gb2312").encode("utf-8")
text = text.replace(" encoding=\"gb2312\"?>"," encoding=\"utf-8\"?>")
print text
doc = xml.dom.minidom.parseString(text)
res= doc.getElementsByTagName("original")[0].firstChild.data
print  res
print res[:3]
if res[:3]=='210':
    print name+' ok'