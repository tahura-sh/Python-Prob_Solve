import calendar

year =int(input("enter a year :"))
month =int(input("enter a month :"))

month_show = calendar.month(year,month)
print(month_show)
