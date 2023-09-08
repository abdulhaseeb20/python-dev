import pyshorteners

long_url = input("Enter url to shorten: ")
inialize = pyshorteners.Shortener()
short_url = inialize.tinyurl.short(long_url)
print("The shortened url is : ", short_url)
