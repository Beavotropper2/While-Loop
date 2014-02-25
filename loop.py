
# Main
numCakeSlices = 8
cakeInFridge = True

while cakeInFridge:
    # Print number of slices in fridge
    print(str(numCakeSlices) + " slices left - taking a slice")
    
    # Take slice of cake
    numCakeSlices -= 1
    
    # Exit loop if no more slices in fridge
    if numCakeSlices == 0:
        print("All slices of cake are gone")
        cakeInFridge = False
        

