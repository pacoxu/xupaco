#!/usr/bin/python
# Filename: if.py


def guess1(number):
  running = True;
  print "guest __name__:",__name__
  while running==True:
    guess = int(raw_input('Enter an integer : '))
    if guess == number:
      print 'Congratulations, you guessed it.' # New block starts here
      print "(but you do not win any prizes!)" # New block ends here
      running = False;
    elif guess < number:
      print 'No, it is a little higher than that' # Another block
      # You can do whatever you want in a block ...
    else:
      print 'No, it is a little lower than that'
      # you must have guess > number to reach here

  print 'Done'
  # This last statement is always executed, after the if statement is executed 


guess1( 22 );
print 'guess another number'
number = 21;
guess1(number);
