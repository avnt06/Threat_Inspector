from banner import banner
from api import fetch
from display import display_cve

print(banner)
keyword = input("Enter the keyword for search: ")
need = input("how many results you need: ")
data = fetch(keyword, need)
#csize = len(data["vulnerabilities"])
for vulnerability in data["vulnerabilities"]:
    cve = vulnerability["cve"]
    display_cve(cve)