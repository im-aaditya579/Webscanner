import os
import whois

try:
    def get_ip_address(url):
        cmd = "ping " + url
        process = os.popen(cmd)
        results = str(process.read())
        split = results.find('statistics for') + 15
        split = results[split:].splitlines()[0]
        return split[:-1]
except:
    print("error in ip")

#print(get_ip_address('google.com'))
