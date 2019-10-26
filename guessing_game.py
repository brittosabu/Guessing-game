import gym
import numpy as np

env  = gym.make("GuessingGame-v0")
env.reset()

lower_limit = -1000
upper_limit  = 1000

for i in range(1,201):
	print("Step",i)
	value =  ((lower_limit+upper_limit)/2)
	obs,rew,done,info = env.step(np.array([value]))

	if obs ==1:
		print(value, "lower than target")
		lower_limit=value
	if obs ==3:
		print(value, "higher than target")
		upper_limit =value
	if obs ==2:
		print( "Target acquired",value)
		break

env.close()

