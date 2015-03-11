from datetime import datetime, timedelta # more attractive import
now = datetime.now()
delta = timedelta(31) # create a timedelta of 31 days
#date = now.strftime("%d")
delivery = now + delta # add the timedelta to the current datetime
print("Today: %s" % now.strftime("%d"))
print("Delivery: %s" % delivery.strftime("%d"))
