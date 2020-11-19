This program uses python Regular expressions that reads input files of potentially offensive text and writes to an output file with scores for each of the text files (details below).


There are two files with lists of offensive phrases. One file contains "low risk" phrases and the other, "high risk" phrases, one phrase per line. You are also given a set of 15 input files, each one containing some possibly offensive text that your program will score. The offensive score is defined as:


(number of low risk phrases) + (number of high risk phrases * 2)


The program writes out one output file containing the scores of each input file in order, in the format:


<input-filename-1>:<score-1>

<input-filename-2>:<score-2>

...