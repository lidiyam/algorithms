"""
Assign each interval a colour such that 2 intervals getting the same
colour are disjoint. Minimize the # of colours used.
"""


class Interval:

    def __init__(self, start, end, colour=None):
        self.start = start
        self.end = end
        self.colour = colour

    def __repr__(self):
        return "Start: {}, End: {}, Colour: {}".format(self.start, self.end, self.colour)

    def intersect(self, interval):
        if interval.start <= self.end and self.start <= interval.end:
            return True
        return self.start <= interval.end and interval.start <= self.end


def interval_colour(intervals, colours_available):
    sorted(intervals, key=lambda i: i.start)
    colours_used = {}

    for interval in intervals:
        flag = False
        for colour, colour_int in colours_used.iteritems():
            if not interval.intersect(colour_int):
                interval.colour = colour
                colour_int.end = interval.end
                flag = True
                break
        if not flag:
            colour = colours_available.pop(0)
            interval.colour = colour
            colours_used[colour] = Interval(interval.start, interval.end, colour)
    return intervals


if __name__ == '__main__':
    intervals = [Interval(2,4), Interval(3,9), Interval(7,10)]
    colours = ['red', 'green', 'blue', 'black', 'white']

    results = interval_colour(intervals, colours)
    print results
