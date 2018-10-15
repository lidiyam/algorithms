

# pref_m[m_i]: list of woman in order of preference
# pref_w[w_i]: dict of man, preference as a value
def gale_shapley(unengaged_man, woman, pref_m, pref_w):
    match = {}

    while unengaged_man:
        m_i = unengaged_man.pop(0)
        while pref_m[m_i]:
            w_j = pref_m[m_i].pop(0)
            if w_j not in match:
                match[w_j] = m_i
                break
            else:
                m_k = match[w_j]
                if pref_w[w_j][m_i] < pref_w[w_j][m_k]:
                    match[w_j] = m_i
                    unengaged_man.push(m_k)
                    break
    return match


if __name__ == '__main__':
    M = ['Bob', 'Dan', 'Steve']
    W = ['Lily', 'Lisa', 'Ann']
    pref = {
        'Bob': [1, 2, 3],
        'Dan': [3, 1, 2],
        'Steve': [1, 2, 3],
        'Lily': [1, 2, 3],
        'Lisa': [2, 1, 3],
        'Ann': [3, 1, 2]
    }
