def solution(tickets):
    routes = {}

    for s, e in tickets:
        routes[s] = routes.get(s, []) + [e]

    for r in routes:
        routes[r].sort(reverse=True)

    start = ['ICN']
    path = []

    while start:
        top = start[-1]
        if not top in routes or not routes[top]:
            path.append(start.pop())
        else:
            start.append(routes[top].pop())

    return path[::-1]