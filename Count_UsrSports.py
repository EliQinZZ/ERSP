import gzip
import os

sports = {}
usrCount = 0

f = gzip.open('endomondoHR.json.gz', 'r')

for l in f:
	usrCount += 1
	
	dic = eval(l)
	sport = dic['sport']
	
	if sport in sports:
		sports[sport] += 1
	else:
		sports[sport] = 1

print(sports)
print(usrCount)
