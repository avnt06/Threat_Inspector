import requests
import time


def fetch(keyword, need):
    try:
        start = time.time()
        output = requests.get(
        f"https://services.nvd.nist.gov/rest/json/cves/2.0"
        f"?keywordSearch={keyword}&resultsPerPage={need}"
        )
        output.raise_for_status()
        print("Request took", round(time.time() - start, 2), "sec")
        #print(output.status_code)
        #print(output.text[:500])
        data = output.json()

        return data
    except requests.exceptions.Timeout:
        print("[-] Request timed out.")

    except requests.exceptions.ConnectionError:
        print("[-] Connection error. Check your internet connection.")

    except requests.exceptions.HTTPError:
        print(f"[-] HTTP Error: {output.status_code}")

    except requests.exceptions.JSONDecodeError:
        print("[-] Invalid response received from server.")

    except requests.exceptions.RequestException as e:
        print(f"[-] Request failed: {e}")

    return None