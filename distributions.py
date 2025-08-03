#distributions.py_
def get_uniform_bounds():
    while True:
        try:
            a= float(input("Enter the lower bound 'a' for the Uniform distribution: "))
            break
        except ValueError:
            print("Please enter a numeric value for lower bound 'a'.")

    while True:
        try:
            b= float(input("Enter the upper bound 'b' for the Uniform distribution: "))
            if b>a:
                break
            print(f"The upper bound 'b' must be greater than the lower bound {a:,}.")
        except ValueError:
            print("Please enter a numeric value for upper bound 'b'.")
    return a,b

def get_uniform_parameters(info): #getting adjusted bounds (that happen to be the parameters)
    d= info['deductible']
    u= info['policy_limit']

    while True:
        a, b = get_uniform_bounds()  # ASK FOR BOUNDS
        if d>0 and u < float('inf'):   #both policy limit and deductible given
            if a<=d < u<=b:
                break
            print(f"\nBoth the deductible and limit must satisfy this inequality: a ≤ deductible < limit ≤ b → [{a:,} ≤ {d:,} < {u:,} ≤ {b:,}]")

        elif d>0 and u == float('inf'): #only deductible is given
            if a<=d<b:
                break
            print(f"\nThe deductible must satisfy this inequality: a ≤ deductible < b → [{a:,} ≤ {d:,} < {b:,}]")

        elif u < float('inf') and d == 0: #only policy limit is given
            if a<u<=b:
                break
            print(f"\nThe policy limit must satisfy this inequality: a < policy limit ≤ b → [{a:,} < {u:,} ≤ {b:,}]")
        else:
            break #no deductible nor policy limit
    if d == a:
        print(f"\n⚠️ Warning: The deductible equals the minimum possible loss. Since losses cannot be less than ${a:,}, the insurer will pay for all losses except when the loss is exactly ${a:,}.")

    if u == b:
        print("\n⚠️ Warning: The policy limit equals the maximum possible loss so it will not cap any losses.")
    return {'a':a,'b':b}


def get_exponential_parameter():
    while True:
        try:
            beta = float(input("Enter the mean β for the Exponential distribution: "))
            if beta > 0:
                return {'beta':beta}
            print("Please enter a positive mean β.")
        except ValueError:
            print("Please enter a positive value for mean β.")


def get_gamma_parameters():
    while True:
        try:
            alpha = float(input("Enter the shape parameter α for the Gamma distribution: "))
            if alpha>0:
                break
            print("Please enter a positive shape parameter α.")
        except ValueError:
            print("Please enter a positive shape parameter α.")

    while True:
        try:
            theta = float(input("Enter the scale parameter θ for the Gamma distribution: "))
            if theta > 0:
                break
            print("Please enter a positive scale parameter θ.")
        except ValueError:
            print("Please enter a positive scale parameter θ.")

    return {'alpha':alpha,'theta':theta}

def get_normal_parameters():
    while True:
        try:
            mean= float(input("Enter the mean μ for the Normal distribution: "))
            break
        except ValueError:
            print("Please enter a numeric value for the mean μ.")

    while True:
        try:
            std= float(input("Enter the standard deviation σ for the Normal distribution: "))
            if std>0:
                break
            print("Please enter a positive standard deviation σ.")
        except ValueError:
            print("Please enter a positive standard deviation σ.")
    return {'mean':mean,'std':std}

def get_lognormal_parameters():
    while True:
        try:
            mu= float(input("Enter the parameter μ for the Lognormal distribution: "))
            if -10<=mu<=10:
                break
            print("Please enter a value between [-10, 10] for parameter μ. A large μ will crash the simulation.")
        except ValueError:
            print(f"Please enter a numeric value for parameter μ.")
    while True:
        try:
            sigma= float(input("Enter the parameter σ for the Lognormal distribution: "))
            if 0<sigma<=5:
                break
            print("Please enter a value between (0,5] for parameter σ. A large σ will crash the simulation.")
        except ValueError:
            print("Please enter a value between (0,5] for parameter σ. A large σ will crash the simulation.")

    return {'mu': mu, 'sigma': sigma}

def get_distribution_choice():
    while True:
        dist = input("Choose one of the following: Uniform, Exponential, Gamma, Normal, Lognormal, Beta: ").strip().lower()
        if dist.lower() in ['uniform', 'exponential', 'gamma', 'normal', 'lognormal', 'beta']:
            return dist
        print("Please enter one of the six supported distributions: ")

