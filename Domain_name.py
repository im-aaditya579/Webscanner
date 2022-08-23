from tld import get_tld

try:

    def get_domain_name(url):
        domain_name = get_tld(url)
        return domain_name
except:
    print("error in domin")

print(get_domain_name('google.com'))
