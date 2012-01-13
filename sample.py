# Sample of code using peekyou_api
from peekyou_api import *

test=peekyou_api()
test.set_key("YOUR API KEY GOES HERE")
test.set_app_id("YOUR APP ID GOES HERE");

#(Optional)In seconds
test.set_frequency(1)

# second parameter for get_url can be xml,json
print test.get_social_audience_info("http://twitter.com/michaelhussey","json")
print test.get_social_consumer_info("http://twitter.com/michaelhussey","json")

