# CS461_Project2
Simulated Annealing Knapsack Problem

Starting from Main:

We have a starting temperature, and a few counters to control the loop & keep track of 
changes, attempts, & iterations.

formatInput() over in fileReader.py takes in the formatted text file & turns it into a 
list with the format:

	[[utility][weight][inclusion bool]
	 [utility][weight][inclusion bool]
	 ...
	]
	
Then, we use initialSolution() to pick a random 20 items from the list of 400 to 'pack'
into our vehicle. This function just picks 20 items to change the inclusion boolean to 1.

The while loop runs until there have been 40,000 consecutive attempts to accept a change
and there haven't been any accepted.

Within the while loop, we copy the initial solution & create a change 
(in proposedChange()). The change is then checked in checkChange() & if it was accepted
or not is stored in the changeBool. If an iteration completes (4000 changes or 40000 
attempts), then we update all our counters & the temperature.
If 40,000 change attempts occur without a single change, then we break out of the loop &
accept the current solution as the final solution. 
