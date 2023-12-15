queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

count = {
    'one': 0,
    'two': 0,
    'three': 0,
}

for query in queries:
    words = query.split()
    if len(words) == 1:
        count['one'] += 1
    elif len(words) == 2:
        count['two'] += 1
    elif len(words) == 3:
        count['three'] += 1

percent = {
    'one': int(count['one'] / sum(count.values()) * 100),
    'two': int(count['two'] / sum(count.values()) * 100),
    'three': int(count['three'] / sum(count.values()) * 100),
}

print(percent)
