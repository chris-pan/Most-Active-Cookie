import sys
import os.path

# Read file and create cookies log for only the given date.
def createCookiesLog(filename, date):
    seenDate = False
    passedDate = False
    # Since input is sorted by timestamp, return cookies log once
    # we have seen all cookies seen on given date

    cookies = {}
    f = open(filename, "r")
    for line in f.readlines():
        l = line.split(",")
        d = l[1].split("T")[0]
        if d == date:
            seenDate = True
            c = l[0]
            if c in cookies:
                cookies[c] += 1
            else:
                cookies[c] = 1
        elif seenDate:
            passedDate = True
        if passedDate:
            break
    f.close()
    
    return cookies

# Return list of all cookies that have been seen the most
def getMostActiveCookies(cookies):
    maxSeen = max(cookies.values())
    mostActiveCookies = []

    for c in cookies:
        if cookies[c] == maxSeen:
            mostActiveCookies.append(c)

    return mostActiveCookies

def main():
    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise FileNotFoundError(filename +  " not found.")

    date = sys.argv[3]

    cookies = createCookiesLog(filename, date)

    mostActiveCookies = getMostActiveCookies(cookies)
    
    for cookie in mostActiveCookies:
        print(cookie)

if __name__ == "__main__":
    main()