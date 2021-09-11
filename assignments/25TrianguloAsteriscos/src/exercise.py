
def main():
    x=int(input("Dame un numero: "))
    for i in range (x+1):
        y=x-i
        print (" "*y+"*"*i)
if __name__=='__main__':
    main()
