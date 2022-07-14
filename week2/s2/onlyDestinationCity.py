def onlyDCity(paths):
    origins = set()
    destinations = set()
    for path in paths:
        origins.add(path[0])  # first element is origin
        destinations.add(path[1])  # second element is dest.
    for d in destinations:
        if d not in origins:
            return d
    # all destinations have outgoing flights
    return None


def onlyDCity2(paths2):  # using flatten 2d array to 1d and using set
    cityList = []
    seen = set()
    result = []
    for i in paths2:
        for j in i:
            cityList.append(j)
    for item in cityList:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result[-1]


print("\n\nonly destination city")
print(onlyDCity2([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
print(onlyDCity([["A", "Z"]]))
print(onlyDCity([["A", "Z"]]))
print(onlyDCity2([["B", "C"], ["D", "B"], ["C", "A"]]))
print(onlyDCity([["B", "C"], ["D", "B"], ["C", "A"]]))
