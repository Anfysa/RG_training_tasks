def list_to_dict(lst):
    if len(lst) == 2:
        return {lst[0]: lst[1]}
    else:
        return {lst[0]: list_to_dict(lst[1:])}

input_list = ['2018-01-01', 'yandex', 'cpc', 100]
result_dict = list_to_dict(input_list)

print(result_dict)
