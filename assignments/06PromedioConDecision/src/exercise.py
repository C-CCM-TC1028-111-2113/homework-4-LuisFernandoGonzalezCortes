def main():
    x=float(input(""))
    y=1
    z=x
    while x >= 0:
        x=float(input(""))
        if x >= 0:
            z+=x
            y+=1
    p=z/y
    print("",p)
if __name__=='__main__':
    main()
