def romanToInt(romanStr):
    romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    strLength = len(romanStr)
    num = romanDict[romanStr[strLength - 1]]
    for i in range(strLength - 2, -1, -1):
        if romanDict[romanStr[i]] >= romanDict[romanStr[i + 1]]:
            num += romanDict[romanStr[i]]
        else:
            num -= romanDict[romanStr[i]]
    return num


print("\n\nroman to integer")
print(romanToInt("III"))  # 3
print(romanToInt("LVIII"))  # 58
print(romanToInt("MCMXCIV"))  # 1994