def get_beta_bounds(info):

    while True:
        try:
            a = float(input("Enter the minimum loss amount: "))
            if a>=0:
                break
            print("Please enter a non-negative value for the minimum loss amount.")
        except ValueError:
            print("Please enter a non-negative value for the minimum loss amount.")

    while True:
        try:
            b = float(input("Enter the maximum loss amount: "))
            if b>a:
                break
            print(f"The maximum loss amount must be greater than the minimum loss amount of ${a:,}.")
        except ValueError:
            print("Please enter a numeric value for the maximum loss amount.")
    return a,b

def beta_adjusted_bounds(info):
    d= info['deductible']
    u=info['policy_limit']

    if d > 0 and u < float('inf') and 0 <= d < u <= 1: #both deductible and policy limit and both are between [0,1]
        a, b = 0, 1

    elif d > 0 and u == float('inf') and 0 <= d < 1: #only deductible and in between [0,1]
        a, b = 0, 1

    elif d == 0 and u < float('inf') and 0 < u <= 1: #only policy limit and in between [0,1]
        a, b = 0, 1

    elif d == 0 and u == float('inf'):    #no deductible nor limit
        a,b = 0,1


    #cases to adjust
    else:
        # print warning when the range is not on [0,1]
        print("\n⚠️ The Beta distribution is only defined on the interval [0,1].")
        print("Your deductible and/or policy limit are outside that range.")
        print("Enter the minimum and maximum loss amounts to rescale the Beta distribution.")

        while True:
            a, b = get_beta_bounds(info) #ASK for bounds
            if d>0 and u < float('inf'):   #both deductible and policy limit are given
                if a<= d < u <=b:
                    print(f"\nThe Beta distribution has been successfully rescaled to the interval [{a:,}, {b:,}].")
                    break
                print(f"\nBoth the deductible and limit must satisfy this inequality: min ≤ deductible < limit ≤ max → [{a:,} ≤ {d:,} < {u:,} ≤ {b:,}]")

            elif d>0 and u == float('inf'): #only deductible is given
                if a<=d<b:
                    print(f"\nThe Beta distribution has been successfully rescaled to the interval [{a:,}, {b:,}].")
                    break
                print(f"\nThe deductible must satisfy this inequality: min ≤ deductible < max → [{a:,} ≤ {d:,} < {b:,}]")

            elif u < float('inf') and d == 0: #only policy limit is given
                if a<u<=b:
                    print(f"\nThe Beta distribution has been successfully rescaled to the interval [{a:,}, {b:,}].")
                    break
                print(f"\nThe policy limit must satisfy this inequality: min < policy limit ≤ max → [{a:,} < {u:,} ≤ {b:,}]")

        if d == a:
            print(f"\n⚠️ Warning: The deductible equals the minimum possible loss. Since losses cannot be less than ${a:,}, the insurer will pay for all losses except when the loss is exactly ${a:,}.")

        if u == b:
            print("\n⚠️ Warning: The policy limit equals the maximum possible loss so it will not cap any losses.")
    return a,b

def get_beta_parameters(info):
    d= info['deductible']
    u= info['policy_limit']

    a, b = beta_adjusted_bounds(info)

    # Ask for alpha and beta parameters
    while True:
        try:
            α = int(input("Enter the parameter α for the Beta distribution: "))
            if α > 0:
                break
            print("Please enter a positive integer for parameter α.")
        except ValueError:
            print("Please enter a positive integer for parameter α.")

    while True:
        try:
            β = int(input("Enter the parameter β for the Beta distribution: "))
            if β > 0:
                break
            print("Please enter a positive integer for parameter β.")
        except ValueError:
            print("Please enter a positive integer for parameter β.")

    return {"α": α, "β": β, "a": a, "b": b}

def get_distribution_parameters(dist, info):
    if dist == 'uniform':
        return get_uniform_parameters(info)
    elif dist == 'exponential':
        return get_exponential_parameter()
    elif dist == 'gamma':
        return get_gamma_parameters()
    elif dist == 'normal':
        return get_normal_parameters()
    elif dist == 'lognormal':
        return get_lognormal_parameters()
    elif dist == 'beta':
        return get_beta_parameters(info)
