# 8-puzzle-solver

Artificial intelligence algorithm that solves the 8 puzzle using A*
Writeup is provided detailing how to run the algorithm, outputs produced, and source code.

## Running the solver

1. Download 8_puzzle_solver.py
2. Place it in a directory with the formatted input text files containing the 8 puzzles that are being solved. It is set up to automatically run the following three puzzles. (This can be changed by altering the main function of the code)

    - Input1.txt
    - Input2.txt
    - Input3.txt

3. Open your shell in the directory with all files.

4. Run the following command in the shell using Python 3. (An example is shown below.) Alternatively run the Python file through your preferred IDE.

    `python3 8_puzzle_solver.py`

5. Files containing the solutions will be generated as follows. Where `#` will be the number of the input passed to the program. The `h1` shows that the *sum of Manhattan distances of the tiles from their goal positions* was used as the heuristic and `h2` shows that *Nilsson's sequence score* was used as the heuristic.
    - Output`#`h1.txt
    - Output`#`h2.txt

