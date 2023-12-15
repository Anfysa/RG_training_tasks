ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
all_unique_values = set()

for user_values in ids.values():
    all_unique_values.update(set(user_values))

print(list(all_unique_values))