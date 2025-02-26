def sum_intervals(intervals):
    """
    Calculate the sum of interval lengths, counting overlapping intervals only once.

    Args:
        intervals: List of intervals, where each interval is a list [start, end]

    Returns:
        The sum of the lengths of all intervals, counting overlapping intervals only once
    """
    if not intervals:
        return 0

    # Sort intervals by their start value
    sorted_intervals = sorted(intervals)

    # Initialize with the first interval
    merged = [sorted_intervals[0]]

    for current in sorted_intervals[1:]:
        # Get the last merged interval
        previous = merged[-1]

        # If current interval overlaps with the last merged interval, update the end of the merged interval if needed
        if current[0] <= previous[1]:
            merged[-1] = [previous[0], max(previous[1], current[1])]
        else:
            # No overlap, add the current interval to merged
            merged.append(current)

    # Calculate the sum of the lengths of the merged intervals
    total_length = sum(end - start for start, end in merged)

    return total_length