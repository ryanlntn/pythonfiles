#
# readposint.py
#

def readposint(prompt="Please enter a positive integer: "):
    while True:
        try:
            attempt = raw_input(prompt)
        
            if int(attempt) < 0:
                raise ValueError
            return int(attempt)
        
        except:
            print attempt + " is not a positive integer. Try again."
