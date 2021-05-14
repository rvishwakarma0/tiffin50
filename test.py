charges = [10, 12, 13]
chargeType = 'PNP'
chargeType = list(chargeType)
maxSum = 0

for i in range(len(charges)):
    if chargeType[i] == 'P':
        maxSum += charges[i]
    else:
        maxSum -= charges[i]

print(abs(maxSum)*100)