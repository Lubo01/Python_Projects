# -*- coding: utf-8 -*-
"""	Project Bubblesort
	Algorithm example
	Documentation check
	Author:LL, Done: 03/2018"""
	
#souce data series as list
dataSeries = [2, 5, 7, 1, 6, 3, 8]	

def bubblesort(data):
	#loops through data
	for i in range (len(data)):
		for j in range (len(data)-i-1):
			#check neighbours, switch if left greater
			if data [j] > data [j+1]:
				data [j], data [j+1] = data [j+1], data [j]
				

def descending_bubble(data):
	#loops through data
	for i in range (len(data)):
		for j in range (len(data)-i-1):
			#check neighbours, switch if right greater
			if data [j] < data [j+1]:
				data [j], data [j+1] = data [j+1], data [j]

#test if function is working
bubblesort(dataSeries)

print "Sorted:\n%s" % dataSeries

descending_bubble(dataSeries)

print "Sorted Descending:\n%s" % dataSeries				
            
