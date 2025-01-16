def bouncing_ball(h, bounce, window):
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    count = 1
    while h * bounce > window:
        h *= bounce
        count += 2
    return count