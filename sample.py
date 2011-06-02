# Sample of code using peekyou_api
from peekyou_api import *

test=peekyou_api()
test.set_key("YOUR API KEY GOES HERE")

#(Optional)In seconds
test.set_frequency(1)

# second parameter for get_url can be xml,json
print test.get_url("http://twitter.com/michaelhussey","json")

