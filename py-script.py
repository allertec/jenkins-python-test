from datetime import date
import platform
import os
import sys


today = date.today()
# European date format - day/month/year :)
eu_date_format = today.strftime("%d/%m/%Y")
print("Today is: ", eu_date_format)
