"""
    Rules goal
    • Any live cell with two or three live neighbours lives on to the next generation.
    • Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    • All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    
    Rules to add
    • Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    • Any live cell with more than three live neighbours dies, as if by overpopulation.
    
    Last Rules to add
    These rules, which compare the behavior of the automaton to real life, can be condensed into the following:
    • Any live cell with two or three neighbors survives.
    • Any dead cell with three live neighbors becomes a live cell.
"""

