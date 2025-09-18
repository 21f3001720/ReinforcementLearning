1. Save input file in same folder as name 'input.txt'
2. Make sure 'input.txt' has following format:
    Line 1: Comma-separated elements of the state space (e.g., a,b,c,d).
    Line 2: Comma-separated elements of the action space (e.g., 1,2).
    Line 3: Single number for discount factor γ.
    Line 4: Single number for termination threshold.
    Line 5: Comma-separated policy probabilities for each state-action pair, ordered by states and actions.
    Line 6: Comma-separated deterministic reward values for state-action pairs, ordered similarly.
    Line 7: Comma-separated transition probabilities for all next states for each state-action pair, ordered by states, actions, and next states.
3. after saving 'input.txt' in same folder, open cmd in current folder and run 'simulate.py' in cmd using command:
    > python simulate.py <mdp_input_file>
4. I have included a sample MDP problem. To use that run:
    > python simulate.py sample_mdp.txt

For any queries reach out to : nishadhemant1234@gmail.com
