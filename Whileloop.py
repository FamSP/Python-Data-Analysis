number = 1

while number < 5:
    print(number)
    if number == 6:
# there is break and continue break mean stop there and 
# continue will go back to loop again without check furter condition
        break 
    number = number + 1
else:
    print('No longer < 5')
    