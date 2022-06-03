import numpy as np


# Reward matrix
R = np.matrix([[-1,-1,-1,-1,0,-1],
               [-1,-1,-1,0,-1,100],
               [-1,-1,-1,0,-1,-1],
               [-1,0,0,-1,0,-1],
               [-1,0,0,-1,-1,100],
               [-1,0,-1,-1,0,100]])


# Q-matrix

Q = np.matrix(np.zeros([6,6]))

# Gama parameter
gamma = 0.8

# Initial state (usually chosen at random)

initial_state  = 1


# Get all the available actions in a particular state

def available_action(state):
    current_state_row = R[state,]
    av_act  = np.where(current_state_row>=0)[1]
    return av_act

available_act = available_action(initial_state)

# function return random actions among all the available actions within the range

def sample_next_action(available_action_range):
    next_action = int(np.random.choice(available_action_range,1))
    return next_action


#sample next action to be performed

action = sample_next_action(available_act)



## Function updates the Q matrix according to the path selected and the Q

def update(current_state, action, gamma):
    max_index = np.where(Q[action,] == np.max(Q[action,]))[1]
    if max_index.shape[0]>1:
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    max_value = Q[action,max_index]
    
    #Q learning
    Q[current_state,action] = R[current_state, action]+gamma*max_value


update(initial_state, action, gamma)



## Training ---------------------------------------------------------------------------------


## Train over 10 000 iterations  (re iterate the process above)
for i in range(0,10000):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_action(current_state)
    action = sample_next_action(available_act)
    update(current_state, action, gamma)
    
print("Trained Q-matrix:")
print(Q/np.max(Q)*100)



# Testing -----------------------------------------------------------------------------------

# Any number [0-5] can be given to test the traversal to the goal (goal would be 5)
current_state = 5
steps = [current_state]


while current_state! = 5:
    next_step_index = np.where(Q[current_state,] == np.max(Q[current_state, ]))[1]
    if next_step_index.shape[0]>1:
        next_step_index = int(np.random.choice(next_step_index, size=1))
    else:
        next_step_index = int(next_step_index)
    steps.append(next_step_index)
    current_state = next_step_index
print(steps)
        
    


