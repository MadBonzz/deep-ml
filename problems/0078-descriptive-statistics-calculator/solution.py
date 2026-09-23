import numpy as np
import math

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    def get_median(data):
        N = len(data)
        if N % 2 == 0:
            median = (data[N//2] + data[(N//2)-1]) / 2
        else:
            median = data[(N-1) // 2]
        return median
    if isinstance(data, np.ndarray):
        data = data.tolist()
    N = len(data)
    mean = sum(data) / N
    median = get_median(data)
    variance = 0
    counts = {}
    for i in data:
        variance += (i - mean) ** 2
        counts[i] = counts.get(i, 0) + 1
    variance /= N
    std = variance ** 0.5
    max_count = -1
    mode = None
    for k, v in counts.items():
        if v > max_count:
            mode = k
            max_count = v
    q1 = data[math.ceil(0.25*N)-1]
    q3 = data[math.ceil(0.75*N)-1]
    # if(N % 2 == 0):
    #     q1 = get_median(data[:N//2])
    #     q3 = get_median(data[N//2:])
    # else:
    #     q1 = get_median(data[:(N-1)//2])
    #     q3 = get_median(data[(N+1)//2:])
    iqr = q3 - q1

    return {
    'mean': mean,
    'median': float(median),
    'mode': mode,
    'variance': variance,
    'standard_deviation': std,
    '25th_percentile': float(q1),
    '50th_percentile': float(median),
    '75th_percentile': float(q3),
    'interquartile_range': float(iqr)
    }