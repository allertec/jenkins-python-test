from datetime import date
import distro
import platform
import sys


today = date.today()
# European date format - day/month/year :)
eu_date_format = today.strftime("%d/%m/%Y")
print("Today is: ", eu_date_format)

get_os_platform = platform.system()
if get_os_platform == "Darwin":
  os_name = "MacOS"
  os_version = platform.mac_ver()[0]
elif get_os_platform == "Windows":
  os_name = get_os_platform
  os_version = platform.release()
elif get_os_platform == "Linux":
  os_name = distro.name()
  os_version = distro.version()


file = open("artifact", "x")
file.write("You are running on: " + os_name + os_version)
file.close()
