import numpy as np
import math

total_no = 49**8
print("Total number of parameter possibilities: ", total_no)

total_0 = 1
total_8 = 48**8
total_no_possible = total_no - total_0 - total_8
print("There is 1 parameter choice of all -1's ")
print("There is " + str(total_8) +  " parameter choices resulting in full cubes")
print("So there is " + str(total_no_possible) +  " non-trivial choices ")


total_no_possible_symetric = total_no_possible / 48
print(" Dividing by 48, there are less than or equal to " + str(total_no_possible_symetric) + " possible topologies ")

print(" In each subset we have: ")
sum = 0
for i in range(1,8):
    print("\t Subset "+ str(i))
    print(" \t\t There are 8 choose " + str(i) + ", \n\t\t or " + str(math.comb(8,i))+ " possible subcube choices")
    print(" \t\t There are 48 possibilities for each one,")
    print(" \t\t so there are (8 choose " + str(i) + ")*48^" + str(i) + " choices")
    num = math.comb(8,i) * (48**i)
    print(" \t\t This is " + str(num))
    print(" \t\t Divide by 48, this is " + str(num/8))
    sum += (num/48)
    percent = float(num) / float(48.0*total_no_possible_symetric)
    print(" \t\t this is " + str(percent*100.0) + " percent of the total " )

print("Summed up, this is " + str(sum) + " fractals, as expected")
