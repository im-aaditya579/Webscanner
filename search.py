path3 = "C:\\Users\\atish\\PycharmProjects\\WEBSCANNER\\Result\\info\\whois.txt"
with open(path3, "r") as f4:
    str = f4.read()
    c = str.find("Name Server")
    c1 = str.find("DN")
    c=c+15
    c1=c1-4
    f4.seek(c)
    print(f4.read(c1-c))
    d = str.find("Domain ID")
    d1 = str.find("Registrar WHOIS")
    d = d+13
    d1 = d1-4
    f4.seek(d)
    print(f4.read(d1 - d))