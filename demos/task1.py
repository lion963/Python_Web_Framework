list1 = [1,3, 4, 7, 34, 2, 3, 5]

dict1 = {}

def data_count(list_data, dict_data):
    for el in list_data:
        if el not in dict_data:
            dict_data[el] = 1
        else:
            dict_data[el] += 1
    return dict_data


print(data_count(list1, dict1))

