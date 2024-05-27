def bubble_sort(list):
    i = 1
    for _ in range(len(list)):
        for j in range(len(list) - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        i += 1


def insertion_sort(list):
	for i in range(1, len(list)):
		j = i-1
		while list[j] > list[j+1] and j >= 0:
			list[j], list[j+1] = list[j+1], list[j]
			j -= 1


def binary_search(lista):
    kis = 0
    nagy = len(lista)
    keresett = int(input("Melyik számot keresed? "))
    megtalalva = False

    for _ in range(int(len(lista)**0.5)+1):
        kozep = int((kis + nagy) / 2)

        if keresett == lista[kozep]:
            print(f"Megtaláltva {kozep+1}. helyen.")
            megtalalva = True
            break
        elif keresett < lista[kozep] + 1:
            nagy = kozep    
        elif keresett > lista[kozep] - 1:
            kis = kozep

    if megtalalva == False:
        print("A szám nincs benne a listában")


if __name__ == "__main__":
    list = [123, 1, 76, 3, 86, 27, 73, 6, 25]
    print("Eredeti lista: ",list)

    bubble_sort(list)
    print("Bubble sort:",list)

    list = [123, 1, 76, 3, 86, 27, 73, 6, 25]
    insertion_sort(list)
    print("Insertion sort:", list)

    binary_search(list)