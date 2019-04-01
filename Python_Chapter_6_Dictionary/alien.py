alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens=[alien_0,alien_1,alien_2]
for n in aliens:
    print(n)
aliens=[]
for n in range(30):
    new_alien={'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for n in aliens[:3]:
    if n['color']=='green':
        n['color']='yellow'
        n['points']='10'
        n['speed'] = 'medium'
for n in aliens[:5]:
    print(n)
print("TOtal " + str(len(aliens)))
