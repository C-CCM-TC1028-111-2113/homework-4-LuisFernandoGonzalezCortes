
def main():
    x = int(input("Enter a number: "))
    y=1
    z=1
    print ("0")
    print ("1")
    print ("1")
    i=0
    while i<x:
        num=y+z
        y=z
        z=num
        print (str(num))
        i+=1
if __name__=='__main__':
    main()
