bruce_willis = input('Are you a fan of Bruce Willis or Keanu Reaves? (Pick one)')
if bruce_willis.lower() == 'bruce' or bruce_willis.lower() == 'bruce willis':
    # (bruce_willis.lower() == 'bruce') or ('bruce willis') <-- evaluate as a boolean True/False non-empty
    christmas = input('How do you feel about Christmas? Good/bad? ')
    if christmas.lower() == 'good' or christmas.lower() == 'great':
        print('You really like Die Hard')
    else:
        yes_no = input('Does he see dead people? ')
        if yes_no.lower() == 'yes':
            print('You like the sixth sense')
        else:
            print('You are really into the Fifth Element')
else:
    yes_no = input('Is there a spoon? yes / no (y/n) ')
    if yes_no.lower() == 'yes' or yes_no.lower() == 'y':
        print('You must like John Wick better.')
    else:
        print('The matrix is your favorite movie.  ')
