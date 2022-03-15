# Program displays correct mailing address
# Date:           15/ 11/ 2019

def mailing_label(name, city, state, zip, address):  # elements needed to perform function
    print('The correct format of this address is: ')
    print(name)  # first start with the name
    for l in address:  # prints out all addresses in the list
        print(l)
    print(city + ',', state, zip)  # correctly formatted city state and zip


name = input('Please enter full name: ')  # user inputted name
city = input('Please enter city: ')  # user inputted city
state = input('Please enter state: ')  # user inputted state
zip = input('Please enter zip code: ')  # user inputted zip
a = input('Please enter address (if more than one please separate with comma): ')  # user inputted addresses
address = a.split(', ')  # create list of addresses that user inputted
mailing_label(name, city, state, zip, address)  # call on function to correctly format our mailing label
print()
