# summary.py_
import numpy as np
from expectedvalue import expected_payment


def summarize_results(losses, payments, info, dist_name, dist_params):
    n = len(losses)
    total_payment = np.sum(payments)
    expected_pay, margin_error, integration_warning = expected_payment(info, dist_name, dist_params)
    expected_total = expected_pay * n
    total_error = margin_error * n
    d=info['deductible']
    u=info['policy_limit']
    c=info['coinsurance_rate']/100

    # summary.py
    print("\nPolicy and claim characteristics:")

    # Singular/plural logic
    if n == 1:
        sim_phrase = "Simulated a single claim that is"
        claim_intro = "The claim follows"
    else:
        sim_phrase = f"Simulated {n:,} claims that are"
        claim_intro = "All claims follow"

    # POLICY CHARACTERISTICS SUMMARY
    if d == 0 and u == float('inf') and c == 1:
        print(f"\n{sim_phrase} not subject to a deductible, policy limit, or coinsurance.")
    elif d > 0 and u == float('inf') and c == 1:
        print(f"\n{sim_phrase} subject only to a deductible of ${d:,}.")
    elif d == 0 and u < float('inf') and c == 1:
        print(f"\n{sim_phrase} subject only to a policy limit of ${u:,}.")
    elif d == 0 and u == float('inf') and c != 1:
        print(f"\n{sim_phrase} subject only to a coinsurance of {c * 100:.0f}%.")
    elif d > 0 and u < float('inf') and c == 1:
        print(f"\n{sim_phrase} subject to a deductible of ${d:,} and a policy limit of ${u:,}, but no coinsurance.")
    elif d > 0 and u == float('inf') and c != 1:
        print(
            f"\n{sim_phrase} subject to a deductible of ${d:,} and a coinsurance of {c * 100:.0f}%, but no policy limit.")
    elif d == 0 and u < float('inf') and c != 1:
        print(
            f"\n{sim_phrase} subject to a policy limit of ${u:,} and a coinsurance of {c * 100:.0f}%, but no deductible.")
    elif d > 0 and u < float('inf') and c != 1:
        print(
            f"\n{sim_phrase} subject to a deductible of ${d:,}, a policy limit of ${u:,}, and a coinsurance of {c * 100:.0f}%.")

    # CLAIM DISTRIBUTION SUMMARY
    if dist_name == 'uniform':
        print(
            f"{claim_intro} a Uniform distribution with lower bound = {dist_params['a']:,} and upper bound = {dist_params['b']:,}.")
    elif dist_name == 'exponential':
        print(f"{claim_intro} an Exponential distribution with mean β = {dist_params['beta']:,}.")
    elif dist_name == 'gamma':
        print(
            f"{claim_intro} a Gamma distribution with scale parameter θ = {dist_params['theta']:,} and shape parameter α = {dist_params['alpha']:,}.")
    elif dist_name == 'normal':
        print(
            f"{claim_intro} a Normal distribution with mean μ = {dist_params['mean']:,} and standard deviation σ = {dist_params['std']:,}.")
    elif dist_name == 'lognormal':
        print(
            f"{claim_intro} a Lognormal distribution with parameters μ = {dist_params['mu']:,} and σ = {dist_params['sigma']:,}.")
    elif dist_name == 'beta' and dist_params['a'] == 0 and dist_params['b'] == 1:
        print(
            f"{claim_intro} a Beta distribution with parameters α = {dist_params['α']:,} and β = {dist_params['β']:,}.")
    elif dist_name == 'beta':
        print(
            f"{claim_intro} a Beta distribution rescaled to the interval [{dist_params['a']:,}, {dist_params['b']:,}], with parameters α = {dist_params['α']:,} and β = {dist_params['β']:,}.")

    all_below_deductible = all(x <= info['deductible'] for x in losses)
    coinsurance_is_zero = info['coinsurance_rate'] == 0
    expected_close_to_zero = expected_total < 0.01
    total_payment_close_to_zero = total_payment < 0.01
    a_e_ratio = total_payment/expected_total

    if expected_total == 0:
        percent_error = float('nan')  # or set to 0.0 or display a message
    else:
        percent_error = (abs(total_payment - expected_total) / expected_total) * 100

    # CONSIDERING EDGE CASES

    print(f"\nPayment Results:")

    # Case 1: All claims below deductible
    if all_below_deductible:
        print(f"\nAll simulated claims were below the deductible.")
        print(f"Total actual claim payment: $0.00")
        print(f"Expected claim payment: less than $0.01")
        print(f"Difference: ${abs(total_payment - expected_total):,.2f}")
        if np.isnan(percent_error):
            print("Percent error: undefined (expected payment is $0.00)")
        else:
            print(f"Percent error: {percent_error:,.2f}%")
        print(f"Margin of error on expected payment: ±${total_error:,.2f}")

        print("\nThis usually happens when:\n")
        print("  • The deductible is set near the tail of the distribution, and/or")
        print("  • The mean of the distribution is below the deductible.")

        print("\n→ Review your deductible and distribution parameters.")

    # Case 2: Both expected and actual payments near zero
    elif expected_close_to_zero and total_payment_close_to_zero:
        print(f"\nBoth the total actual claim payment and expected claim payment are less than $0.01.")

        print("\nThis usually occurs when:\n")
        print("  • The deductible is near the tail of the distribution, and/or")
        print("  • Almost all simulated claims fall below the deductible.")

    # Case 3: Expected payment near zero, but actual payment not
    elif expected_close_to_zero and not total_payment_close_to_zero:
        print(f"\nExpected claim payment: less than $0.01.")
        print(f"Total actual claim payment: ${total_payment:,.2f}")
        print(f"Difference: ${abs(total_payment - expected_total):,.2f}")
        if np.isnan(percent_error):
            print("Percent error: undefined (expected payment is $0.00)")
        else:
            print(f"Percent error: {percent_error:,.2f}%")

        print(f"Margin of error on expected payment: ±${total_error:,.2f}")

    # Case 4: Actual payment near zero, but expected payment not
    elif not expected_close_to_zero and total_payment_close_to_zero:
        print(f"\nTotal actual claim payment: less than $0.01")
        print(f"Total expected claim payment: ${expected_total:,.2f}")
        print(f"Difference: ${abs(total_payment - expected_total):,.2f}")
        if np.isnan(percent_error):
            print("Percent error: undefined (expected payment is $0.00)")
        else:
            print(f"Percent error: {percent_error:,.2f}%")
        print(f"Margin of error on expected payment: ±${total_error:,.2f}")

    # Case 5: Coinsurance is zero
    elif coinsurance_is_zero:
        print(f"\nBoth the total actual claim payment and expected claim payment are $0.00.")

        print("\nReason:\n")
        print("  • The coinsurance rate is 0%, so the insurer pays nothing.")

    # PAYMENT SUMMARY (default case)
    else:

        print(f"\nTotal actual claim payment: ${total_payment:,.2f}")
        print(f"Total expected claim payment: ${expected_total:,.2f}")
        print(f"Difference: ${abs(total_payment - expected_total):,.2f}")

        if np.isnan(percent_error):
            print("Percent error: undefined (expected payment is $0.00)")
        else:
            print(f"Percent error: {percent_error:,.2f}%")

        if a_e_ratio > 1:
            print(f"The A/E ratio is {a_e_ratio*100:.2f}%, meaning that actual payments are higher than expected.")
        else:
            print(f"The A/E ratio is {a_e_ratio*100:.2f}%, meaning that actual payments are lower than expected.")

        print(f"Margin of error on expected payment: ±${total_error:,.2f}")


    if integration_warning:
        print("\n⚠️  Warning: The calculation of the expected payment encountered convergence issues.")
        print( "  • This may occur when integrating in the tail of a distribution (such as the Lognormal with large parameters).")
        print("  • The expected value shown may be inaccurate.")
        print("  • Large margin of error: the numerical integral failed to meet the required tolerance.")
        print( "\n→ Consider using different parameters and/or reducing the integration domain by adjusting the policy characteristics for a better approximation of the expected payment.")



