# DollarGame
This program creates the Dollar Game. In this game, the user left clicks or right clicks
on a node. A left click will send 1 dollar to each of the connected nodes. A right click will receive 1
dollar from each of the connected nodes. The objective of the game is to get each node to have 0 or more dollars.
The starting node values are defined by a text file of the format:
    6,1,1,1
    1,-3,1,1
    1,1,0,0
    1,1,0,-2
Each row defines a new node. The diagonal elements are the node values. A 1 denotes which nodes the current node is connected to.
