boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys = sorted(boys)
girls = sorted(girls)
if (len(girls)==len(boys)):
    match = zip (girls,boys)
    for girls, boys in match:
        print(f"{boys} и {girls}")
else:
    print('Error: the number of people on the list does not match')