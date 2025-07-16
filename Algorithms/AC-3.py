from collections import deque

class regions:
    def __init__(self, name):
        self.name = name
        self.color = None
        self.domain = []

    def __repr__(self):
        return f"{self.name}:{self.color}"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, regions) and self.name == other.name

def AC3(constraints, colors):
    for region in constraints:
        region.domain = list(colors)

    queue = deque()
    for Xi in constraints:
        for Xj in constraints[Xi]:
            queue.append((Xi, Xj))

    while queue:
        Xi, Xj = queue.popleft()
        if removeInconsistentArcs(Xi, Xj):
            if not Xi.domain:
                return False
            for Xk in constraints[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))
    return True

def removeInconsistentArcs(X, Y):
    revise = False
    to_remove = []
    for x_color in list(X.domain):  # iterate over a copy
        if not any(x_color != y_color for y_color in Y.domain):
            to_remove.append(x_color)
    for color in to_remove:
        X.domain.remove(color)
        revise = True
    return revise

def backtrack(assignment, constraints, regions_list):
    if len(assignment) == len(regions_list):
        return assignment

    # Select unassigned region with the smallest domain (MRV heuristic)
    unassigned = [r for r in regions_list if r not in assignment]
    var = min(unassigned, key=lambda r: len(r.domain))

    for color in var.domain:
        if all(neighbor.color != color for neighbor in constraints[var] if neighbor.color is not None):
            var.color = color
            assignment.append(var)
            result = backtrack(assignment, constraints, regions_list)
            if result:
                return result
            assignment.pop()
            var.color = None
    return None

if __name__ == "__main__":
    wa = regions("WA")
    nr = regions("NR")
    sa = regions("SA")
    ea = regions("EA")
    nsw = regions("NSW")
    vic = regions("VIC")
    ta = regions("TA")

    regions_list = [wa, nr, sa, ea, nsw, vic, ta]
    constraints = {wa : [nr, sa],
                   nr : [wa, sa, ea],
                   sa : [wa, nr, ea, nsw, vic],
                   ea : [nr, sa, nsw],
                   nsw : [sa, ea, vic],
                   vic : [nsw, sa],
                   ta : []}
    colors = ["Red", "Blue", "Green"]

    # Run AC-3 to prune domains
    if AC3(constraints, colors):
        # Use backtracking to assign colors
        assignment = []
        solution = backtrack(assignment, constraints, regions_list)
        print(solution)
    else:
        print("No solution")