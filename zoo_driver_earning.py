''' There is a zoo and there are several groups(number of groups:K) of people for tour. Each group is having different size (g1,g2,g3...gK). There is one bus with capacity C. Journey starts from a point and bus will come back to the same point. A group can only be included in the bus if all the members of the groups can be accumulated in bus. After coming back from the tour, each group in the bus will again wait in the queue at the bus-stand. Bus-driver earns a rupee for each person travelled. You have to find the earning of the bus driver after R rounds.'''

from collections import deque
def get_bus_driver_earning(no_of_gps, gp_size, bus_capacity, no_of_rounds):
    earnings = 0
    for i in range(no_of_rounds):
        current_capacity = 0
        for j in range(no_of_gps):	
            if current_capacity + gp_size[0] <= bus_capacity:
                gp = gp_size.popleft()
                gp_size.append(gp)
                earnings += gp
                current_capacity += gp
            else:
                break
    return earnings

def main():
    print "######### Case 1 #########"
    no_of_gps = 4
    gp_size = deque([2,4,3,5])
    bus_capacity = 7
    no_of_rounds = 4	
    print get_bus_driver_earning(no_of_gps, gp_size, bus_capacity, no_of_rounds)
    
    print "######### Case 2 #########"
    no_of_gps = 4
    gp_size = deque([2,4,3,5])
    bus_capacity = 200      # Much higher than all 4 gp size. But driver cannot take same group more than once at same time... :)
    no_of_rounds = 4	
    print get_bus_driver_earning(no_of_gps, gp_size, bus_capacity, no_of_rounds)

if __name__ == "__main__":	
    main()
