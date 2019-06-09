from __future__ import division
from __future__ import print_function

from sys import stderr

from watchlist import update_watchlist


def solve_iterative(instance, watchlist, assignment, d, verbose):
    """
    - The state list wil keep track of what values for which variables were tried
    - A value of 0 means nothing has been tried yet
    - A value of 1 means False has been tried but not True
    - A value of 2 means True has been tried but not False
    - A value of 3 means True and False have been tried.
    """

    n = len(instance.variables)
    state = [0] * n

    while True:
        if d == n:
            yield assignment
            d -= 1
            continue
        # Let's try assigning a value to v. Here would be the place to insert
        # heuristics of which value to try first.
        tried_something = False
        for a in [0, 1]:
            if (state[d] >> a) & 1 == 0:
                if verbose:
                    print('Trying {} = {}'.format(instance.variables[d], a),
                          file=stderr)
                tried_something = True
                # Set the bit indicating a has been tried for d
                state[d] |= 1 << a
                assignment[d] = a
                if not update_watchlist(instance, watchlist,
                                        d << 1 | a,
                                        assignment,
                                        verbose):
                    assignment[d] = None
                else:
                    d += 1
                    break

        if not tried_something:
            if d == 0:
                # Can't backtrack further. No solutions.
                return
            else:
                # Backtrack
                state[d] = 0
                assignment[d] = None
                d -= 1
