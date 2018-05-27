import sys

rows = []
with open('sampleprime.txt') as file:
    for line in file:
        rows.append(line.split())
size = len(rows[-1])
for i in range(len(rows)):
    rows[i] = rows[i] + ['0'] * (size - len(rows[i]))



def isprimeornot(n): #Input asal sayi ise true döner değilse false
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

def dynamicProgSum(rows):
    secondLastLineIndex = len(rows) - 2
    rightIndex = len(rows[len(rows)-1])-1


    for i in range(secondLastLineIndex,-1,-1):

        rightIndex = rightIndex - 1

        if(i == len(rows) - 2): #Sadece ilk iteration bu if bloğu çalışır
            for t in range(rightIndex,-1,-1):

                if (isprimeornot(int(rows[i][t]))):
                    rows[i][t] = -sys.maxsize - 1


                if (not isprimeornot(int(rows[i][t]))):

                    rightLeaf = int(rows[i + 1][t + 1])
                    leftLeaf = int(rows[i + 1][t])
                    rootLeaf = int(rows[i][t])

                    #Sol leaf sağdan büyükse
                    if (((leftLeaf > rightLeaf) and (not isprimeornot(leftLeaf))) or
                            ((rightLeaf > leftLeaf) and ((isprimeornot(rightLeaf) and (not isprimeornot(leftLeaf)))))):
                        rows[i][t] = format(rootLeaf + leftLeaf)
                    # Sağ leaf soldan büyükse
                    if (((leftLeaf < rightLeaf) and (not isprimeornot(rightLeaf))) or
                            ((leftLeaf>rightLeaf) and ((isprimeornot(leftLeaf) and (not isprimeornot(rightLeaf)))))):
                        rows[i][t] = format(rootLeaf+rightLeaf)
                    # Sağ leaf ile sol eşitse
                    if ((rightLeaf == leftLeaf) and (not isprimeornot(rightLeaf))):
                        rows[i][t] = format(rootLeaf + rightLeaf)

        # Satırları sayar
        if (i != len(rows) - 2):
            # Tek satır içinde sayıları gezer-----------------
            for t in range(rightIndex, -1, -1):
                key = 1
                #Sayı asal sayı ise min olarak işaretle
                if (isprimeornot(int(rows[i][t]))):
                    rows[i][t] = -sys.maxsize - 1
                    key = 0
                #Sayı asal değilse işleme girmek için bu if bloğu çalışır
                if (not isprimeornot(int(rows[i][t])) and key == 1):
                    rightLeaf = int(rows[i + 1][t + 1])
                    leftLeaf = int(rows[i + 1][t])
                    rootLeaf = int(rows[i][t])

                    # Sağ leaf soldan büyükse
                    if(rightLeaf > leftLeaf):
                        rows[i][t] = format(rightLeaf+rootLeaf)
                    # Sol leaf sağdan büyükse
                    if(rightLeaf < leftLeaf):
                        rows[i][t] = format(leftLeaf + rootLeaf)
                    # İki taraf eşitse ve asal değillerse
                    if(rightLeaf == leftLeaf and rightLeaf !=(-sys.maxsize - 1)):
                        rows[i][t] = int(rows[i][t]) + int(leftLeaf)
                    # İki taraf eşitse ve asallarsa
                    if (rightLeaf == leftLeaf and rightLeaf == (-sys.maxsize - 1)):
                        rows[i][t] = -sys.maxsize - 1

    if(rows[i][t] == (-sys.maxsize - 1)):
        print("There is no path without a prime number")
    else:
        print("Sum of longest path without prime number is: " + format(rows[i][t]))



dynamicProgSum(rows);


