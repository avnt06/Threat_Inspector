import requests
import time


def fetch(keyword, need):
    start = time.time()
    output = requests.get(
        f"https://services.nvd.nist.gov/rest/json/cves/2.0"
        f"?keywordSearch={keyword}&resultsPerPage={need}"
    )
    print("Request took", round(time.time() - start, 2), "sec")
    #print(output.status_code)
    #print(output.text[:500])
    data = output.json()

    return data