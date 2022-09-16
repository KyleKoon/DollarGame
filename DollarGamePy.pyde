'''
TITLE: Dollar Game
AUTHOR: Kyle Koon
DATE DUE: 1/21/21
COURSE TITLE: Game Design
MEETING TIME(S): Mon. and Wed. at 2pm
DESCRIPTION: This program creates the Dollar Game. In this game, the user left clicks or right clicks
on a node. A left click will send 1 dollar to each of the connected nodes. A right click will receive 1
dollar from each of the connected nodes. The objective of the game is to get each node to have 0 or more dollars.
The starting node values are defined by a text file of the format:
    6,1,1,1
    1,-3,1,1
    1,1,0,0
    1,1,0,-2
Each row defines a new node. The diagonal elements are the node values. A 1 denotes which nodes the current node is
connected to.
'''

Nodes = [] #stores the nodes for the game
import math

def setup():
    print("left click on a node to lend money to connected nodes \nright click on a node to borrow money from connected nodes")
    file = open("board1.txt", "r") #opens the board data file for reading
    numNodes = len(file.readline().strip().split(",")) #figures out how many column values (# of nodes) are in the first row
    for i in range(numNodes): #creates blank node objects of the Node class
        node = Node(0)
        Nodes.append(node)

    file.seek(0) #returns to the first line of the file
    rowNum = 0
    for row in file:
        row = row.split(",")
        i = 0
        connectionAdrs = [] #will store references to the other node objects that the current node is connected to
        while i < len(row): 
            if rowNum == i: #when the row index matches the column index, we've found a diagonal element. This is the node value
                Nodes[rowNum].val = int(row[i]) #sets the node value of the current node
            elif int(row[i]) == 1: #if there is a 1 in one of the non-diagonal entries
                connectionAdrs.append(i) #the column index is added to a list corresponding to the current node
            else: #any non-diagonal entries and any values other than 1
                pass #nothing occurs
            i+=1 #a new column in the same row is examined
    
        for i in range(len(connectionAdrs)):
            currentNode = Nodes[rowNum] #this is the current node where the connections originate from
            currentNode.addConnection(Nodes[connectionAdrs[i]]) #the node at the current connection address is connected to our original node
        rowNum += 1 #a new row is examined
        
    size(1000, 800) #a 1000x800 window is created

def draw():

    background(200) #the background color is set
    
    #evenly spaced coordinates based on window size
    x1 = width/2-100
    x2 = width/2 + 100
    y1 = height/2 - 100
    y2 = height/2 + 100
    
    radius = 80  #radius of the circles we will create
    
    #sets the x and y coordinate values for each of the four nodes
    Nodes[0].x = x1
    Nodes[0].y = y1

    Nodes[1].x = x2
    Nodes[1].y = y1
    
    Nodes[2].x = x1
    Nodes[2].y = y2
    
    Nodes[3].x = x2
    Nodes[3].y = y2
    
    for node in Nodes:
        i = 0
        while i < len(node.connected):
            line(node.x,node.y,node.connected[i].x,node.connected[i].y) #a line is drawn from the current node to a connected node
            i+=1 #will move to new connection if one exists
    
    for node in Nodes:
        fill(255)
        circle(node.x,node.y,radius) #the circles are created based on each nodes x and y coordinates
        textSize(30)
        textAlign(CENTER)
        fill(0) #the text color is set to black
        text(node.val,node.x,node.y) #the text is created at the current nodes x and y coordinates




class Node:
    def __init__(self, value):
        self.val = value #will store the dollar amount of the node
        self.connected = [] #will store references to the other nodes that this node is connected to
        self.x = 0 #will store the x coordinate of the node on the screen
        self.y = 0 #will store the y coordinate of the node on the screen
    
    def borrow(self): #the current node will receive one dollar from each of the nodes connected to it
        for node in self.connected:
            self.val += 1 #the current node's value increases
            node.val -= 1 #the connected node's value decrease

    def lend(self): #the current node will give out one dollar to each of the nodes connected to it
        for node in self.connected:
            self.val -= 1 #the current node's value decreases
            node.val += 1 #the connected node's value increases

    def addConnection(self, node):
        self.connected.append(node) #the node object is added to the connected list of the current node



def checkForWin(): #checks if all nodes contain 0 or more dollars
    for node in Nodes:
        if node.val/-1 > node.val: #if the node value is negative, the player has not won yet
            return False
    return True


def mousePressed(): #will either lend money (left click) to connected nodes or borrow money (right click) from connected nodes
    i = 0
    while i < len(Nodes):
        if mouseX < Nodes[i].x + 40 and mouseX > Nodes[i].x - 40: #if the x coordinate of the clicked mouse position is within the node circle
            if mouseY < Nodes[i].y + 40 and mouseY > Nodes[i].y - 40: #ifi the y coordinate of the clicked mouse position is within the node circle
                if mouseButton== LEFT: #if the left mouse button is clicked
                    Nodes[i].lend() #the current node lends money to connected nodes
                elif mouseButton == RIGHT: #if the right mouse button is clicked
                    Nodes[i].borrow() #the current node borrows moeny from connected nodes
        i+=1 #checks same conditions for the other three nodes
  
    if checkForWin(): #if all nodes contain 0 or more dollars
        print("Congrats! You won!")
        print("Please close the window and re-run the program to play again") 
