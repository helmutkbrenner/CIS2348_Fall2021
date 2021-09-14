# Helmut Brenner #
# 2037275 #

if __name__ == '__main__':

    # Dictionary is a good choice for holding this type of correlated data.
    services = {
        'Oil change': 35,
        'Tire rotation': 19,
        'Car wash': 7,
        'Car wax': 12,
        '-': 'No service'
    }

    # Normally would not use this many print statements but we have not learned loops yet...
    print('Davy\'s auto shop services')
    print('Oil change -- ${}'.format(services['Oil change']))
    print('Tire rotation -- ${}'.format(services['Tire rotation']))
    print('Car wash -- ${}'.format(services['Car wash']))
    print('Car wax -- ${}\n'.format(services['Car wax']))

    # Collect the desired services from user.
    service1 = str(input('Select first service:\n'))
    service2 = str(input('Select second service:\n'))

    # printing/calculating  the invoice using the dictionary and if statements to check for 'No service' option
    print('\nDavy\'s auto shop invoice\n')
    if service1 == '-':
        print('Service 1: {}'.format(service1))
        print('Service 2: {}, ${}'.format(service2, services[service2]))
        print('\nTotal: ${}'.format(services[service2]))
    elif service2 == '-':
        print('Service 1: {}, ${}'.format(service1, services[service1]))
        print('Service 2: {}'.format(service1))
        print('\nTotal: ${}'.format(services[service1]))
    else:
        print('Service 1: {}, ${}'.format(service1, services[service1]))
        print('Service 2: {}, ${}'.format(service2, services[service2]))
        print('\nTotal: ${}'.format(services[service1] + services[service2]))
