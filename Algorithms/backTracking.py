import random

class regions:
    def __init__(self, name):
        self.name = name
        self.color = None

    def __repr__(self):
        return f"{self.name}:{self.color}"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, regions) and self.name == other.name

def backTrackingSearch(rslt, constraints, clrs):
    return recursiveBackTracking(rslt, constraints, clrs)

def recursiveBackTracking(result, constraints, colors):
    if len(result) == len(constraints):
        return result
    unassigned = [r for r in constraints if r.color is None]
    if not unassigned:
        return result
    var = random.choice(unassigned)
    for color in colors:
        conflict = False
        for neighbor in constraints[var]:
            if neighbor.color == color:
                conflict = True
                break
        if not conflict:
            var.color = color
            result.append(var)
            res = recursiveBackTracking(result, constraints, colors)
            if res:
                return res
            result.pop()
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

    constraints = {wa : [nr, sa],
                   nr : [wa, sa, ea],
                   sa : [wa, nr, ea, nsw, vic],
                   ea : [nr, sa, nsw],
                   nsw : [sa, ea, vic],
                   vic : [nsw, sa],
                   ta : []}
    colors = ["Red", "Blue", "Green"]
    result = []
    print(backTrackingSearch(result, constraints, colors))