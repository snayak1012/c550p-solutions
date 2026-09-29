def main():
    time=input("what time is it? ")
    times=convert(time)
    if 7.0<=times<=8.0:
        print("breakfast time")
    elif 12.0<=times<=13.0:
        print("lunch time")
    elif 18.0<=times<=19.0:
        print("dinner time")
    else:
        print()
        
def convert(time):
    hour,minutes=time.split(":")
    minutes=int(minutes)/60
    times=float(hour)+float(minutes)
    return times

if __name__=="__main__":
    main()
