# vacation-days
 Converts days into hours, minutes, and seconds

## Scope/Instructions
Write a program that prompts the user to enter the number of days they plan to spend on their next vacation. Then, computer and report how long that is in hours, in minutes, and in seconds.

Make sure your spacing and formatting are appropriate.

## Sample Run
    How many days do you plan to spend on your next vacation? 1

    That is equivalent to 24 hours or 1,440 minutes or 86,400 seconds.

## Pseudocode
### Main program logic
    START
      INPUT number of vacation days
      CALL days_to_hours function
      CALL hours_to_minutes function
      CALL minutes_to_seconds function
      PRINT vacation days in hours, minutes, and seconds
    END

### days_to_hours function
    START
      PASS IN: days
      CALCULATE days in hours by multiplying by 24
      RETURN hours
    END

### hours_to_minutes function
    START
      PASS IN: hours
      CALCULATE minutes by multiplying hours by 60
      RETURN minutes
    END

### minutes_to_seconds function
    START
      PASS IN: minutes
      CALCULATE seconds by multiplying minutes by 60
      RETURN: seconds
    END
