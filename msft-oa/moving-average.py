# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

class MovingAverage(object):
    def __init__(self, window_size):
        self.data_stream = []
        self.window_size = window_size
        self.total = 0

    def next(self, val):
        self.total += val
        self.data_stream.append(val)

        if len(self.data_stream) > self.window_size:
            self.total -= self.data_stream.pop(0)

        return self.total/len(self.data_stream)


if __name__ == '__main__':
    m = MovingAverage(3)
    print m.next(1) #output = 1
    print m.next(10) #output = (1 + 10)/2 = 5
    print m.next(3) #output = (1 + 10 + 3)/3 = 4
    print m.next(5) #output = (10 + 3 + 5)/3 = 6


