"""
Created on Sat Jul  3 22:10:47 2021
"""

string = input("Enter string: ")
length = len(string)

def minimalDistance(string, length):

    minimalDistance = len(string)

    for i in range(length):
        
        for j in range(i+1, length):
            
            if(string[i] == string[j] and (j-i) < minimalDistance):
                
                minimalDistance = j-i
                break
            
    if(minimalDistance == len(string)):
        
        return -1
    
    else:
        
        return minimalDistance - 1

print("Shortest distance: ", minimalDistance(string, length))
