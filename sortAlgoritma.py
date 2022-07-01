
def bubbleSort(myArray):
    for i in range(len(myArray)-1):
        
        for j in reversed(range(i+1, len(myArray))):
            
            if myArray[j] < myArray[j-1]:
                depo = myArray[j-1]
                myArray[j-1] = myArray[j]
                myArray[j] = depo
                
    #print(myArray)


myArray = [5, 8, 13, 25, 1]

#bubbleSort(myArray)

# myArray.sort() Kucukten buyuge
# myArray.reverse() Diziyi ters cevirir


def insertionSort(myArray):
    for i in range(1, len(myArray)):
        key= myArray[i]
        j= i -1

        while j>=0 and key< myArray[j]:
            myArray[j+1]= myArray[j]
            j=j-1

        myArray[j+1]= key

#insertionSort(myArray)
#print(myArray)

dizi=[2,5,7,8,3]




def bubble_sort(dizi):

    for i in range(len(dizi)):
        for c in range (0,len(dizi)-1):
            if dizi[c]> dizi[c+1]:
                dizi[c+1], dizi[c]= dizi[c], dizi[c+1]
    
    return dizi

#print(bubble_sort(dizi))


def selectionSort(dizi):
    for i in range(len(dizi)):
        minIndex= i
        for j in range(i+1, len(dizi)):

            if dizi[minIndex]> dizi[j]:
                minIndex=j

            if minIndex !=i:
                dizi[minIndex], dizi[i] = dizi[i], dizi[minIndex]



selectionSort(dizi)
print(dizi)