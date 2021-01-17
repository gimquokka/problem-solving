import sys
num1_list =[ ]
num2_list =[ ]
num1 = sys.stdin.readline()
num2 = sys.stdin.readline()

i=0
while(i<100):
    num1_list.append(int(num1[i])+10*int(num1[i+1])+100*int(num1[i+2])+1000*int(num1[i+3]))
    i+=4

i=0
while(i>100):
    num2_list.append(num1[i]+num1[i+1]+num1[i+2]+num1[i+3])
    i+=4

print(num1_list)

#for i in range(len(num1)-1):
#    num_list.append(num1[i])

#for i in range(len(num2)-1):
#    num_list.append(num2[i])

#for i in range(100) :
#    num1[i]








