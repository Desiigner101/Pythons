start = 25
end = 50 
print ("prime numbers between", start, "and", end, "are")

for number in range (start, end + 1):
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print (number)
