def myfunction():
    print("Hello, i am from MyFunction")
myfunction()
def mydetails(fname,lname):
    print(fname +" "+ lname )

mydetails("Ajit","Das")

def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil","Tobias","Linus")