# simulation of rolling a dice for 1000 times


from random import randint
import pygal


class Die():

    def __init__(self, num=6):
        self.num = num

    def roll(self):
        return randint(1, self.num)


die = Die()
results = []
for i in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for face in range(1, die.num + 1):
    frequency = results.count(face)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.add('Die', frequencies)
hist.render_to_file('die_visual.svg')
