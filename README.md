# zoombombing
zoombombing is used to brute force through zoom IDs'.
This script works by running through every number through 999999999 and adding to the back of the url for testing.
Once the url is created the script opens the url in chrome and checks if the url redirects the user to zoom.
if the url does not redirect the user that means the id is invalid and the script knows to exit chrome and run the next possible url.

to run this script download the script and simply run:
    
    
    cd zoombombing
    python3 ./main.py
