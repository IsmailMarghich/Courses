import requests
import hashlib
import sys
def request_api_data(query_char): #a function that requests the API for how many times a password was used
    url = 'https://api.pwnedpasswords.com/range/' + query_char # string concatenate what u want to request to the link
    res = requests.get(url)
    if res.status_code != 200: #if the status code isnt 200 then raise an error
        raise RuntimeError(f' Error fetching: {res.status_code} check the api and try again')
    return res 

def get_password_leaks_count(hashes, hash_to_check): #this function splits what we get from the API and iterates over it to get the count of each hashed password
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count 
    return 0 #return 0 (False) if the password wasnt found

def pwned_api_check(password): #this function hashes the password that the user inputs and processes it with hexdigest so the API can read it
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:] #grab the head and tail which is used to identify passwords later on
    response = request_api_data(first5_char) #request the API with the head
    return get_password_leaks_count(response, tail) #request this function with the head and tail how many times this password has appared


def main(args): # a main function that will start the whole process
    for password in args: # for each password that the user enters
        count = pwned_api_check(password) #grab the count of how many times it appeared
        if count: #if the password had counts
            print(f'{password} was found {count} times... dont use this password') #print how many times it has been found
        else: #if the password wasnt count, and thus the count was False
            print(f'{password} was not found, carry on') #print that the password is safe
if __name__ == '__main__': #if this is the main file 
    main(sys.argv[1:]) #run the whole program with the command line arguments