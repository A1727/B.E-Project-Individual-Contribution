def wordcount(filename,listwords):
	with open(filename) as file_object:
		file_text=file_object.read()
		return {word:file_text.count(word) for word in listwords}
best=0
for word,count in wordcount('q1.txt',["modularity","speed","flexibility","extensibility","portability"]).items():
	if(count>=1):
		count=1
		best+=1
	else:
		count=0;
	print("Count of {}:{}".format(word,count))
print(best)
prob=float(best/5)
print(prob)
