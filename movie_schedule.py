current_movies = {}
current_movies['The Grinch'] = '11:00AM'
current_movies['Rudolph'] = '1:00PM'
current_movies['Frosty'] = '3:00PM'
current_movies['Vacation'] = '5:00PM'

print('Currently showing:')
for key in current_movies:
    print(key)

#set initial 'finished' status to 'N'. We will repeat this loop until the user indicates they are done.
finished = 'N'
finished_input = None

#define acceptable answers for Yes/No. Only a Y or N will be allowed.
answers = {'Y': 'Yes',
           'N': 'No'}


while finished == 'N':

    movie = input('Which movie would you like a showtime for?\n')
        
    showtime = current_movies.get(movie)
    if showtime == None:
        print('This movie isn\'t playing.')
    else:
        print(showtime)

    finished_input = input('Are you finished checking movies? Y/N\n')
    
    while answers.get(finished_input) == None:
        finished_input = input('Invalid response. Are you finished? Y/N\n')

    finished = finished_input

    if finished == 'Y':
        print('Thank you for using MovieCheck! Goodbye.')
        break
