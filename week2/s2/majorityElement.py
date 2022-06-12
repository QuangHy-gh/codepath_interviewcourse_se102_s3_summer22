def majorityElement(eList):
    leastMajority = len(eList) / 2
    elementFreq = {}
    for i in range(len(eList)):
        if eList[i] in elementFreq:
            elementFreq[eList[i]] += 1
        else:
            elementFreq[eList[i]] = 1
    for freqKey, freqVal in elementFreq.items():
        if freqVal > leastMajority:
            return freqKey
    return -1


print("majority element")
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
print(majorityElement([2, 2, 1, 1, 1, 2]))
