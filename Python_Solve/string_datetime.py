from datetime import datetime

date_string = "Aug 6 2025 1:03PM"

# strptime----str to datetime
# strftime----datetime to str

date_time = datetime.strptime(date_string,"%b %d %Y %I:%M%p")
print(date_time)
print(type(date_time))
date_new = datetime.strftime(date_time,"%b %d %Y %I:%M%p")
print(date_new)
print(type(date_new))


# using dateutil & parser(for me flexible method)

from dateutil import parser

# date_string = "Aug 6 2025 1:03PM"
#
# date_timee = parser.parse(date_string)
# print(date_timee)

