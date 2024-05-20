def bubblesort(list):
    i = 1
    for _ in range(len(list)):
        for j in range(len(list) - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        i += 1


def insertionsort(list):
	for i in range(1, len(list)):
		j = i-1
		while list[j] > list[j+1] and j >= 0:
			list[j], list[j+1] = list[j+1], list[j]
			j -= 1


if __name__ == "__main__":
    list = [123, 1, 76, 3, 86, 27, 73, 6, 25]
    print("Eredeti lista: ",list)

    bubblesort(list)
    print("Bubble sort:",list)

    list = [123, 1, 76, 3, 86, 27, 73, 6, 25]
    insertionsort(list)
    print("Insertion sort:", list)