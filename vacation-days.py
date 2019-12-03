# Vacation Days
# Shaun Hayworth
# CIS 2
# 12-02-2019
# Source code and revision history are available at
# https://github.com/SCHayworth/vacation-days

# This program gets a number of vacation days from the user and converts them
# into hours, minutes, and seconds.


# Define the main function.
def main ():
    '''This is the main program logic.
    '''
    # Prompt the user for the number of vacation days.
    vacation_days = int(input('How many days do you plan to spend on your next vacation? '))
    
    # Convert the days into hours, minutes, and seconds.
    vacation_hours = days_to_hours(vacation_days)
    vacation_minutes = mins_and_secs(vacation_hours)
    vacation_seconds = mins_and_secs(vacation_minutes)

    # Print the results to the screen.
    print(f'That is the equivalent to {vacation_hours:,} hours or {vacation_minutes:,} or {vacation_seconds:,} seconds.')


# Define the days_to_hours function.
def days_to_hours(days):
    '''Converts a given number of days into hours.
    '''
    # Calculate the number of hours in the supplied number of days and return
    # the result.
    hours = days * 24
    return hours


# Define the hours_to_minutes function.
def mins_and_secs(time):
    '''Converts a number of hours into minutes.
    '''
    # Calculate the number of minutes in the supplied number of hours and
    # return the result.
    min_sec = time * 60
    return min_sec


# Call the main() function to execute the program.
main()
