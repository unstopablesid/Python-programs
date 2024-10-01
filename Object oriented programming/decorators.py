def greet(fx):
    print("good morning")
    fx()
    print("your tasks")
    return max
@greet
def hello():
    print("Hello sir")
hello()