import math


# Return distance between 2 points
def euclid_dist(pair1, pair2):
    x1, y1 = pair1
    x2, y2 = pair2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Select candidates for the vertical strip
def select_candidates(l, r, d, xmid):
    j = 0
    for i in range(l, r):
        if abs(Q[i].x - xmid) <= d:
            j += 1
            R[j] = Q[i]
    return R

# Checking the vertical strip
def check_strip(R, d):
    t = len(R)
    delta = d
    for j in range(1, t-1):
        for k in range(k+1, min(t, j + 7)):
            x1 = R[j].x
            x2 = R[k].x
            y1 = R[j].y
            y2 = R[k].y
            delta = min(delta, euclid_dist((x1,y1), (x2,y2)))
    return delta

def closest_pair(l, r):
    if l == r:
        return -1
    m = (l + r) / 2
    delta_l = closest_pair(l, m)
    delta_r = closest_pair(m+1, r)
    delta = min(delta_l, delta_r)
    merge(l, m, r)
    R = select_candidates(l, r, delta, Q[m].x)
    delta = check_strip(R, delta)
    return delta
