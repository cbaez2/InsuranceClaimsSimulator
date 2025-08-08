#main.py

from input import get_number_of_claims, get_user_inputs
from distributions import get_distribution_choice, get_distribution_parameters
from simulate import simulate_losses
from summary import summarize_results

def main():
    print("📊 Welcome to the Insurance Claim Simulator!\n")
    print("We will simulate insurance claims to perform an actual-to-expected (A/E) analysis on the insurance payments based on customizable inputs such as: \n"
          "  • The number of claims\n"
          "  • Policy terms\n"
          "  • Claim distribution used\n")
    
    # Step 1: Ask how many claims to simulate
    n_claims = get_number_of_claims()

    # Step 2: Set up the policy using that number
    info = get_user_inputs(n_claims)

    # Step 3: Choose a loss distribution for those claims
    if n_claims ==1:
        print("\nWhat distribution do you want this single claim to follow?")
    else:
        print(f"\nWhat distribution do you want the {n_claims:,} claims to follow?")
    dist_name = get_distribution_choice()
    dist_params = get_distribution_parameters(dist_name, info)

    # Step 4: Simulate and summarize
    losses, payments = simulate_losses(info, dist_name, dist_params)
    summarize_results(losses, payments, info, dist_name, dist_params)
    input("\nSimulation complete. Press Enter to exit.")
    
if __name__ == "__main__":
    main()










