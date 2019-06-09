# Classic SAT solver in Python

This project is a iterative implementation of a backtracking, watchlist-based, SAT solver.

## Usage

    usage: run.py [-h] [-v] [-a] [-b] [--output_filter OUTPUT_FILTER]
                  [-i INPUT]

    Solve SAT instance by reading from stdin using an iterative or recursive
    watchlist-based backtracking algorithm. Recursive algorithm is used by
    default, unless the --iterative flag is given. Empty lines and lines that
    starting with a # will be ignored.

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         verbose output.
      -a, --all             output all possible solutions.
      -b, --brief           brief output for assignemnts: outputs variables
                            assigned 1.
      --output_filter OUTPUT_FILTER
                            only output variables with name-string with given
                            string.
      --iterative           use the iterative solver.
      -i INPUT, --input INPUT
                            read from given file instead of stdin.

## Example Usage

    $ python run.py -v -i examples/03.in.txt
    
    Trying A = 0
    Trying C = 0
    Current watchlist:
    A:
    ~A:
    C: C, A C
    ~C:
    B: C B
    ~B: ~B
    Current assignment: ~A ~C
    Clause C contradicted.
    Trying C = 1
    Trying B = 0
    Found satisfying assignment #1:
    ~A C ~B

## Reference
\[1\] [Understanding SAT by Implementing a Simple SAT Solver in Python](https://sahandsaba.com/understanding-sat-by-implementing-a-simple-sat-solver-in-python.html5)
