from banner import banner
from api import fetch
from display import display_cve

print(banner)
keyword = input("Enter the keyword for search: ")
while True:
    try:
        need = int(input("Enter a number greater than zero: "))
        if number <= 0:
            print("Error: The number must be greater than zero. Try again.")
            continue
        break 
        
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
data = fetch(keyword, need)
if data is None:
    exit()

if data["totalResults"] == 0:
    print("\n[-] No vulnerabilities found.")
    exit()


#csize = len(data["vulnerabilities"])
for vulnerability in data["vulnerabilities"]:
    cve = vulnerability["cve"]
    display_cve(cve)