# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(day, month, year, hour, minute, timestamp)

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_date)

# 3. Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")

print(date_object)

# 4. Calculate the time difference between now and new year.
now = datetime.now()
new_year = datetime(year=now.year + 1, month=1, day=1)

time_to_new_year = new_year - now
print(time_to_new_year)

# 5. Calculate the time difference between 1 January 1970 and now.
start_date = datetime(1970, 1, 1)
current_date = datetime.now()

difference = current_date - start_date
print(difference)

# 6. Think, what can you use the datetime module for? Examples:
# Time series analysis
datetime.now()

# To get a timestamp of any activities in an application
series_analysis = datetime.now().timestamp()

# Adding posts on a blog
post_date = datetime.now().strftime("%Y-%m-%d %H:%M")