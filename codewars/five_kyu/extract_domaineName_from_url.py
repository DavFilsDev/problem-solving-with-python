def domain_name(url):
    return  url.replace("http://","").replace("https://","").replace("www.","").split(".")[0]

print(domain_name("http://github.com/carbonfive/raygun"))  # github
print(domain_name("http://www.zombie-bites.com"))          # zombie-bites
print(domain_name("https://www.cnet.com"))                 # cnet
