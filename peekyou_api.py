#Peekyou class used in a effort for providing ease of use of our
#peekyou api.
import urllib
import re
import time

class peekyou_api:
    api_key=''
    app_id=''
    frequency=5#default frequency in seconds
    api_version=3#set default api version to use
    
 
# Sets the api key.
# @param string key
# @return none
    def set_key(self,key):
        self.api_key=key

# Sets the app id.
# @param string key
# @return none
    def set_app_id(self,id_key):
        self.app_id=id_key

 
# Sets the frequency,
# Controls the rate a user would like to check peekyou api for status
# @param int value
# @return none
    def set_frequency(self,value):
        self.frequency=value


 
# Gets url information from peekyou social audience for a given url(For example http://twitter/[username]
# @param string url
# @param string type (xml,json)
# @return string representing json,or xml
    def get_social_audience_info(self,url,type):
       
        type=str.strip(str.lower(type))
        
        if(type!="json" and type!="xml"):
            return "Invalid type!!"
	    
        url="http://api.peekyou.com/analytics.php?key="+self.api_key+"&url="+url+"&output="+type+"&app_id="+self.app_id
	
        result=self.check_status(url,type)
        while(result==-1):
            time.sleep(self.frequency)
            result=self.check_status(url,type)
	
        return result

# Gets url information from peekyou social consumer api for a given url(For example http://twitter/[username]
# @param string url
# @param string type (xml,json)
# @return string representing json,or xml
    def get_social_consumer_info(self,url,type):
       
        type=str.strip(str.lower(type))
        
        if(type!="json" and type!="xml"):
            return "Invalid type!!"
	    
        url="http://api.peekyou.com/api.php?key="+self.api_key+"&url="+url+"&apiv="+str(self.api_version)+"&output="+type+"&app_id="+self.app_id
	
        result=self.check_status(url,type)
        while(result==-1):
            time.sleep(self.frequency)
            result=self.check_status(url,type)
	
        return result

 
# Checks the status return by peekyou api.
# @param string url
# @param string type
# @return If status is 1 then -1 is return implying search is still 
# active on peekyou,otherwise any other status results is returned.
    def check_status(self,url,type):
        result=self.read_url(url)
       
        if(type=="json"):
	    #you can replace this part with your own json decoder object to get value
	    #of status rather than using regexp match
            reg_pat = re.compile('"status":(.*?),')
            status=reg_pat.search(result)
        else:
	    #you can replace this part with your own xml parser to get value
	    #of status rather than using regexp match
	    reg_pat = re.compile('<status>(.*?)<\/status>')
            status=reg_pat.search(result)
        if(not result):
            return "API down. Try again later"
        elif(status.group(1)=='1'):
	    return -1
        else: 
	    return result
	

# Returns html from url link
# @param string url
# @return string containing html from url location.
    def read_url(self,url):
        results=urllib.urlopen(url)
        return results.read()



