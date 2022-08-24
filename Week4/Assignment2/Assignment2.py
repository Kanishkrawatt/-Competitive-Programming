# A permutatio f of a set S is defined as bijection from S to itself. 
# That is , it is a function from S to S which every element occurs exactly once 
# as an image value for Example S = {1,2,3} 
# Example of Permutation on S is: f(1)=2,f(2)=1,f(3)=3
# Sn ={1,2,3,...,n} permutation F on Sn.
# Way 1 - one-line Notation = we describe the permutation as a sequence of length n,
# The i-th element of the sequence contains the value of f(i)
# Way 2 - Cyclic Notation, we describe the effect of repeatedly applying the permutaion on the element of the set
# It Expresses The permutation as a product of Cycles 
# select an arbitrary element x of Sn and write it down 
# Ex = {1,2,3,4,5}     1,5= arbitrary element
# Then Trace the orbit of X , that is , write down its values under successive apllications of f until the value 
# return to x , an once this happens , write down a closing parenthesis rather than x
# Now continue Until all elements y of Sn, Not yet written down, and preceed in the same way
# continue until all elements of Sn are written in Cycles



# Output Format
# T is The Number of Test Cases
# N = size of P list

def Linked(num,Array,previousPos):
    data =[]
    data.append(Array[previousPos])
    if(Array[previousPos]!=num):
        for i in Linked(num,Array,Array[previousPos]-1):
            data.append(i)
    
    return data
        



T = int(input())  
for _ in range(T):
    N = int(input())
    P = list(map(int,input().split()))
    data ={}
    i=0
    while(i<N):
        link = Linked(i+1,P,i)
        data[link[0]]=len(link)
        i += 1
        
    print(' '.join(map(str, data.values()))+" ")

        
    

