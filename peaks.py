def pick_peaks(arr):
    peaks = {"pos": [], "peaks": []}

    if len(arr) < 3:  # No peak can exist in arrays smaller than 3 elements
        return peaks

    for i in range(1, len(arr) - 1):  # Iterate from the second element to the second last
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:  # Normal peak
            peaks["pos"].append(i)
            peaks["peaks"].append(arr[i])
        elif arr[i] > arr[i - 1] and arr[i] == arr[i + 1]:  # Potential plateau peak
            j = i
            while j < len(arr) - 1 and arr[j] == arr[j + 1]:  # Move to the end of plateau
                j += 1
            if j < len(arr) - 1 and arr[j] > arr[j + 1]:  # Peak exists at start of plateau
                peaks["pos"].append(i)
                peaks["peaks"].append(arr[i])

    return peaks







def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}
