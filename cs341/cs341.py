#!/usr/bin/env python3

from heapq import heappush, heappop

import random

# Practice for the final exam

###
### Algorithms
###

### Part 1: Divide and conquer

def select_sort(A):
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    L = merge_sort(A[:n//2])
    R = merge_sort(A[n//2:])

    combined = []
    a = 0
    b = 0
    for i in range(n):
        if a >= len(L):
            combined.append(R[b])
            b += 1
        elif b >= len(R):
            combined.append(L[a])
            a += 1
        elif L[a] < R[b]:
            combined.append(L[a])
            a += 1
        else:
            combined.append(R[b])
            b += 1

    return combined

def linear_search(A, x):
    for i in range(len(A)):
        if A[i] == x:
            return True
    return False

def dc_search(A, x):
    n = len(A)

    if n == 0:
        return False
    if n == 1:
        return A[0] == x

    return dc_search(A[:n//2], x) or dc_search(A[n//2:], x)

def naive_select(A, k):
    n = len(A)
    assert k < n

    A.sort()
    return A[k]

def quick_select(A, k):
    n = len(A)
    assert k < n
    
    if n == 1:
        return A[0]

    p = random.randint(0, n - 1)
    L = [A[i] for i in range(n) if i != p and A[i] <= A[p]]
    R = [A[i] for i in range(n) if i != p and A[i] > A[p]]
    if len(L) == k:
        return A[p]
    if len(L) < k:
        return quick_select(R, k - len(L) - 1)
    return quick_select(L, k)

def mom_select(A, k):
    n = len(A)
    assert k < n
    
    if n == 1:
        return A[0]

    M = []
    i = 0
    while i < n:
        j = min(i + 5, n)
        M.append(naive_select(A[i:j], (j - i) // 2))
        i += 5

    p = A.index(mom_select(M, len(M) // 2))
    L = [A[i] for i in range(n) if i != p and A[i] <= A[p]]
    R = [A[i] for i in range(n) if i != p and A[i] > A[p]]
    if len(L) == k:
        return A[p]
    if len(L) < k:
        return mom_select(R, k - len(L) - 1)
    return mom_select(L, k)

def dominates(p, q):
    return p[0] > q[0] and p[1] > q[1]

def dist_sq(p, q):
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def naive_2d_maxima(P):
    return {p for p in P if not any(dominates(q, p) for q in P)}

def dc_2d_maxima(P):
    P.sort()

    def go(P):
        n = len(P)

        if n == 0:
            return set()
        if n == 1:
            return {P[0]}

        ML = go(P[:n//2])
        MR = go(P[n//2:])

        right_max_y = max(p[1] for p in MR)
        return MR | {p for p in ML if p[1] > right_max_y}

    return go(P)

def naive_closest_pair(P):
    n = len(P)
    assert n >= 2

    pair = None
    dist = float('inf')

    for i, p in enumerate(P):
        for q in P[i+1:]:
            d = dist_sq(p, q)
            if d < dist:
                dist = d
                pair = (p, q)

    return pair

def dc_closest_pair(P):
    P.sort()

    def go(P):
        n = len(P)
        assert n >= 2

        if n == 2:
            return (P[0], P[1])
        if n == 3:
            return min([(P[0], P[1]), (P[0], P[2]), (P[1], P[2])],
                       key=lambda p: dist_sq(*p))

        pairL = go(P[:n//2])
        pairR = go(P[n//2:])

        mid_x = P[n//2][0]
        delta = min(dist_sq(*pairL), dist_sq(*pairR))
        S = [p for p in P if abs(p[0] - mid_x) <= delta]
        S.sort(key=lambda p: p[1])

        pairS = None
        dist = float('inf')
        for i, p in enumerate(S):
            j = i + 1
            while j < len(S) and S[j][1] - S[i][1] < delta:
                d = dist_sq(S[i], S[j])
                if d < dist:
                    dist = d
                    pairS = (S[i], S[j])
                j += 1

        return min((pairL, pairR, pairS), key=lambda p: dist_sq(*p))

    return go(P)

### Part 2: Greedy algorithms

def activity_selection(R):
    result = []
    R.sort(key=lambda r: r[1])
    for s, f in R:
        if not result or s >= result[-1][1]:
            result.append((s, f))
    return result

def job_scheduling(J):
    J.sort()
    return J

def weighted_job_scheduling(J):
    J.sort(key=lambda job: job[0] / job[1])
    return J

def stable_marriage(M, W):
    assert len(M) == len(W)
    n = len(M)

    def prefers(w, m1, m2):
        ranks = W[w]
        return m1 in ranks and ranks.index(m1) < ranks.index(m2)

    free_men = list(M.keys())
    women_to_men = {}
    while free_men:
        m = free_men.pop(0)
        w = M[m].pop(0)
        if w in women_to_men:
            current = women_to_men[w]
            if prefers(w, m, current):
                women_to_men[w] = m
                free_men.append(current)
            else:
                free_men.append(m)
        else:
            women_to_men[w] = m

    return {(m, w) for w, m in women_to_men.items()}

### Part 3: Dynamic programming

def lin_ind_set(V):
    n = len(V)

    if n == 0:
        return [], 0
    if n == 1:
        return [0], V[0]

    A = [0] * n

    # Base cases
    A[0] = V[0]
    A[1] = max(V[0], V[1])

    # Bottom-up iterative solution
    for i in range(2, n):
        A[i] = max(A[i-1], A[i-2] + V[i])

    # Backtrack to get optimal subset
    S = []
    i = n - 1
    while i >= 0:
        if i != 0 and A[i] == A[i-1]:
            i -= 1
        else:
            S.insert(0, i)
            i -= 2

    assert sum(V[i] for i in S) == A[-1]
    return S, A[-1]

def seq_alignment(X, Y, alpha, delta):
    m = len(X)
    n = len(Y)

    C = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        C[i][0] = i * delta
    for j in range(n + 1):
        C[0][j] = j * delta

    # Bottom-up iterative solution
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            C[i][j] = min(
                C[i-1][j] + delta,
                C[i][j-1] + delta,
                C[i-1][j-1] + alpha(X[i-1], Y[j-1]))

    # Backtrack
    seq_x = []
    seq_y = []
    i = m
    j = n
    while i > 0 and j > 0:
        if C[i][j] == C[i-1][j] + delta:
            seq_x.insert(0, X[i-1])
            seq_y.insert(0, '-')
            i -= 1
        elif C[i][j] == C[i][j-1] + delta:
            seq_x.insert(0, '-')
            seq_y.insert(0, Y[j-1])
            j -= 1
        else:
            assert C[i][j] == C[i-1][j-1] + alpha(X[i-1], Y[j-1])
            seq_x.insert(0, X[i-1])
            seq_y.insert(0, Y[j-1])
            i -= 1
            j -= 1
    assert i == 0 or j == 0
    while i > 0:
        seq_x.insert(0, X[i-1])
        seq_y.insert(0, '-')
        i -= 1
    while j > 0:
        seq_x.insert(0, '-')
        seq_y.insert(0, Y[j-1])
        j -= 1

    def calc_cost(x, y):
        if x == '-' or y == '-':
            return delta
        return alpha(x, y)

    cost = sum(calc_cost(x, y) for x, y in zip(seq_x, seq_y))
    assert cost == C[m][n]

    return "".join(seq_x), "".join(seq_y), cost

def optimal_parens(D):
    n = len(D) - 1
    assert n >= 1
    
    C = [[0] * n for _ in range(n)]

    # Base case: C[i][i] == 0 for i from 0 to n-1

    # Bottom-up iterative solution
    for i in range(n, -1, -1):
        for j in range(i + 1, n):
            C[i][j] = min(
                C[i][k] + C[k+1][j] + D[i] * D[k+1] * D[j+1]
                for k in range(i, j))

    # Backtrack: too hard

    return C[0][n-1]

def value_activity_selection(R):
    n = len(R)
    if n == 0:
        return [], 0

    R.sort(key=lambda r: r[1])
    C = [0] * n

    # Base case
    C[0] = R[0][2]

    # Build helper array
    z = [0] * n
    for i in range(n):
        j = i - 1
        while j >= 0 and R[j][1] > R[i][0]:
            j -= 1
        z[i] = j

    # Bottom-up iterative solution
    for i in range(1, n):
        if z[i] == -1:
            C[i] = max(C[i-1], R[i][2])
        else:
            C[i] = max(C[i-1], C[z[i]] + R[i][2])

    # Backtrack
    i = n - 1
    schedule = []
    while i >= 0:
        if i > 0 and C[i] == C[i-1]:
            i -= 1
        else:
            schedule.insert(0, R[i])
            i = z[i]

    cost = sum(r[2] for r in schedule)
    assert cost == C[n-1]

    return schedule, cost

### Part 4: Graph algorithms

WHITE = 0
GREY = 1
BLACK = 2

def breadth_first_search(G, s):
    color = {v: WHITE for v in G}
    color[s] = GREY
    pi = {s: None}
    dist = {s: 0}

    queue = [s]
    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if color[v] == WHITE:
                color[v] = GREY
                pi[v] = u
                dist[v] = dist[u] + 1
                queue.append(v)
        color[u] = BLACK

    return color, pi, dist

def depth_first_search(G, s):
    color = {v: WHITE for v in G}
    pi = {s: None}
    time = 0
    finish_time = {}

    stack = [s]
    while stack:
        u = stack.pop()
        if color[u] == WHITE:
            color[u] = GREY
            stack.append(u)
            for v in G[u]:
                if color[v] == WHITE:
                    stack.append(v)
                    pi[v] = u
        elif color[u] == GREY:
            color[u] = BLACK
            finish_time[u] = time
            time += 1

    return color, pi, finish_time

def depth_first_search_rec(G, s=None):
    color = {v: WHITE for v in G}
    pi = {}
    time = 0
    finish_time = {}

    def visit(u):
        nonlocal time

        color[u] = GREY
        for v in reversed(G[u]):
            if color[v] == WHITE:
                pi[v] = u
                visit(v)
        color[u] = BLACK
        finish_time[u] = time
        time += 1

    if s:
        # Single source
        pi[s] = None
        visit(s)
    else:
        # DFS forest
        for s in G:
            if color[s] == WHITE:
                pi[s] = None
                visit(s)

    return color, pi, finish_time

def bipartition(G):
    seen = set()
    partition = {}
    for s in G:
        if not s in seen:
            color, _, dist = breadth_first_search(G, s)
            seen.update(v for v, c in color.items() if c == BLACK)
            for v, d in dist.items():
                partition[v] = d % 2

    for u in G:
        for v in G[u]:
            if partition[u] == partition[v]:
                return False

    return partition

def undirected_has_cycle(G):
    color = {v: WHITE for v in G}
    cycle = False

    def visit(u, p):
        nonlocal cycle
        if cycle:
            return

        color[u] = GREY
        for v in G[u]:
            if color[v] == WHITE:
                visit(v, u)
            elif v != p and color[v] == GREY:
                cycle = True
        color[u] = BLACK

    for s in G:
        if color[s] == WHITE:
            visit(s, None)
            if cycle:
                return True

    return cycle

def topological_sort(G):
    color = {v: WHITE for v in G}
    order = []
    dag = True

    def visit(u):
        nonlocal dag
        if not dag:
            return

        order.append(u)
        color[u] = GREY
        for v in G[u]:
            if color[v] == WHITE:
                visit(v)
            elif color[v] == GREY:
                dag = False
        color[u] = BLACK

    for s in G:
        if color[s] == WHITE:
            visit(s)
            if not dag:
                return False

    return order

def topological_sort_alt(G):
    in_degree = {v : 0 for v in G}
    for neighbours in G.values():
        for v in neighbours:
            in_degree[v] += 1

    queue = []
    for v in G:
        if in_degree[v] == 0:
            queue.append(v)

    order = []
    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in G[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) < len(G):
        return False
    return order

def reverse_graph(G):
    Grev = {v: [] for v in G}
    for u, neighbours in G.items():
        for v in neighbours:
            Grev[v].append(u)
    return Grev

def kosaraju(G):
    f = depth_first_search_rec(G)[2]
    Grev = reverse_graph(G)

    color = {v: WHITE for v in G}
    sccs = []

    def visit(u):
        color[u] = GREY
        sccs[-1].append(u)

        for v in Grev[u]:
            if color[v] == WHITE:
                visit(v)

        color[u] = BLACK

    for s in sorted(G.keys(), key=lambda v: f[v], reverse=True):
        if color[s] == WHITE:
            sccs.append([])
            visit(s)

    return sccs

def kruskal(G, w, s):
    mst = {v: [] for v in G}
    edges = sorted(w.keys(), key=lambda e: w[e])
    for u, v in edges:
        mst[u].append(v)
        mst[v].append(u)
        if undirected_has_cycle(mst):
            mst[u].pop()
            mst[v].pop()
    return breadth_first_search(mst, s)[1]

def prim(G, w, s):

    def get_weight(u, v):
        if (u, v) in w:
            return w[u, v]
        return w[v, u]

    pi = {s: None}
    connected = {s}

    pq = []
    for v in G[s]:
        heappush(pq, (get_weight(s, v), s, v))

    while pq:
        _, u, v = heappop(pq)
        assert u in connected

        if not v in connected:
            connected.add(v)
            pi[v] = u
            for z in G[v]:
                heappush(pq, (get_weight(v, z), v, z))

    return pi

def bfs_sssp(G, s):
    return breadth_first_search(G, s)[2]


def dijkstra(G, s, w=None):

    def get_weight(u, v):
        return w[u, v] if w else 1

    dist = {s: 0}
    entries = {}
    pq = []
    for v in G[s]:
        d = get_weight(s, v)
        entry = [d, v, True]
        dist[v] = d
        entries[v] = entry
        heappush(pq, entry)

    while pq:
        u_dist, u, valid = heappop(pq)
        if valid:
            for v in G[u]:
                new_dist = u_dist + get_weight(u, v)
                if not v in dist or new_dist < dist[v]:
                    dist[v] = new_dist
                    entry = [new_dist, v, True]
                    if v in entries:
                        entries[v][2] = False
                    entries[v] = entry
                    heappush(pq, entry)

    return dist

def dag_sssp(G, s, w=None):

    def get_weight(u, v):
        return w[u, v] if w else 1

    dist = {s: 0}
    order = topological_sort(G)
    assert order

    for u in order:
        for v in G[u]:
            new_dist = dist[u] + get_weight(u, v)
            if not v in dist or new_dist < dist[v]:
                dist[v] = new_dist

    return dist

def floyd_warshall(W):
    n = len(W)
    assert all(len(row) == n for row in W)

    D = [row[:] for row in W]
    E = [[0] * n for _ in range(n)]

    for m in range(n):
        for i in range(n):
            for j in range(n):
                E[i][j] = min(D[i][j], D[i][m] + D[m][j])
        D, E = E, D

    return D

def complement_graph(G):
    return {u: [v for v in G if u != v and not v in G[u]] for u in G}

### Part 5: Intractability and undecidability

def clique_to_vertex_cover(G, k, vertex_cover):
    n = len(G)
    assert k <= n

    Gcomp = complement_graph(G)
    return vertex_cover(Gcomp, n - k)

###
### Tests
###

def test_sort(sort):
    assert sort([]) == []
    assert sort([1]) == [1]
    assert sort([1, 2, 3]) == [1, 2, 3]
    assert sort([3, 2, 1]) == [1, 2, 3]
    assert sort([99, -1, 0, 0, 2, 42]) == [-1, 0, 0, 2, 42, 99]

def test_search(search):
    assert not search([], 1)
    assert not search([1], 2)
    assert not search([1, 3], 2)
    assert search([1], 1)
    assert search([1, 2], 1)
    assert search([2, 1], 1)
    assert search([1, 2, 3], 2)

def test_select(select):
    assert select([1], 0) == 1
    assert select([1, 2, 3], 0) == 1
    assert select([1, 2, 3], 1) == 2
    assert select([1, 2, 3], 2) == 3
    assert select([-100, 3, -3], 2) == 3
    assert select([5, 3, 2, 5, 2, 3, 3, 3, 4], 6) == 4

def test_2d_maxima(maxima):
    assert maxima([]) == set()
    assert maxima([(1, 1)]) == {(1,1)}
    assert maxima([(1, 1), (2, 2), (3, 3)]) == {(3, 3)}
    assert maxima([(3, 1), (2, 2), (1, 3)]) == {(3, 1), (2, 2), (1, 3)}
    assert (maxima([(1, 4), (4, 2), (2, -1), (0, 0), (2, 6)])
            == {(4, 2), (2, 6)})

def test_closest_pair(closest):
    assert closest([(0, 0), (0, 0)]) == ((0, 0), (0, 0))
    assert closest([(1, 2), (3, 4)]) == ((1, 2), (3, 4))
    assert closest([(0 ,0), (1, 2), (1, 0)]) == ((0, 0), (1, 0))
    assert closest([(0 ,0), (4, 2), (3, 7), (8, 8), (2, 3)]) == ((4, 2), (2, 3))

def test_activity_selection(activity):
    assert activity([]) == []
    assert activity([(1, 2)]) == [(1, 2)]
    assert activity([(1, 2), (1, 3), (2, 3), (3, 4)]) == [(1, 2), (2, 3), (3, 4)]
    assert (activity([(1, 4), (-1, 5), (2, 3), (5, 6), (4, 6), (5, 6)])
            == [(2, 3), (5, 6)])

def test_job_scheduling(schedule):
    assert schedule([]) == []
    assert schedule([1, 2, 3]) == [1, 2, 3]
    assert schedule([3, 2, 1]) == [1, 2, 3]

def test_weighted_job_scheduling(schedule):
    assert schedule([]) == []
    assert schedule([(1, 1), (2, 1), (3, 1)]) == [(1, 1), (2, 1), (3, 1)]
    assert schedule([(3, 1), (2, 1), (1, 1)]) == [(1, 1), (2, 1), (3, 1)]
    assert schedule([(1, 1), (1, 2), (1, 3)]) == [(1, 3), (1, 2), (1, 1)]
    assert schedule([(2, 3), (1, 4), (9, 3)]) == [(1, 4), (2, 3), (9, 3)]

def test_stable_marriage(marry):
    assert marry({}, {}) == set()
    assert (marry({"A": [1, 2], "B": [2, 1]}, {1: ["A", "B"], 2: ["B", "A"]})
            == {("A", 1), ("B", 2)})
    assert (marry({"A": [1, 2], "B": [1, 2]}, {1: ["A", "B"], 2: ["A", "B"]})
            == {("A", 1), ("B", 2)})
    assert (marry(
        {"A": [1, 2, 3], "B": [3, 1, 2], "C": [1, 3, 2]},
        {1: ["C", "A", "B"], 2: ["A", "C", "B"], 3: ["C", "A", "B"]})
        == {("A", 2), ("B", 3), ("C", 1)})

def test_lin_ind_set(ind_set):
    assert ind_set([]) == ([], 0)
    assert ind_set([100]) == ([0], 100)
    assert ind_set([1, 2, 3, 4]) == ([1, 3], 6)
    assert ind_set([3, 7, 9, 6]) == ([1, 3], 13)
    assert ind_set([3, 1, 1, 4, 1, 8, 7, 9, 11]) == ([0, 3, 5, 8], 26)

def test_seq_alignment(align):
    def alpha_fn(map):
        return lambda x, y: map.get(tuple(sorted([x, y])), 0)

    alpha1 = lambda x, y: 0
    alpha2 = lambda x, y: 1
    alpha3 = lambda x, y: int(x != y)
    alpha4 = alpha_fn({
        ("A", "G"): 1, ("A", "C"): 2, ("A", "T"): 10, ("C", "T"): 5})
    alpha5 = alpha_fn({
        ("A", "C"): 1, ("C", "T"): 2, ("G", "T"): 3})

    assert align("", "", alpha1, 0) == ("", "", 0)
    assert align("", "", alpha2, 10) == ("", "", 0)
    assert align("", "", alpha5, 99) == ("", "", 0)
    assert align("AAA", "AAA", alpha1, 0) == ("---AAA", "AAA---", 0)
    assert align("AAA", "AAA", alpha1, 1) == ("AAA", "AAA", 0)
    assert align("AAA", "AAA", alpha2, 0) == ("---AAA", "AAA---", 0)
    assert align("AAA", "AAA", alpha2, 2) == ("AAA", "AAA", 3)
    assert align("AAA", "AAA", alpha3, 0) == ("---AAA", "AAA---", 0)
    assert align("AAA", "AAA", alpha3, 1) == ("AAA", "AAA", 0)
    assert align("AGA", "GGT", alpha1, 0) == ("---AGA", "GGT---", 0)
    assert align("AGA", "GGT", alpha1, 1) == ("AGA", "GGT", 0)
    assert align("AGA", "GGT", alpha2, 2) == ("AGA", "GGT", 3)
    assert align("AGA", "GGT", alpha3, 0) == ("---AGA", "GGT---", 0)
    assert align("AGA", "GGT", alpha3, 1) == ("AGA", "GGT", 2)
    assert align("AGA", "GGT", alpha4, 1) == ("AG-A", "GGT-", 3)
    assert align("AGA", "GGT", alpha4, 2) == ("AG-A", "GGT-", 5)
    assert align("AGA", "GGT", alpha4, 4) == ("AG-A", "GGT-", 9)
    assert align("AGA", "GGT", alpha4, 5) == ("AG-A", "GGT-", 11)
    assert align("AGA", "GGT", alpha4, 6) == ("AGA", "GGT", 11)
    assert (align("AAGTACTC", "GAATTCCAG", alpha4, 1) ==
            ("-AAGT--ACTC", "GAATTCCAG--", 5))
    assert (align("AAGTACTC", "GAATTCCAG", alpha4, 2) ==
            ("-AAGTAC-TC", "GAATTCCAG-", 8))
    assert (align("AAGTACTC", "GAATTCCAG", alpha5, 1) ==
            ("AAGTAC-TC", "GAATTCCAG", 1))

def test_optimal_parens(parens):
    assert parens([1, 1]) == 0
    assert parens([100, 100]) == 0
    assert parens([1, 1, 1]) == 1
    assert parens([100, 100, 100]) == 1000000
    assert parens([10, 5, 10, 10]) == 1000

def test_value_activity_selection(select):
    assert select([]) == ([], 0)
    assert select([(0, 1, 5)]) == ([(0, 1, 5)], 5)
    assert select([(0, 2, 5), (1, 3, 10)]) == ([(1, 3, 10)], 10)
    assert select([(0, 2, 10), (1, 3, 5)]) == ([(0, 2, 10)], 10)
    assert (select(
        [(0, 2, 1), (1, 3, 4), (5, 6, 2), (4, 7, 3), (1, 4, 5), (2, 5, 6)])
        == ([(0, 2, 1), (2, 5, 6), (5, 6, 2)], 9))

def test_graph_search(search):
    assert search({0: []}, 0)[:2] == ({0: BLACK}, {0: None})
    assert (search({0: [1], 1: [0]}, 0)[:2] ==
            ({0: BLACK, 1: BLACK}, {0: None, 1: 0}))
    assert (search({0: [1], 1: [0]}, 1)[:2] ==
            ({0: BLACK, 1: BLACK}, {0: 1, 1: None}))
    assert (search({0: [1], 1: []}, 0)[:2] ==
            ({0: BLACK, 1: BLACK}, {0: None, 1: 0}))
    assert (search({0: [1], 1: []}, 1)[:2] ==
            ({0: WHITE, 1: BLACK}, {1: None}))
    assert (search({"A": ["B", "C"], "B": ["C"], "C": ["A"]}, "A")[:2] ==
            ({"A": BLACK, "B": BLACK, "C": BLACK},
             {"A": None, "B": "A", "C": "A"}))
    assert (search({"A": ["B", "C"], "B": ["C"], "C": ["A"]}, "B")[:2] ==
            ({"A": BLACK, "B": BLACK, "C": BLACK},
             {"B": None, "C": "B", "A": "C"}))
    assert (search({"A": ["B", "C"], "B": ["C"], "C": ["A"]}, "C")[:2] ==
            ({"A": BLACK, "B": BLACK, "C": BLACK},
             {"C": None, "A": "C", "B": "A"}))

def test_graph_search_bfs(search):
    assert (search(
        {1: [2, 3], 2: [1, 4], 3: [1, 5], 4: [2, 6], 5: [3, 6], 6: [4, 5]}, 1)
        == ({v: BLACK for v in range(1, 7)},
            {1: None, 2: 1, 3: 1, 4: 2, 5: 3, 6: 4},
            {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3}))
    assert (search(
        {1: [2, 3], 2: [1, 4], 3: [1, 5], 4: [2, 6], 5: [3, 6], 6: [4, 5]}, 6)
        == ({v: BLACK for v in range(1, 7)},
            {6: None, 4: 6, 5: 6, 2: 4, 3: 5, 1: 2},
            {6: 0, 4: 1, 5: 1, 2: 2, 3: 2, 1: 3}))
    assert (search(
        {1: [2, 3], 2: [4], 3: [5], 4: [6], 5: [6], 6: []}, 1)
        == ({v: BLACK for v in range(1, 7)},
            {1: None, 2: 1, 3: 1, 4: 2, 5: 3, 6: 4},
            {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3}))
    assert (search(
        {1: [2, 3], 2: [4], 3: [5], 4: [6], 5: [6], 6: []}, 6)
        == ({v: BLACK if v == 6 else WHITE for v in range(1, 7)},
            {6: None},
            {6: 0}))

def test_graph_search_dfs(search):
    assert (search(
        {1: [2, 3], 2: [1, 4], 3: [1, 5], 4: [2, 6], 5: [3, 6], 6: [4, 5]}, 1)
        == ({v: BLACK for v in range(1, 7)},
            {1: None, 3: 1, 5: 3, 6: 5, 4: 6, 2: 4},
            {2: 0, 4: 1, 6: 2, 5: 3, 3: 4, 1: 5}))
    assert (search(
        {1: [2, 3], 2: [1, 4], 3: [1, 5], 4: [2, 6], 5: [3, 6], 6: [4, 5]}, 6)
        == ({v: BLACK for v in range(1, 7)},
            {6: None, 5: 6, 3: 5, 1: 3, 2: 1, 4: 2},
            {4: 0, 2: 1, 1: 2, 3: 3, 5: 4, 6: 5}))
    assert (search(
        {1: [2, 3], 2: [4], 3: [5], 4: [6], 5: [6], 6: []}, 1)
        == ({v: BLACK for v in range(1, 7)},
            {1: None, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5},
            {6: 0, 5: 1, 3: 2, 4: 3, 2: 4, 1: 5}))
    assert (search(
        {1: [2, 3], 2: [4], 3: [5], 4: [6], 5: [6], 6: []}, 6)
        == ({v: BLACK if v == 6 else WHITE for v in range(1, 7)},
            {6: None},
            {6: 0}))

def test_bipartition(bipart):
    assert bipart({}) == {}
    assert bipart({0: []}) == {0: 0}
    assert bipart({0: [], 1: []}) == {0: 0, 1: 0}
    assert bipart({0: [1], 1: [0]}) == {0: 0, 1: 1}
    assert bipart({0: [1], 1: [0, 2], 2: [1]}) == {0: 0, 1: 1, 2: 0}
    assert not bipart({0: [1, 2], 1: [0, 2], 2: [1, 0]})
    assert bipart({0: [], 1: [2], 2: [1]}) == {0: 0, 1: 0, 2: 1}
    assert (bipart({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
            == {0: 0, 1: 1, 2: 0, 3: 1})
    assert not bipart({0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]})

def test_undirected_has_cycle(has_cycle):
    assert not has_cycle({})
    assert not has_cycle({0: []})
    assert not has_cycle({0: [], 1: []})
    assert not has_cycle({0: [1], 1: [0]})
    assert has_cycle({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    assert has_cycle({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]})
    assert not has_cycle({0: [1], 1: [0, 2], 2: [1, 3], 3: [2]})

def test_topological_sort(sort):
    assert sort({}) == []
    assert sort({0: []}) == [0]
    assert sort({0: [], 1: []}) == [0, 1]
    assert sort({0: [1], 1: []}) == [0, 1]
    assert not sort({0: [1], 1: [0]})
    assert sort({0: [1], 1: [2], 2: [3], 3: []}) == [0, 1, 2, 3]
    assert (sort({0: [1], 1: [2, 3], 2: [4], 3: [5], 4: [], 5: []})
            in [[0, 1, 2, 4, 3, 5], [0, 1, 2, 3, 4, 5]])
    assert not sort({0: [1], 1: [2, 3], 2: [4], 3: [5], 4: [], 5: [0]})

def test_reverse_graph(reverse):
    assert reverse({}) == {}
    assert reverse({0: [], 1: []}) == {0: [], 1: []}
    assert reverse({0: [1], 1: []}) == {0: [], 1: [0]}
    assert reverse({0: [1], 1: [0]}) == {0: [1], 1: [0]}

def test_find_sccs(find):
    assert find({}) == []
    assert find({0: []}) == [[0]]
    assert find({0: [], 1: []}) == [[1], [0]]
    assert find({0: [1], 1: []}) == [[0], [1]]
    assert find({0: [], 1: [0]}) == [[1], [0]]
    assert find({0: [1], 1: [0]}) == [[0, 1]]
    assert find({0: [1, 2], 1: [0, 2], 2: [0, 1]}) == [[0, 1, 2]]

def test_minimum_spanning_tree(mst):
    assert mst({0: [1], 1: [0]}, {(0, 1): 5}, 0) == {0: None, 1: 0}
    assert (mst({0: [1, 2], 1: [0, 2], 2: [0, 1]},
                {(0, 1): 5, (1, 2): 10, (0, 2): 15},
                0)
            == {0: None, 1: 0, 2: 1})
    assert (mst({0: [1, 2], 1: [0, 2], 2: [0, 1]},
                {(0, 1): 15, (1, 2): 5, (0, 2): 10},
                0)
            == {0: None, 2: 0, 1: 2})

def test_single_source_shortest_path(sssp, weighted, cyclic):
    assert sssp({0: []}, 0) == {0: 0}
    assert sssp({0: [], 1: []}, 0) == {0: 0}
    assert sssp({0: [1], 1: []}, 0) == {0: 0, 1: 1}

    if cyclic:
        assert sssp({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0) == {0: 0, 1: 1, 2: 1}

    if weighted:
        assert (sssp({0: [1, 2], 1: [2], 2: []},
                    0,
                    {(0, 1): 1, (0, 2): 10, (1, 2): 2})
                == {0: 0, 1: 1, 2: 3})
        assert (sssp({0: [1], 1: [2, 3, 4], 2: [3, 4], 3: [], 4: []},
                     0,
                     {(0, 1): 1, (1, 2): 6, (1, 3): 4, (1, 4): 1, (2, 3): 1,
                      (2, 4): 2})
                == {0: 0, 1: 1, 2: 7, 3: 5, 4: 2})

    if weighted and cyclic:
        assert (sssp({0: [1], 1: [2, 3, 4], 2: [0, 3, 4], 3: [], 4: []},
                     0,
                     {(0, 1): 1, (1, 2): 6, (1, 3): 4, (1, 4): 1, (2, 3): 1,
                      (2, 4): 2, (2, 0): 3})
                == {0: 0, 1: 1, 2: 7, 3: 5, 4: 2})

def test_all_pairs_shortest_path(apsp):
    I = float('inf')
    assert (apsp([[0, 1, 2, 4],
                 [I, 0, I, -1],
                 [I, I, 0, 3],
                 [I, I, I, 0]])
            == [[0, 1, 2, 0],
                [I, 0, I, -1],
                [I, I, 0, 3],
                [I, I, I, 0]])
    assert (apsp([[0, 1, 4, 3],
                  [I, 0, 2, I],
                  [-1, I, 0, I],
                  [I, -2, 1, 0]])
            == [[0, 1, 3, 3],
                [1, 0, 2, 4],
                [-1, 0, 0, 2],
                [-1, -2, 0, 0]])

def test_complement_graph(complement):
    assert complement({}) == {}
    assert complement({0: []}) == {0: []}
    assert complement({0: [], 1: []}) == {0: [1], 1: [0]}
    assert complement({0: [1, 2], 1: [0], 2: [0]}) == {0: [], 1: [2], 2: [1]}

def test_all():
    test_sort(select_sort)
    test_sort(merge_sort)
    test_search(linear_search)
    test_search(dc_search)
    test_select(naive_select)
    test_select(mom_select)
    test_2d_maxima(naive_2d_maxima)
    test_2d_maxima(dc_2d_maxima)
    test_closest_pair(naive_closest_pair)
    test_closest_pair(dc_closest_pair)

    test_activity_selection(activity_selection)
    test_job_scheduling(job_scheduling)
    test_weighted_job_scheduling(weighted_job_scheduling)
    test_stable_marriage(stable_marriage)

    test_lin_ind_set(lin_ind_set)
    test_seq_alignment(seq_alignment)
    test_optimal_parens(optimal_parens)
    test_value_activity_selection(value_activity_selection)

    test_graph_search(breadth_first_search)
    test_graph_search(depth_first_search)
    test_graph_search(depth_first_search_rec)
    test_graph_search_bfs(breadth_first_search)
    test_graph_search_dfs(depth_first_search)
    test_graph_search_dfs(depth_first_search_rec)
    test_bipartition(bipartition)
    test_undirected_has_cycle(undirected_has_cycle)
    test_topological_sort(topological_sort)
    test_topological_sort(topological_sort_alt)
    test_reverse_graph(reverse_graph)
    test_find_sccs(kosaraju)
    test_minimum_spanning_tree(kruskal)
    test_minimum_spanning_tree(prim)
    test_single_source_shortest_path(bfs_sssp, weighted=False, cyclic=True)
    test_single_source_shortest_path(dijkstra, weighted=True, cyclic=True)
    test_single_source_shortest_path(dag_sssp, weighted=True, cyclic=False)
    test_all_pairs_shortest_path(floyd_warshall)
    test_complement_graph(complement_graph)

###
### Main
###

if __name__ == "__main__":
    test_all()