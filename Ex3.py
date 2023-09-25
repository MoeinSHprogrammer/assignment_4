n = int(input())
m = int(input())


for i in range(1, n+1):
    string = ''
    for j in range(1 , m+1):

        string += (str(i * j) + " ")
    print(string)