
# Importing the jsonFileHandler module to use its function for reading the JSON file
import jsonFileHandler

# Reading the JSON file using the readJsonFile function from jsonFileHandler module
data = jsonFileHandler.readJsonFile('files/insulin.json')

# Checking if data is not an empty string, indicating the file was successfully read
if data != "":
    # Extracting the 'bInsulin' and 'aInsulin' sequences from the 'molecules' section of the JSON
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    
    # Concatenating bInsulin and aInsulin to form the full insulin sequence
    insulin = bInsulin + aInsulin
    
    # Extracting the actual molecular weight of insulin from the JSON
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    
    # Printing the extracted insulin data
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
    # -----------------------------------
    # Molecular weight calculation process
    # Extracting the amino acid weights from the 'weights' section of the JSON
    aaWeights = data['weights']
    
    # Counting the occurrences of each amino acid in the insulin sequence
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in 
                      ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 
                       'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})
    
    # Calculating the molecular weight of insulin by multiplying the count of each amino acid
    # by its respective weight and summing them up
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
                                 ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 
                                  'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())
    
    # Printing the calculated rough molecular weight of insulin
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    
    # Calculating and printing the percent error between the calculated and actual molecular weight
    print("Percent error: " +
          str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
else:
    # If the data is empty, printing an error message
    print("Error. Exiting program")
