from lista4_0 import Robot
import copy
import datetime


def quicksort(array):

    less = []
    equal = []
    greater = []
    s = (0 + len(array)-1) //2

    if len(array) > 1:
        pivot = array[s]
        for x in range(len(array)):
            if array[x] < pivot:
                less.append(array[x])
            elif array[x] == pivot:
                equal.append(array[x])
            elif array[x] > pivot:
                greater.append(array[x])
        # print(array)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return array


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, (len(array)-1)-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    return(array)


def to_sort(army, key):
    robots_by_parametr = []
    for r in range(len(army)):
        robot = army[r]
        robots_by_parametr.append([robot[key], r])
    tab_sort = bubble_sort(robots_by_parametr)

    return tab_sort


def to_sort2(army, key):
    robots_by_parametr = []
    for r in range(len(army)):
        robot = army[r]
        robots_by_parametr.append([robot[key], r])
    tab_sort = quicksort(robots_by_parametr)

    return tab_sort


def print_sort_tab(army, tab_sort):
    tab1 = tab_sort
    sorted_army1 = []
    for i in range(len(tab_sort)):
        order1 = tab1[i][1]
        sorted_army1.append(army[order1])

    robots.showArmy(sorted_army1, True)
    return sorted_army1


robots = Robot()
robotsArmy = robots.openArmy()

parametrs = ["id", "typ", "masa", "zasieg", "rozdz"]
tab1 = copy.deepcopy(robotsArmy)
tab2 = copy.deepcopy(robotsArmy)

start1 = datetime.datetime.now()
sorted_table1 = to_sort(tab1, 'masa')
duration1 = datetime.datetime.now() - start1

start2 = datetime.datetime.now()
sorted_table2 = to_sort2(tab2, 'masa')
duration2 = datetime.datetime.now() - start2

print('sortowanie babelkowe:')
print_sort_tab(tab1, sorted_table1)
print('sortowanie szybkie:')
print_sort_tab(tab2, sorted_table2)

print("czas sortowanie babelkowego: ", duration1)
print("czas sortowania szybkiego: ", duration2)
