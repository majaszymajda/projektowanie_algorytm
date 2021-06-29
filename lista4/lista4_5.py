from operator import itemgetter
from lista4_0 import Robot


found_robots = {
    "id": [],
    "typ": [],
    "masa": [],
    "zasieg": [],
    "rozdz": [],
}


def sort(array, key):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append[key](x)
            elif x == pivot:
                equal.append[key](x)
            elif x > pivot:
                greater.append[key](x)
        return sort(less)+equal+sort(greater)
    else:
        return array


def sortRobots(army, param):
    return sort(army, key=itemgetter(param))


def auxiliaryVectors(army):
    vectors = []
    print(f'\nKlucze: {army[0].keys()}')
    for param in army[0].keys():
        vector = []
        sortedArmy = sortRobots(army, param)
        for elem in sortedArmy:
            vector.append(army.index(elem))
        vectors.append(vector)

    print(f'\nVectors: {vectors}')
    return vectors


def BinarySearch(tab, value, left, rigth, army, key):
    if left >= rigth:
        found_robots[key].append("brak")
        return -1
    if value == army[tab[left]][key]:
        # print(value, army[tab[left]][f"{key}"], left)
        print(f'ZNALEZIONO: {value}, na miejcu {tab[left]+1}')
        found_robots[key].append(tab[left]+1)

        return left
    mid = (left + rigth) // 2
    wanted = army[tab[mid]][key]
    print(f"Na pozycji: {tab[mid]+1}, znajduje sie wart: {wanted}")
    # print("środek: ", mid)
    if value < army[tab[mid]][key]:
        BinarySearch(tab, value, left, mid-1, army, key)
    else:
        BinarySearch(tab, value, mid+1, rigth, army, key)


def to_find(army, search_array):
    vectors = auxiliaryVectors(army)
    for index in range(len(search_array)):
        if search_array[index] is None:
            print('szukana to None !')
        else:
            key = list(army[0].keys())[index]
            print(f'szukane wybranej kategorii {key}: {search_array[index]} ')
            for items in range(len(search_array[index])):
                left = 0
                rigth = len(vectors[0])  # liczba robotów
                value = search_array[index][items]
                print(f"szukana: {value}, z kategorii {key}")
                BinarySearch(vectors[index], value, left, rigth, army, key)
    print(found_robots)
    return found_robots


robots = Robot()
# robotsArmy = robots.raiseArmy(HOW_MANY_ROBOTS)
robotsArmy = robots.openArmy()

TO_SEARCH = (None, ['AFV', 'AGV'], [590, 1179], [655, 998], [3, 29])

progressRobotIndex = to_find(robotsArmy, TO_SEARCH)

finalRobotIndex = ''

'''
for x in range(len(progressRobotIndex) - 1):
    finalRobotIndex = progressRobotIndex[x].intersection(progressRobotIndex[x+1])
print(f'finalRobotIndex: {finalRobotIndex}')
'''
