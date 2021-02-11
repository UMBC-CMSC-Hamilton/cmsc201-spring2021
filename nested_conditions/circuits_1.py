a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if (a and b) or c:
    print('yep')
else:
    print('nope')

d = int(input('Enter d: '))
e = int(input('Enter e: '))

# non-nested version
if ((not a or b) and c) or not (d and e):
    print('yes that is true for some reason')
else:
    print('no its not')

if (not a or b) and c:
    print('yes, first part true')
elif not (d and e):
    print('yes, second condition')
else:
    print('false no go')

if (a and b) and ((not c or d) and not e):
    print('this is the if statement we need')
else:
    print('yep this is totally false')

# nested version of it:

if a and b:
    # this would be necessary if input d e
    # done here
    if (not c or d) and not e:
        print('this is the if statement we also need')
    else:
        print('its partially true but not good enough')
else:
    print('no this is totally false')
