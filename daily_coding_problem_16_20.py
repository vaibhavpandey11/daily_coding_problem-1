def coding_problem_16():
    """
    You run a sneaker website and want to record the last N order ids in a log. Implement a data structure to
    accomplish this, with the following API:

        record(order_id): adds the order_id to the log
        get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

    You should be as efficient with time and space as possible.
    Example:

    >>> coding_problem_16()
    True
    """
    class OrdersLog(object):

        def __init__(self, num):
            self.circular_buffer = [None] * num
            self.current_index = 0

        def record(self, order_id):
            self.circular_buffer[self.current_index] = order_id
            self.current_index += 1
            if self.current_index == len(self.circular_buffer):
                self.current_index = 0

        def get_last(self, num):
            start_index = self.current_index - num
            if start_index < 0:  # wrap around
                return self.circular_buffer[start_index:] + self.circular_buffer[:self.current_index]
            else:  # no wrapping required
                return self.circular_buffer[start_index:self.current_index]

    log = OrdersLog(10)
    for id in xrange(20):
        log.record(id)

    assert(log.get_last(0) == [])
    assert(log.get_last(1) == [19])
    assert(log.get_last(5) == range(15, 20))

    log.record(20)
    log.record(21)

    assert(log.get_last(0) == [])
    assert(log.get_last(1) == [21])
    assert(log.get_last(5) == range(17, 22))

    return True


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
