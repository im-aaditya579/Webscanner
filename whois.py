import bane
import json

try:
    def get_whois(url):
        res = bane.whois(url)
        result = json.dumps(res)
        return result

except:
    print("error in whois")

#print(bane.udp_flood('162.241.216.11', p=25 , min_size=10, max_size=20 , duration= 300 , interval=0.001))
#res = (bane.path_traversal_urls('https://computer-database.gatling.io/computers', timeout=15 ))
#print(res)
