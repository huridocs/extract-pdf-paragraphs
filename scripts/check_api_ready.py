import time

import requests

if __name__ == "__main__":
    service_url = "http://localhost:5051/info"

    for i in range(60):
        time.sleep(0.5)
        try:
            response = requests.get(service_url)
            if response.status_code == 200:
                print("ready!")
                break
        except requests.exceptions.ConnectionError:
            print("not ready, yet")
