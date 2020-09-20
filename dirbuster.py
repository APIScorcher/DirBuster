import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-u", type=str, dest="url", help="--url (https://url.com)", default=None)
parser.add_argument("-w", type=str, dest="wordlist", help="--wordlist", default=None)

args = parser.parse_args()
url = ""
wordlist = ""

url = args.url
wordlist = args.wordlist

def dirb(url, dict):
    print("""  _____  _      ____            _
 |  __ \(_)    |  _ \          | |
 | |  | |_ _ __| |_) |_   _ ___| |_ ___ _ __
 | |  | | | '__|  _ <| | | / __| __/ _ \ '__|
 | |__| | | |  | |_) | |_| \__ \ ||  __/ |
 |_____/|_|_|  |____/ \__,_|___/\__\___|_|

                                             """)
    try:
        wordlist = open(dict,"rb")
        for path in wordlist.readlines():
            path = path.strip().decode("utf-8")
            urlpath = url+"/"+path
            r = requests.get(urlpath)
            if r.status_code != 404:
                print("{} -> {}".format(r.status_code, urlpath))
    except: # Catching exceptions
        print("Error Occured!")

if __name__ == "__main__":
    dirb(url, wordlist)
