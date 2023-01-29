#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request
    list_if = []
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        list_if.append(type(response.read()))
        list_if.append(response.headers.items()[1][1][20:])
    print("{0}".format("Body response:"))
    print("\t- type: {0}".format(list_if[0]))
    print(f"\t- content: {html}")
    if list_if[1] == 'utf-8':
        print("\t- utf8 content: {0}".format('OK'))
