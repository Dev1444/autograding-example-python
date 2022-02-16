# NAME:         Deven Mistry
# ASSIGNMENT:   Project 1

# Problem 1: squared_sum
def squared_sum(squared):
    squaredsum = 0
    for element in squared: # Reading list
        squaredsum += element ** 2 # Finding sum
    return squaredsum # Finds result

if __name__ == '__main__': 
    print(squared_sum([])) # Running test cases 
    print(squared_sum([5,-2,3]))
    print(squared_sum([-3,4]))
    print(squared_sum([7,-1,15,0]))

print('')

# Problem 2: mix
def mix(s1,s2): 
    case = ""
    for x in range(0,min(len(s1),len(s2))): # Calculating length 
        case = case + s1[x] + s2[x]
        
    if(len(s1)>len(s2)): 
        case = case + s1[x+1:]
    else:
        case = case + s2[x+1:]
    print(case)
    # Test cases
mix("hello", "there")    
mix("1234", "abcd")
mix("12", "abcd")
mix("1234", "ab")

