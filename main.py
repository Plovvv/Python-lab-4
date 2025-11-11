MAX_VOLUME = 9
price_start = 15
items = {'r':{'weight':3,'price':25},
        'a':{'weight':2,'price':15},
        'p':{'weight':2,'price':15},
        'm':{'weight':2,'price':20},
        'i':{'weight':1,'price':5},
        'k':{'weight':1,'price':15},
        'x':{'weight':3,'price':20},
        't':{'weight':1,'price':25},
        'f':{'weight':1,'price':15},
        'd':{'weight':1,'price':10},
        's':{'weight':2,'price':20},
        'c':{'weight':2,'price':20}}

def gen_table(items, max_volume=MAX_VOLUME):
    item_list = list(items.items())
    N = len(item_list)
    DP = [[0] * (max_volume + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        item_name, item_data = item_list[i-1]
        price = item_data['price']
        volume = item_data['weight']

        for w in range(max_volume + 1):
            if volume > w:
                DP[i][w] = DP[i-1][w]
            else:
                price_not_taken = DP[i-1][w]
                price_taken = price + DP[i-1][w - volume]
                DP[i][w] = max(price_not_taken, price_taken)              
    return DP, item_list

def find_selected_items(dp_table, item_list, max_volume=MAX_VOLUME):
    N = len(item_list)
    w = max_volume
    selected_items = []
    for i in range(N, 0, -1):
        item_name, item_data = item_list[i-1]
        volume = item_data['weight']
        if dp_table[i][w] != dp_table[i-1][w]:
            selected_items.append(item_name)
            w -= volume
        
    selected_items.reverse()
    return selected_items


if __name__ == '__main__':
    dp_table, items_list = gen_table(items, MAX_VOLUME)
    selected = find_selected_items(dp_table, items_list, MAX_VOLUME)
    max_price = sum([i['price'] for i in list(items.values())])
    sum_price = dp_table[len(items)][MAX_VOLUME] 

    print(f"Полученная стоимость: {2*sum_price - max_price + price_start}")
    print(f"Выбранные предметы: {selected}")
