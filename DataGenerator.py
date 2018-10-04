import random, decimal, sched, time, os
#import sched, time

s = sched.scheduler(time.time, time.sleep)

def generate_data(sc):
	print ("Append data")
	f = open('myfile.txt', 'a')
	f.write(str(random.random() * 5 - 2) + os.linesep)
	f.close() 
	s.enter(0.5, 1, generate_data, (sc,))
s.enter(0.5, 1, generate_data, (s,))
s.run()