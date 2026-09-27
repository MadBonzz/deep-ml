import numpy as np
import math

def calculate_latency_percentiles(latencies: list[float]) -> dict[str, float]:
    """
    Calculate P50, P95, and P99 latency percentiles.
    
    Args:
        latencies: List of latency measurements
    
    Returns:
        Dictionary with keys 'P50', 'P95', 'P99' containing
        the respective percentile values rounded to 4 decimal places
    """
    # Your code here
    latencies.sort()
    output = {
        'P50': 0.0,
        'P95': 0.0,
        'P99': 0.0
    }

    percentiles = [0.5, 0.95, 0.99]

    if(len(latencies) == 1):
        for key in output.keys():
            output[key] = latencies[0]

    if(len(latencies) > 1):
        h_s = [percentile * (len(latencies) - 1) for percentile in percentiles]
        i_s = [math.floor(h) for h in  h_s]
        f_s = [h - i for h,i in zip(h_s, i_s)]
        output['P50'] = round(latencies[i_s[0]] + f_s[0] * (latencies[i_s[0] + 1] - latencies[i_s[0]]), 4)
        output['P95'] = round(latencies[i_s[1]] + f_s[1] * (latencies[i_s[1] + 1] - latencies[i_s[1]]), 4)
        output['P99'] = round(latencies[i_s[2]] + f_s[2] * (latencies[i_s[2] + 1] - latencies[i_s[2]]), 4)
    return output

