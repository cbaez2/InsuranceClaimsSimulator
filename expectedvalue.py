#expectedvalue
from scipy.integrate import quad
from payment import payment
from scipy.stats import uniform, expon, gamma, norm, lognorm, beta
import numpy as np
import warnings
from scipy.integrate import IntegrationWarning

def get_pdf_and_bounds(dist_name, dist_params):
    if dist_name == 'uniform':
        a, b = dist_params['a'], dist_params['b']
        return lambda x: uniform.pdf(x, loc=a, scale=b - a), a, b #returning the mathematical expression of the uniform pdf to integrate it later on

    elif dist_name == 'exponential':
        beta_ = dist_params['beta']
        return lambda x: expon.pdf(x, scale=beta_), 0, 10*beta_

    elif dist_name == 'gamma':
        α, θ = dist_params['alpha'], dist_params['theta']
        return lambda x: gamma.pdf(x, a=α, scale=θ), 0, 10 * α * θ

    elif dist_name == 'normal':
        μ, σ = dist_params['mean'], dist_params['std']
        return lambda x: norm.pdf(x, loc=μ, scale=σ), μ - 5 * σ, μ + 5 * σ

    elif dist_name == 'lognormal':
        μ, σ = dist_params['mu'], dist_params['sigma']
        return lambda x: lognorm.pdf(x, s=σ, scale=np.exp(μ)), 0, np.exp(μ + 5 * σ)

    elif dist_name == 'beta':
        a, b = dist_params['a'], dist_params['b']
        α, β_ = dist_params['α'], dist_params['β']
        return lambda x: beta.pdf(x, a=α, b=β_, loc=a, scale=b - a), a, b

def expected_payment(info, dist_name, dist_params):  #defining function to do expected payment
    f_X, lower, upper = get_pdf_and_bounds(dist_name, dist_params)  #defining variables to save PDF and its bounds
    integrand = lambda x: payment(x, info) * f_X(x)   #defining integrand as mathematical function
    warning_occurred = False   #by default warning_occurred is defined as a boolean value.

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("ignore", IntegrationWarning)  # suppress display
        warnings.simplefilter("always", IntegrationWarning)  # capture silently

        result, error = quad(integrand, lower, upper, limit=1000)

        for warn in w:  #consdering case in which theres a warning
            if issubclass(warn.category, IntegrationWarning):
                warning_occurred = True
                break

    return result, error, warning_occurred  #returns the integral result, margin of error, and boolean value in case if there's a warning

