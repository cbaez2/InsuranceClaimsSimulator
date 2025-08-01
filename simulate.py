# simulate.py
import numpy as np
from scipy.stats import uniform, expon, gamma, norm, lognorm, beta
from payment import payment


def simulate_losses(info, dist_name, dist_params):

    n_claims = info["n_claims"]

    if dist_name == 'uniform':
        losses= uniform.rvs(loc=dist_params['a'], scale=dist_params['b']-dist_params['a'], size=n_claims)

    elif dist_name == 'exponential':
        losses= expon.rvs(scale=dist_params['beta'], size=n_claims)

    elif dist_name == 'gamma':
        losses= gamma.rvs(scale=dist_params['theta'], a=dist_params['alpha'], size=n_claims)

    elif dist_name == 'normal':
        losses= norm.rvs(scale=dist_params['std'], loc= dist_params["mean"], size=n_claims)

    elif dist_name == 'lognormal':
        losses= lognorm.rvs(s=dist_params['sigma'], scale= np.exp(dist_params['mu']), size=n_claims)

    elif dist_name == 'beta':
        a = float(dist_params['a'])
        b = float(dist_params['b'])
        α = dist_params['α']
        β_ = dist_params['β']  # renamed to avoid confusion with scipy.beta

        losses = beta.rvs(a=α, b=β_, loc=a, scale=b - a, size=n_claims)

    v_payments= np.vectorize(lambda x: (payment(x,info)))
    payments= v_payments(losses)

    return losses, payments #returns simulated losses and payments


