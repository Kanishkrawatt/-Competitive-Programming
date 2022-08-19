# Solution 
# Bob is Instructed _ To paint a row of cubes 
# Initially There are no cubes 
# There are two Types
# Type1 Put an unpainted cube in the end of the row and paint it to colour C
# Type2 Paint all blocks which were painted with colour c1 to colour c2
# First Line is Number of Queries
# 1 X  -> Place a cube in the end and paint it X
# 2 X Y -> Paint all block which were painted with colour X to Colour Y

# 1 2 1 2 1 
# 2 9 9 9 8 1 10


from sys import stdin,stdout
Blocks = []
number_of_Queiries = int(stdin.readline())

for _ in range(number_of_Queiries):
    Color = list(map(int, stdin.readline().split()))
    if(Color[0]==2):
        if(len(Blocks)==0):
            continue
        while(Color[1] in Blocks):
            Index =Blocks.index(Color[1])
            Blocks[Index] = Color[2]            
    else:
         Blocks.append(Color[1])
        
ans =' '.join([str(elem) for elem in Blocks])
stdout.write(ans)