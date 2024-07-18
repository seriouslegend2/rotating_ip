import requests

with open("valid_proxies.txt","r") as f:
    proxies = f.read().split("\n")

sites_all = [""]

counter = 0

for site in sites_all:
    try:
        print(f"using proxy: {proxies[counter]}")
        res = requests.get(site, proxies={"http": proxies[counter],
                                          "https": proxies[counter]})
        print(res.status_code)
        print(res.text)
    except:
        print("failed")
    finally:
        counter+=1
        counter % len(proxies)


