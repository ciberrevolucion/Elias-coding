#!/usr/bin/python
# Elias Coding function library

# Function to asign probabilities to each symbol
def setProbabilities(toencode,mode):
	while(1):
		if mode == 'auto':
			prob=computeRealProbabilities(toencode)
			# print "Probabilities: " + str(prob)
			break
		elif mode == 'custom':
			prob=computeCustomProbabilities(toencode)
			# print "Probabilities: " + str(prob)
			break
		else:
			mode == input("Choose the mode: 'real' for Real probabilities or 'custom' For custom probabilities: ")
	return prob


# Function used to compute the probabilities of each symbol of a string
def computeRealProbabilities(notencoded):
	
	splitted = list(notencoded)
	# dictionary=[]
	probabilities ={}
	counter=0
	for symbol in splitted:
		# Adding the number of instances for each symbol to the dictionary
		
		if not(symbol in probabilities):
			probabilities[symbol]=1
			# print symbol + " added to the dictionary"
		else:
			probabilities[symbol]=probabilities[symbol]+1
			# print symbol + " updated"
		counter=counter+1
		# print "Counter: " + str(counter)
		
	for key in probabilities:
		probabilities[key] = float(probabilities[key])/counter
	return probabilities

# Function that lets the user add custom probability to each symbol
def computeCustomProbabilities(notencoded):
	splitted = list(notencoded)
	# dictionary=[]
	probabilities ={}
	counter=0
	value=0
	for symbol in splitted:
		# Adding the number of instances for each symbol to the dictionary
		if not(symbol in probabilities):
			probabilities[symbol]= 0 
	for key in probabilities:
		print "Status of the probabilities: " + str(probabilities)
		value= float(raw_input("Probability of " + key + ": "))
		counter=counter+value
		print "Left probability to assign: " + str(1-counter)
		if (1-counter) == 0:
			print "You have assigned all the probability, the rest will be set to 0"
			probabilities[key] = value
			break
		elif (1-counter) < 0:
			print "Invalid probability assigned for the last symbol, quitting"
			exit(1)
		if value > 1:
			print "Invalid probability assigned to the last symbol, quitting"
			exit(1)
		probabilities[key] = value
	return probabilities

# Elias Encoder
def eliasEncoder(prob, run, toencode):
	c=[0] # principio del intervalo
	a=[1] # rango del intervalo
	for i in range(run):
		symbol=toencode[i]
		print "Current interval: " + str([c[i],c[i]+a[i]])
		print "Encoding " + symbol
		a.append(a[i]*prob[symbol])
		c.append(c[i]+a[i]*F(prob,symbol))
		
	code = (a[run]+2*c[run])/2
	print "Current interval: " + str([c[run],c[run]+a[run]])
	print "Code: " + str(code)
	return code
		
# Cumulative probability
def F(prob, symbol):
	accumulated=0
	for key, value in prob.iteritems():
		if key != symbol:
			accumulated=accumulated + value
			continue
		else:
			break
#	print "Accumulated: " + str(accumulated)
	return accumulated
	
# Elias Decoder
def eliasDecoder(prob,run,code):
	low=0
	high=1
	distance=high-low
	subintervals={}
	message=""
	subintervals=computeSubintervals(prob,low,distance)
	for i in range(run):
		value=(code-low)/distance
#		print "Value: " + str(value)
		symbol=findSubinterval(subintervals,value)
		print "Current interval: " + str([low,high])
		print "Symbol: " + symbol
		subinterval=subintervals[symbol]
		message=message+symbol
		high=low+distance*subinterval[1]
		low=low+distance*subinterval[0]
		distance=high-low
#		print "Distance: " + str(distance)
	return message

# Finds the subinterval where the passed code is
def findSubinterval(subs,code):
	for key, value in subs.iteritems():
		if (code > value[0]) & (code < value[1]):
			return key

# Computes the subintervals given some parameters
def computeSubintervals(probs,low,distance):
	sub={}
	previous=[low] # explicit copy
	for key, value in probs.iteritems():
#		print "Key: " + str(key) + ". Value: " + str(value)
		sub[key]=[previous[0], previous[0]+distance*value]
#		print "new subinterval: " + str(sub[key])
		previous[0]=previous[0]+distance*value
#		print "Previous: " + str(previous)
#	print "Subintervals: " + str(sub)
	return sub
		
		
