import numpy as np
import MDP

def valueIteration_policyEvaluation(mdp: MDP):
    num_states = len(mdp.states)
    num_actions = len(mdp.actions)
    V = np.zeros(num_states)  # Initialize value function to zero for all states
    
    iteration = 0
    while True:
        delta = 0
        V_new = np.zeros(num_states)
        
        for s in range(num_states):
            value_sum = 0
            for a in range(num_actions):
                
                pi_sa = mdp.policy[s, a]
                
                reward_sa = mdp.rewards[s, a]
                
                expected_value = np.sum(mdp.transitions[s, a, :] * V)
                
                value_sum += pi_sa * (reward_sa + mdp.gamma * expected_value)
            
            V_new[s] = value_sum
            delta = max(delta, abs(V_new[s] - V[s]))
        
        V = V_new
        iteration += 1
        
        # Termination condition
        if delta < mdp.threshold:
            break
    
    return V, iteration

