# Project Euler [![Build Status](https://travis-ci.org/movery/Project-Euler.svg?branch=master)](https://travis-ci.org/movery/Project-Euler)

<a href="https://projecteuler.net/archives">
<img src="https://projecteuler.net/profile/movery.png"
 title="Project Euler ID" align="right" />
</a>

Solutions written in [Python](http://python.org) using version 2.7.

## INSTALLATION

Simply navigate to the 'Project-Euler' directory and enter
```
sudo python setup.py install
;;;

## USAGE

 Enter 'pe' followed by the problems you would like the solutions to (delimited
 by whitespace).

```
 $ pe 10 20 90
-----------------------------------------
 Attempting to solve Problem 10
 142913828922 found in 8.132522 seconds
-----------------------------------------
 Attempting to solve Problem 20
 648 found in 0.103 seconds
-----------------------------------------
 Attempting to solve Problem 90
 Problem 90 has not been solved yet
-----------------------------------------
```

## SOURCE CODE

/src/main.py contains the script which takes the user's number input and
attempts solve the corresponding problem.

/src/problems.py contains the solutions to each of the Project Euler problems.

/src/tools.py contains commonly used functions for use in problems.py

/resources/* contains text data to be used in /src/problems.py
