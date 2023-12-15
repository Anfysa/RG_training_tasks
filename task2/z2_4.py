stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
max=0
maxc=''
for channel,value in stats.items():
    if value>max:
        max=value
        maxc=channel
print(max,maxc)

