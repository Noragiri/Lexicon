def sleep_in(weekday, vacation):
    if weekday == False:
        return True
    if weekday == True:
        if vacation == True:
            return True
        else:
            return False
