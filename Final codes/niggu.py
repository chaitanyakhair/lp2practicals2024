heuristic_values = {'A': 11, 'B': 16, 'C': 43, 'D': 56, 'E': 26}

graph = {
    'A': {'B': 21, 'D': 8, 'E': 52},
    'B': {'A': 23, 'E': 45, 'C': 69},
    'C': {'B': 78, 'D': 87, 'E': 90},
    'D': {'A': 61, 'C': 11},
    'E': {'A': 44, 'B': 92, 'C': 59}
}

import queue as Q

start_city = 'B'
goal_city = 'A'
result_path = ''

def calculate_total_cost(city_sequence):
    cities = city_sequence.split(" , ")
    heuristic_cost = 0
    actual_cost = 0
    for i in range(len(cities) - 1):
        actual_cost += graph[cities[i]][cities[i + 1]]
    heuristic_cost = heuristic_values[cities[-1]]
    return heuristic_cost + actual_cost

def expand_search(city_queue):
    global result_path
    total_cost, city_sequence, current_city = city_queue.get()
    if current_city == goal_city:
        result_path = city_sequence + " : : " + str(total_cost)
        return
    for next_city in graph[current_city]:
        city_queue.put((calculate_total_cost(city_sequence + " , " + next_city), city_sequence + " , " + next_city, next_city))
    expand_search(city_queue)

def main():
    city_queue = Q.PriorityQueue()
    current_city = start_city
    city_queue.put((calculate_total_cost(start_city), start_city, current_city))
    expand_search(city_queue)
    print("The A* path with the total is: ")
    print(result_path)

main()
