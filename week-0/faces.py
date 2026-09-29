def main():
    face = input()
    print(convert(face))

def convert(x):
    x= x.replace(":)","🙂")
    x = x.replace(":(","🙁")
    return x

main()
