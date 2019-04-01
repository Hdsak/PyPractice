alien = {'color': "green",'points':5}
print(alien['color'])
print(alien['points'])
print(alien)
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)
alien = {}
alien['color'] = 'yellow'
alien['points'] = 10
print(alien)
alien = {'x_position':0,'y_position':25,'speed':'medium' }
print("position x " + str(alien['x_position']))
if alien['speed'] == 'low':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
print("new x pos is " + str(alien['x_position'] + x_increment))
del alien['speed']
print(alien)