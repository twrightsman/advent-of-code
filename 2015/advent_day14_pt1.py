import re
import sys

RACE_DURATION = 2503

class Reindeer:
    def __init__(self, name, fly_speed, fly_time, rest_time):
        self.name = name
        self.fly_speed = fly_speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.position = 0
        self.resting = False
        self.current_action_time = 0
        self.points = 0

    def race(self):
        self.current_action_time += 1
        
        if not self.resting:
            self.position += self.fly_speed

            if self.current_action_time == self.fly_time:
                self.current_action_time = 0
                self.resting = True
        else:
            if self.current_action_time == self.rest_time:
                self.current_action_time = 0
                self.resting = False


instruction_pattern = re.compile(r'^([A-Z][a-z]+) can fly ([0-9]+) km\/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.')

reindeer = []

for line in sys.stdin:
    result = re.match(instruction_pattern, line)

    name = result.group(1)
    fly_speed = int(result.group(2))
    fly_time = int(result.group(3))
    rest_time = int(result.group(4))

    reindeer.append(Reindeer(name, fly_speed, fly_time, rest_time))

def getRacerPosition(item):
    return item[1]

for second in range(1, RACE_DURATION + 1):
    current_positions = []
    for racer in reindeer:
        racer.race()
    for racer in reindeer:
        current_positions.append((racer, racer.position))

    current_positions = sorted(current_positions, key=getRacerPosition)
    current_positions[-1][0].points += 1

    lead = current_positions[-1][1]
    for index in range(2, len(current_positions)):
        if current_positions[-index][1] == lead:
            current_positions[-index][0].points += 1
        else:
            break

results = []
for racer in reindeer:
    results.append((racer.name, racer.points))

def getRacerPoints(item):
    return item[1]

results = sorted(results, key=getRacerPoints)

print(results[-1])