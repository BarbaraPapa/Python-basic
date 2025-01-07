# Importing the json module to work with JSON data
import json

# Defining the function to read a JSON file
def readJsonFile(fileName):
    # Initializing an empty string to store the data from the file
    data = ""
    
    # Using a try/except block to handle possible errors when reading the file
    try:
        # Opening the file specified by fileName in read mode
        with open(fileName) as json_file:
            # Loading the JSON content from the file and storing it in the 'data' variable
            data = json.load(json_file)
    except IOError:
        # If there is an error (e.g., file not found), print an error message
        print("Could not read file")
    
    # Returning the data (empty string if there was an error, JSON data if successful)
    return data


