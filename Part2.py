#Day one of the Advent of code 2020

#inport text file
f = open("input.txt", "r")
textList = f.read().split()
f.close()
intList = [int(x) for x in textList]

#sort numbers high to low
list1 = sorted(intList, reverse=True)
list2 = sorted(intList, reverse=False)


#does that = a lower number?
for x in list1:
    for y in list2:
        for z in list2:
            sum = x + y + z
            if sum == 2020:
                # print("Number 1 = ", y, " and Number 2 = ", x)
                answer = x * y * z
                print("The answer is ", answer)
                print(x,y,z)
                quit()

#close file and output

