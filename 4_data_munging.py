largest_spread = 0
day_with_largest_spread = None

for line in open('weather.dat', 'r'):
    datapoints = line.split()

    if len(datapoints) == 0:
        continue

    if datapoints[0].isdigit():
        day, maximum, minimum = [ number.rstrip('*') for number in datapoints[0:3] ]
        spread = int(maximum) - int(minimum)
        
        if spread > largest_spread:
            largest_spread = spread
            day_with_largest_spread = datapoints[0]

print day_with_largest_spread
