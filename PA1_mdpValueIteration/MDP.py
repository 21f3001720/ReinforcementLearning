import numpy as np

class MDP:
    def __init__(self, states, actions, gamma, threshold, policy, rewards, transitions):
        self.states = states
        self.actions = actions
        self.gamma = gamma
        self.threshold = threshold
        self.policy = policy        # shape: (num_states, num_actions)
        self.rewards = rewards      # shape: (num_states, num_actions)
        self.transitions = transitions  # shape: (num_states, num_actions, num_states)

def read_mdp_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    states = lines[0].strip().split(',')
    actions = lines[1].strip().split(',')
    gamma = float(lines[2].strip())
    threshold = float(lines[3].strip())

    num_states = len(states)
    num_actions = len(actions)

    # Parse policy as 2D array: (states x actions)
    policy_flat = list(map(float, lines[4].strip().split(',')))
    policy = np.array(policy_flat).reshape((num_states, num_actions))

    # Parse rewards as 2D array: (states x actions)
    rewards_flat = list(map(float, lines[5].strip().split(',')))
    rewards = np.array(rewards_flat).reshape((num_states, num_actions))

    # Parse transition probabilities as 3D array: (states x actions x states)
    transitions_flat = list(map(float, lines[6].strip().split(',')))
    transitions = np.array(transitions_flat).reshape((num_states, num_actions, num_states))

    return MDP(states, actions, gamma, threshold, policy, rewards, transitions)

