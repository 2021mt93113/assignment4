from CensorWords import censor_string

if __name__ == '__main__':
    print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
    print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
    print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))
