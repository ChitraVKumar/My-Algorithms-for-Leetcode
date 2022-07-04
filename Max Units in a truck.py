def maxUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1])
    sorted_list = (boxTypes)[::-1]
    print(sorted_list)

    count_units = 0
    for box_nums, unit in sorted_list:
        if truckSize <= box_nums:
            count_units += truckSize * unit
            break
        count_units += box_nums * unit
        truckSize -= box_nums

    return count_units

print(maxUnits([[5,10], [2,5], [4,7], [3,9]], 10))
