def compare_batching(requests: list, max_batch_size: int, time_per_step: float) -> dict:
    """
    Simulate and compare static vs continuous batching strategies for LLM serving.
    
    Args:
        requests: List of integers, each representing decode steps for a request
        max_batch_size: Maximum concurrent requests the GPU can handle
        time_per_step: Time in milliseconds for one decode step
    
    Returns:
        Dictionary with performance metrics for both strategies
    """
    # Your code here
    static_time = 0
    static_idle = 0
    continuous_time = 0
    cointinuous_idle = 0
    for i in range(0, len(requests), max_batch_size):
        batch = requests[i:i+max_batch_size]
        time = max(batch) * time_per_step
        static_time += time
        for req in batch:
            static_idle += max(batch) - req
        if(len(batch) < max_batch_size):
            static_idle += max(batch) * (max_batch_size - len(batch))

    continuos_batch = requests[:max_batch_size]
    i = max_batch_size
    while(True):
        min_time = min(continuos_batch)
        continuos_batch = [x - min_time for x in continuos_batch]
        continuos_batch = [x for x in continuos_batch if x != 0]
        continuous_time += min_time * time_per_step
        space = max_batch_size - len(continuos_batch)
        while((i < len(requests)) and (space)):
            continuos_batch.append(requests[i])
            i += 1
            space -= 1
        if(i == len(requests)):
            continuous_time += max(continuos_batch) * time_per_step
            for req in continuos_batch:
                cointinuous_idle += max(continuos_batch) - req
            break
    return {
    'static_total_time': round(static_time, 4),
    'continuous_total_time': round(continuous_time, 4),

    'static_throughput': round(len(requests) * 1000 / static_time, 4),
    'continuous_throughput': round(len(requests) * 1000 / continuous_time, 4),

    'static_gpu_utilization': round(
        1 - (static_idle / (static_time * max_batch_size)), 4
    ),

    'continuous_gpu_utilization': round(
        1 - (cointinuous_idle / (continuous_time * max_batch_size)), 4
    ),

    'speedup': round(
        (len(requests) * 1000 / continuous_time) /
        (len(requests) * 1000 / static_time),
        4
    )
}


