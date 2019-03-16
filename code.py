def wordcount(filename,listwords):
	with open(filename) as file_object:
		file_text=file_object.read()
		return {word:file_text.count(word) for word in listwords}
for word,count in wordcount('q1.txt',['modularity','speed','flexibility','extensibility','portability']).items():
	print("Count of {}:{}".format(word,count))
