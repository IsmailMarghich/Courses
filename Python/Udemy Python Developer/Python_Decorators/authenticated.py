# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True }# changing this will either run or not run the message_friends function.
def authenticated(fn):
    def wrapper(*args, **kwargs): #takes it all the arguments
        if args[0]['valid']: #looks for the first argument, which is the dictionary and looks if valid is true or not
            return fn(*args, **kwargs) 
    return wrapper #return the function if valid equals True
@authenticated #call the decorator
def message_friends(user):
    print('message has been sent')
message_friends(user1) #call for the function with the decorator called
