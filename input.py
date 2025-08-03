def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'n']:
            break
        print("Please enter either 'y' or 'n'.")
    return response


def get_number_of_claims():
    MAX_CLAIMS = 10 ** 7  # For example, 10 million max
    while True:
        try:
            n = int(input("How many claims would you like to simulate? "))
            if n > 0 and n <= MAX_CLAIMS:
                return n
            elif n > MAX_CLAIMS:
                print(f"Please enter a number less than or equal to {MAX_CLAIMS:,}.")
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")


def get_user_inputs(n_claims):
    import numpy as np

    MAX_DEDUCTIBLE = 1_000_000
    MAX_POLICY_LIMIT = 1_500_000
    MAX_COINSURANCE = 200

    if n_claims == 1:
        print(f"\nHow do you want to set up the insurance policy for this single claim?")
    else:
        print(f"\nHow do you want to set up the insurance policy for these {n_claims:,} claims?")

    deductible = 0  # Deductible
    if get_yes_no("Do you want a deductible? (y/n) ") == "y":
        while True:
            try:
                deductible = float(input("Enter a deductible amount: "))
                if deductible > MAX_DEDUCTIBLE:
                    print(f"Please enter a deductible amount less than or equal to ${MAX_DEDUCTIBLE:,}.")
                elif deductible > 0:
                    break
                elif deductible == 0:
                    print("⚠️ Warning: A deductible of 0 means the deductible has no effect.")
                    break
                else:
                    print("Please enter a positive deductible amount.")
            except ValueError:
                print("Please enter a positive deductible amount.")

    policy_limit = np.inf  # Policy limit none by default
    if get_yes_no("Do you want a policy limit? (y/n) ") == "y":
        while True:
            try:
                policy_limit = float(input("Enter a policy limit: "))
                if policy_limit <= deductible:
                    print(f"Please enter a policy limit greater than the deductible amount of ${deductible:,}.")
                elif policy_limit > MAX_POLICY_LIMIT:
                    print(f"Please enter a policy limit less than or equal to ${MAX_POLICY_LIMIT:,}.")
                else:
                    break
            except ValueError:
                print("Please enter a numeric value for the policy limit.")

    coinsurance_rate = 100  # default = 100%
    if get_yes_no("Do you want a coinsurance? (y/n) ") == 'y':
        while True:
            try:
                coinsurance_rate = float(input("Enter a coinsurance (as a percentage): "))
                if coinsurance_rate > MAX_COINSURANCE:
                    print(f"Please enter a coinsurance of {MAX_COINSURANCE}% or less.")
                elif coinsurance_rate == 0:
                    print("⚠️ Warning: A coinsurance of 0% means the insurer does not pay anything.")
                    break
                elif coinsurance_rate == 100:
                    print("⚠️ Warning: A coinsurance of 100% means the insurer pays 100% of the losses.")
                    break
                elif coinsurance_rate > 100:
                    print("⚠️ Warning: A coinsurance above 100% means the insurer pays more than the loss itself.")
                    break
                elif 0 < coinsurance_rate < 100:
                    break
                else:
                    print("Please enter a positive coinsurance.")
            except ValueError:
                print("Please enter a valid numeric value for coinsurance.")

    return {
        'deductible': deductible,
        'policy_limit': policy_limit,
        'coinsurance_rate': coinsurance_rate,
        'n_claims': n_claims
    }





