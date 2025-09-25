
# Your name: Hangming Hu
# Your student ID: 201912905
# You state that the code submitted is wholly written by yourself. 
# Date: 25/9/2025

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14

#use list to use index
state_order = ["red", "red_amber", "green", "amber"]
#current index
current = 0
#time in state
state_time = 1

for systime in range(1,maxtime+1):
    #state change
    if state_time >= states[state]:
        #index changes
        current = (current+1)%(len(state_order))
        #state change
        state = state_order[current]
        #reset the time
        state_time = 1
    
    #state does not change
    else:
        state_time += 1

    print(f"Time {systime:03} State {state}")