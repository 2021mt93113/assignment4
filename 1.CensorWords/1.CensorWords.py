def censor_string(string, lst, char):
 modified_string=string.split()
 returned_words = [word if word not in lst else char*len(word) for word in modified_string]
 print (' '.join(returned_words))


censor_string("Today is a Wednesday!", ["Today", "a"], "-")
censor_string("The cow jumped over the moon.", ["cow", "over"], "*")
censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*")
