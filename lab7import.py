def add(x,y):
    result=x+y
    print(f"result={result}")
def sub(x,y):
    result=x-y
    print(f"result={result}")
def mul(x,y):
    result=x*y
    print(f"result={result}")
def div(x,y):
    if(y>0):
        result=x/y
        print(f"result={result}")
    else:
        print("division by zero not possible")