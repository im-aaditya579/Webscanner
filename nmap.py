import os

try:
    def get_nmap(options, ip):
        cmd = "nmap " + options + " " + ip
        process = os.popen(cmd)
        results = str(process.read())
        return results
except:
    print("error in nmap")

#print(get_nmap('-F','162.241.216.11'))