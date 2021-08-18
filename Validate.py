import validators

with open('urls.txt') as f:
    lines = f.readlines()

for line in lines:
    url  = line.strip()
    if validators.url(url):
        print("valid url: {}".format(url))
    else:
        print("invalid url: {}".format(url))