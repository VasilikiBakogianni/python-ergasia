import random
# We fill our list with random numbers from -30 to 30(we want thirty numbers)
lst = random.sample(xrange(-30,30), 30)                      

def triads(lst, x):
# Search for possible triads
    found = True

    for i in range(0, x-2):
     
        for j in range(i+1, x-1):
         
            for z in range(j+1, x):
             
                if (lst[i] + lst[j] + lst[z] == 0):
                    print(lst[i], lst[j], lst[z])
                    found = True
     

    if (found == False):
        print("It is impossible to form a triad.")


print ("The randomly created list : ")
print lst
print ("\n")

x = len(lst)
print ("The triads whose sum is 0 are the following: ")
triads(lst, x)