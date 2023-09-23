def add_time(start_time, duration, starting_day_of_week=""):
    i = 0   #index for week_days
    week_days = ['Monday','Tuesday',
                'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']
    
    if starting_day_of_week in week_days:
        i = week_days.index(starting_day_of_week)

    if start_time.split()[1] == 'AM':
        am = True
    elif start_time.split()[1] == 'PM':
        am = False
    splitted = start_time.split(':')
    splitted_dur = duration.split(':')
    # the beginning value of hours
    hr = int(splitted[0])
    # the beginning value of minutes
    min = int(splitted[1][:2])
    # added duration to both - minutes and hours
    minutes = min + int(splitted_dur[1])
    hours = hr + int(splitted_dur[0])
    # giving variables default values so that if the conditional
    # where it's in is not executed, it will never be created 
    # therefore, using it in complitely another conditional will return error:)

    result_hours = hours
    ho = 0
    result_minutes = minutes

    # if added minutes are over 60, we're gonna have to change result_hours
    if minutes >= 60:
        subs = int(minutes/60)
        left = minutes%60
        result_hours = hours + subs
        result_minutes = left
    # if result_hours is over 24, we're gonna change i index (index for week_days)
    if result_hours >= 24:
        lef = result_hours % 24
        ho = int(result_hours/24)
        
        i+=ho

        
        result_hours = lef
        print(result_hours)
        # for every 24 hours, the weekday changes
    # if result_hours is over 12, it might effect AM and PM (depending on result_hours)
    if result_hours >= 12:
        h = result_hours % 12
        x = int(result_hours/12)
        result_hours = h
        if am == True:
            if x % 2 == 0:
                am = True
            else:
                am = False
        elif am == False:
            if x % 2 == 0:
                am = False
            else:
                am = True



# if index is over 7 or more,
# we will start the counting
# from the beginning.

    if i > 6:
        nashti = i%7
        i = nashti
        
    if am == True:
        amORpm = 'AM'
    elif am == False:
        amORpm = 'PM'
    # to say how many days later:
    if ho == 1:
        d_later = f"(next day)"
    else: 
        d_later = f"({ho} days later)"

    if result_minutes < 10:
        result_minutes = f"0{result_minutes}"
    
    # differentiating starting day of the week not specified and specified
    if starting_day_of_week == "":

        print(f"{result_hours}:{result_minutes} {amORpm} {d_later}")
    else:
        print(f"{result_hours}:{result_minutes} {amORpm}, {week_days[i]} {d_later}")

