import bisect

def request_handler(requests, orders_starts, orders_start_dict, orders_ends, orders_end_dict):
    orders_starts.sort()
    orders_ends.sort()

    start_costs = []
    total_cost = 0

    for start in orders_starts:
        for order in orders_start_dict[start]:
            total_cost += order['cost']
        start_costs.append(total_cost) # накапливаеамая сумма заказов от минимального start до start1, start2, ...
    
    end_durations = []
    total_duration = 0
    for end in orders_ends:
        for order in orders_end_dict[end]:
            total_duration += order['end'] - order['start']
        end_durations.append(total_duration) # накапливаеамая продолжительность заказов от минимального end до end1, end2, ...

    result = []

    for request in requests:
        if request['type'] == 1:
            # границы заказов
            left_index = bisect.bisect_left(orders_starts, request['start']) # индекс первого элемента >= request['start'] в orders_starts
            right_index = bisect.bisect_right(orders_starts, request['end']) - 1 # индекс первого элемента > request['end'] в orders_starts - 1 
            
            if left_index <= right_index: # заказы в промежутке есть
                if left_index == 0:
                    result.append(start_costs[right_index])
                else:
                    result.append(start_costs[right_index] - start_costs[left_index - 1])
            else: # если left_index > right_index, то значит нет заказов, начинающихся в промежуте [request['start'], request['end']]
                result.append(0)
        else:
            left_index = bisect.bisect_left(orders_ends, request['start'])
            right_index = bisect.bisect_right(orders_ends, request['end']) - 1
            
            if left_index <= right_index:
                if left_index == 0:
                    result.append(end_durations[right_index])
                else:
                    result.append(end_durations[right_index] - end_durations[left_index - 1])
            else:
                result.append(0)

    return ' '.join(map(str, result))

N = int(input())
orders = []
requests = []

orders_starts = []
orders_start_dict = {}
orders_ends = []
orders_end_dict = {}

for _ in range(N):
    start, end, cost = map(int, input().split())
    order = {'start': start, 'end': end, 'cost': cost}
    orders.append(order)

    if start in orders_start_dict:
        orders_start_dict[start].append(order)
    else:
        orders_start_dict[start] = [order]
        orders_starts.append(start)
        
    if end in orders_end_dict:
        orders_end_dict[end].append(order)
    else:
        orders_end_dict[end] = [order]
        orders_ends.append(end)

Q = int(input())
for _ in range(Q):
    start, end, req_type = map(int, input().split())
    requests.append({'start': start, 'end': end, 'type': req_type})

print(request_handler(requests, orders_starts, orders_start_dict, orders_ends, orders_end_dict))
