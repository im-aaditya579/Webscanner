import os

try:
    def get_sql(url):
        cmd = "cd C:\\Users\\atish\\sqlmap && python sqlmap.py -u " + url + "--batch --banner --passwords --dbs " \
                                                                  "--tables "
        process = os.popen(cmd)
        results = str(process.read())
        return results
except:
    print("error in injection")

#print(get_sql("www.google.com"))