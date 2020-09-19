import numpy as np

class linear_model:
    def __init__(self, num_states, num_actions):
        self.num_states = num_states
        self.num_actions = num_actions
        self.w = np.random.randn(self.num_states) 
        
    def predict(self, s):
        out = self.w.dot(s)
        return 0 if (1 / (1 + np.exp(-out))) < 0.5 else 1
        