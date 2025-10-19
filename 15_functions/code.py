def hello():
    print("Hello!")  # type: ignore


hello()

# -- Defining vs. calling --
# It's still all sequential!


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.") # type: ignore


print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Goodbye!")

# -- Don't reuse names --


# def print():
#     print("Hello, world!")  # type: ignore # Error!


# -- Don't reuse names, it's generally confusing! --
friends = ["Rolf", "Bob"]

def add_friend(): # type: ignore
    global friends
    friend_name = input("Enter your friend name: ")
    friends = friends + [friend_name]

add_friend()
print(friends)  

# -- Can't call a function before defining it --


def say_hello():
    print("Hello!") # type: ignore

say_hello() # type: ignore
# -- Remember function body only runs when the function is called --


def add_friend():
    friends.append("Rolf")


friends = []
add_friend()

print(friends) 
