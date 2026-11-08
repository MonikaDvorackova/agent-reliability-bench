"""Wilson confidence intervals for observed binary benchmark rates."""
import math

def wilson_interval(successes, trials, z=1.959963984540054):
    if not isinstance(trials, int) or not isinstance(successes, int) or trials <= 0 or not 0 <= successes <= trials or z <= 0:
        raise ValueError("Invalid counts or z-score")
    p = successes / trials
    denominator = 1 + z*z/trials
    center = (p + z*z/(2*trials)) / denominator
    radius = z*math.sqrt(p*(1-p)/trials + z*z/(4*trials*trials))/denominator
    return max(0.0, center-radius), min(1.0, center+radius)
