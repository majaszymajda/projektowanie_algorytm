import random
import matplotlib.pyplot as plt
import time


def generate_array(size):
    array = []
    for i in range(size):
        x = random.randint(1, 1000)
        array.append(x)

    return array


def draw_an_array(array):
    result = array
    print("result", result)
    plt.bar(range(len(result)), result, color='maroon', width=0.8)
    plt.draw()
    plt.pause(0.5)
    plt.clf()


def heap_pom(array, n, i):
    largest = i  # rodzic
    left = 2 * i + 1     # dziecko lewe = 2*i + 1
    right = 2 * i + 2     # dziecko prawe = 2*i + 2

    draw_an_array(array)

    if left < n and array[largest] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        heap_pom(array, n, largest)


def heapSort(array):
    n = len(array)

    for i in range(n//2 - 1, -1, -1):
        heap_pom(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap_pom(array, i, 0)

    return array


def quicksort(array):

    less = []
    equal = []
    greater = []
    s = (0 + len(array)-1) // 2

    if len(array) > 1:
        pivot = array[s]

        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        # array_vol2 = less+equal+greater
        # draw_an_array(array_vol2)

        return quicksort(less)+equal+quicksort(greater)
    else:
        return array


if __name__ == '__main__':

    size = int(input("podaj ilość zmiennych do sortowania: "))
    array = generate_array(size)
    array1 = array.copy()
    array2 = array.copy()

    plt.ion()
    plt.figure(figsize=(10, 5))
    plt.show()

    sorted_array1 = heapSort(array1)

    print(sorted_array1)

    time.sleep(10)

    sorted_array2 = quicksort(array2)
    print(sorted_array2)


