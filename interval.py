def sum_intervals(intervals):
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


def sum_intervals(intervals):
    if not intervals:
        return 0  # Edge case: Empty list

    # Sort intervals by the start value
    intervals.sort()

    total_length = 0
    start, end = intervals[0]  # Initialize with the first interval

    for s, e in intervals[1:]:
        if s <= end:  # Overlapping interval, merge it
            end = max(end, e)
        else:  # Non-overlapping, count previous and move to the new one
            total_length += end - start
            start, end = s, e

    # Add the last interval
    total_length += end - start

    return total_length


def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a,b in sorted(intervals):
        if top < a: top    = a
        if top < b: s, top = s+b-top, b
    return s

