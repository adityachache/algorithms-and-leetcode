"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
                
        nodeMap = {None:None}
             
        curNode = head
        
        while curNode:
            
            newNode = Node(curNode.val)
            
            # this will be like {7(og): 7(copy), 13(og):13(copy)...}
            nodeMap[curNode] = newNode
            
            curNode = curNode.next
            
        curNode = head
        
        while curNode:
            
            copyNode = nodeMap[curNode]
            
            copyNode.next = nodeMap[curNode.next]
            copyNode.random = nodeMap[curNode.random]
            # if curNode.random == None we dont have it in hashtable that's why we add None:None in hashtable
            
            curNode = curNode.next
            
        
        return nodeMap[head]
            
            