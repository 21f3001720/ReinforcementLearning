import sys
from MDP import read_mdp_from_file
from policyEvaluation import valueIteration_policyEvaluation

def main():
    if len(sys.argv) < 2:
        print("Usage: python simulate.py <mdp_input_file>")
        sys.exit(1) 

    mdp_filename = sys.argv[1]
    mdp = read_mdp_from_file(mdp_filename)
    V, iterations = valueIteration_policyEvaluation(mdp)

    print(f"Value function after {iterations} iterations:")
    for state, val in zip(mdp.states, V):
        print(f"State {state}: {val:.4f}")

if __name__ == "__main__":
    main()
