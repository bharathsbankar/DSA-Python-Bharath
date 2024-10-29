
#problem : find maximaum of 10day whether and average of first weak whether from nyc_weather.csv
#which data structure is good ? , answer : list is better since elements need to be traversed based on given conditions
arr = []
try:
    file = open("nyc_weather.csv", "r")

except:
    print("error in opening file")
next(file)  # it is used to skip the header line in csv
for line in file:
    tokens = line.split(",")
    # try:
    temp = int(tokens[1])

    arr.append(temp)
    # except:
    #     print("error in converting to int")

sum = 0
for i in range(0, 7):
    sum += arr[i]

average_temp = sum / 7
maximaum_temp = max(arr)
print("max:", maximaum_temp)
print("average:", average_temp)
