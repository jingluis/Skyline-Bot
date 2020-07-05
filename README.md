# Skyline Bot
![](skyline.png) 


This is a Telegram bot that parses commands allowing the user to manipulate, store and load skylines.

## Prerequisites

You will need to installed the required Python libraries using the following command

    pip3 install -r requirements.txt

You will also need a valid Telegram bot token written in **token.txt**.  

## Test Execution

To run the program that contains the telegram bot you must type the following command for the console from the **bot** folder:

    python3 bot.py

## Grammar

* The user can construct a skyline with a single building, by specifying the start x-coordinate, the height, and the end x-coordinate. An example would be `(1, 2, 3)`, where the building has height 2 and goes from the x-coordinates 1 to 3.
* The user can construct a skyline with multiple buildings by entering a list with multiple single buildings. An example would be `[(1, 2, 3), (4, 5, 6)]`.
* The user can construct a skyline with many randomly generated buildings by specifying some parameters `{n, h, w, xmin, xmax}`. An example would be `{100, 20, 4, 1, 1000}`. The meaning of the parameters is:
  * `n`: the amount of buildings
  * `h`: the maximum height of each building
  * `w`: the maximum width of each building
  * `xmin`: the minimum x-coordinate of each building
  * `xmax` the maximum x-coordinate of each building
* The union of two skylines is represented by `skyline1 + skyline2`.
* The intersection of two skylines is represented by `skyline1 * skyline2`.
* The reflection of a skyline is represented by the unary negation operator: `-skyline`.
* The right shift by `n` units of a skyline is represented by `skyline + n`.
* The left shift by `n` units of a skyline is represented by `skyline - n`.
* The replication `n` times of a skyline is represented by `skyline * n`.



## Skyline Implementation

All operations are implemented with a time complexity lower than O(N^2), being N the total number of the buildings involved in the operation. For the **union** operation, the time complexity is O(N lg N) using a variant of merge-sort. The rest of the operations are done with a time complexity O(N). 

The grammar does accept expressions of with/without spaces. Hence, to construct a skyline you can either write `(1,2,3)` or `(1, 2, 3)`.


### Parsing

The parsing of the expressions is implemented with the `antlr4` library for Python. 


### Persistent storage

Persistent storage is achieved with the `pickle` module in the Python standard library, which allows the saving and loading of arbitrary objects into binary files.



