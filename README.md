CSC1034: Practical 2
====================
Description
-----------------
This purpose of this program is to analyse a taxonomy of proteins across different
species. It has the functionality to print out a list of the proteins in the taxonomy,
show the average length of the proteins and create a graph to show the average length of different
proteins.


How to use
-----------------
To use this program you will need to enter specific commands into the terminal.
You will need to provide it with the following pieces of information when wishing to use a feature of the program, these
include, depth (0 can be selected for this or 1 if you wish for the program to read more of the records from the file),
file-location (the file that you wish the program to run on) and finally you must state the feature of the program you
wish to use.
```
"pipenv run python uniplot.py --depth 0 --file-location `The file you wish to us' dump"
```
This will allow you to print out protein names and general data such as type and sequence to the terminal. 
```
"pipenv run python uniplot.py --depth 0 --file-location `The file you wish to us' list"
```
This will allow you to print out a formatted list of all the proteins.
```
"pipenv run python uniplot.py --depth 0 --file-location `The file you wish to us' average"
```
This will print out the average length of the proteins.
```
"pipenv run python uniplot.py --depth 0 --file-location `The file you wish to us' plot-average-by-taxa"
```
This will plot a bar graph showing the average protein length by taxonomy.
```
"pipenv run python uniplot.py --depth 0 --file-location `The file you wish to us' plot-average-by-taxa-pie"
```
This will plot a pie graph showing the average protein length by taxonomy.





