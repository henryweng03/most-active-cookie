#!/usr/bin/env python3 

import datetime
import csv
import sys
import argparse

# outputs datetime object from string formatted as YYYY-MM-DD
def stringToDateTime(dateString):
    year = int(dateString[:4])
    month = int(dateString[5:7])
    day = int(dateString[8:])
    return datetime.date(year, month, day)

def isValidDate(dateString):
    if len(dateString) != 10:
        return False
    if dateString[:4].isnumeric() == False:
        return False
    if dateString[5:7].isnumeric() == False or int(dateString[5:7]) >= 13 or int(dateString[5:7]) <= 0:
        return False
    if dateString[8:].isnumeric() == False or int(dateString[8:]) >= 32 or int(dateString[8:]) <= 0:
        return False
    return True

class Cookie:
    def __init__(self, cookieName, date):
        self.cookieName = cookieName
        self.date = date
    
    def __lt__(self, other):
        return self.date < other.date
    
    def __eq__(self, other):
        return self.date == other.date

    def __gt__(self, other):
        return self.date > other.date

def findMostActive(date, cookieLog):
    startIndex = binarySearch(date, 0, len(cookieLog) - 1, cookieLog)
    if startIndex == -1:
        print("The date " + str(date) + " was not found in the cookie log. Please try a different date")
        return None

    # hashmap containing counts of each cookie
    cookieCount = {}

    # iterate through all cookies of same date starting at startindex
    lowerIndex = startIndex
    upperIndex = startIndex + 1
    maxCookies = 0

    while lowerIndex >= 0 and cookieLog[lowerIndex].date == date:
        if cookieLog[lowerIndex].cookieName in cookieCount:
            cookieCount[cookieLog[lowerIndex].cookieName] += 1
            if cookieCount[cookieLog[lowerIndex].cookieName] > maxCookies:
                maxCookies = cookieCount[cookieLog[lowerIndex].cookieName]
        else:
            cookieCount[cookieLog[lowerIndex].cookieName] = 1
            if maxCookies == 0:
                maxCookies = 1
        lowerIndex -= 1
    
    while upperIndex < len(cookieLog) and cookieLog[upperIndex].date == date:
        if cookieLog[upperIndex].cookieName in cookieCount:
            cookieCount[cookieLog[upperIndex].cookieName] += 1
            if cookieCount[cookieLog[upperIndex].cookieName] > maxCookies:
                maxCookies = cookieCount[cookieLog[upperIndex].cookieName]
        else:
            cookieCount[cookieLog[upperIndex].cookieName] = 1
            if maxCookies == 0:
                maxCookies = 1
        upperIndex += 1
    
    # adding the names of the most active cookies to a set
    mostActiveCookies = set()
    for key, value in cookieCount.items():
        if value == maxCookies:
            mostActiveCookies.add(key)
    
    return mostActiveCookies


# cookieLog is sorted list of cookies, lower index = more recent date
def binarySearch(target, lowIndex, highIndex, cookieLog):
    if highIndex >= lowIndex:
        midIndex = int(((lowIndex + highIndex) / 2))
        if cookieLog[midIndex].date == target:
            return midIndex
        if cookieLog[midIndex].date < target:
            return binarySearch(target, lowIndex, midIndex - 1, cookieLog)
        else:
            return binarySearch(target, midIndex + 1, highIndex, cookieLog)
    return -1

def isValidFile(filename):
    return filename[-4:] == ".csv"

def main():
    parser = argparse.ArgumentParser(description="find most active cookie")
    parser.add_argument("filename", type=str, help="cookie log CSV file name")
    parser.add_argument("-d", "--date", type=str, help="date to find most active cookie formatted in YYYY-MM-DD")
    args = parser.parse_args()

    if(isValidFile(args.filename)):
        filename = args.filename
    else:
        print("File type must be a CSV. Please enter a file with the extension .csv")
        sys.exit(1)

    if(isValidDate(args.date)):
        date = stringToDateTime(args.date)
    else:
        print("Invalid date entered. Please enter a date in the format YYYY-MM-DD")
        sys.exit(1)

    # reading CSV file
    cookieLog = []
    try:
        with open(filename, 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            for cookie in csvreader:
                cookieLog.append(Cookie(cookie[0], stringToDateTime(cookie[1][:10])))
    except:
        print(filename + " not found. Please try a different filename for the cookie log CSV file")
        sys.exit(1)

    for val in findMostActive(date, cookieLog):
        print(val)

if __name__ == '__main__':
    main()