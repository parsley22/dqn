from colelctions import deque

class replay_buffer:
    def __init__(self, buffer_size = 1000):
        self.buffer_size = buffer_size
        self.buffer = deque(maxlen = self.buffer_size)

    def reset(self):
        self.buffer = deque(maxlen = self.buffer_size)
    def update(self, transition):
        self.buffer.append(transition)

    