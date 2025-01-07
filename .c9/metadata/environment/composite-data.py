{"filter":false,"title":"composite-data.py","tooltip":"/composite-data.py","undoManager":{"mark":47,"position":47,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":11},"action":"insert","lines":["import csv","import copy"],"id":48}],[{"start":{"row":1,"column":11},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":49},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":50}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":51}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["#"],"id":52}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":[" "],"id":53}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":34},"action":"insert","lines":["Creating a car inventory program"],"id":54}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":[" "],"id":56}],[{"start":{"row":2,"column":2},"end":{"row":2,"column":25},"action":"insert","lines":["Defining the dictionary"],"id":57}],[{"start":{"row":2,"column":25},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":58},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":[" "],"id":59}],[{"start":{"row":3,"column":2},"end":{"row":3,"column":20},"action":"insert","lines":["import the modules"],"id":60}],[{"start":{"row":7,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["myVehicle = {","    \"vin\" : \"<empty>\",","    \"make\" : \"<empty>\" ,","    \"model\" : \"<empty>\" ,","    \"year\" : 0,","    \"range\" : 0,","    \"topSpeed\" : 0,","    \"zeroSixty\" : 0.0,","    \"mileage\" : 0","}"],"id":61}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":62}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["# Defining the dictionary"],"id":63}],[{"start":{"row":17,"column":1},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":64},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["#"],"id":65}],[{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":[" "],"id":66}],[{"start":{"row":7,"column":2},"end":{"row":7,"column":21},"action":"insert","lines":["define a dictionary"],"id":67}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["#"],"id":68}],[{"start":{"row":19,"column":1},"end":{"row":19,"column":2},"action":"insert","lines":[" "],"id":69}],[{"start":{"row":19,"column":2},"end":{"row":19,"column":61},"action":"insert","lines":[" iterate over the initial keys and values of the dictionary"],"id":70}],[{"start":{"row":19,"column":61},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":71}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":38},"action":"insert","lines":["for key, value in myVehicle.items():","    print(\"{} : {}\".format(key,value))"],"id":72}],[{"start":{"row":21,"column":38},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":73},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]},{"start":{"row":22,"column":4},"end":{"row":23,"column":0},"action":"insert","lines":["",""]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "],"id":74}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":20},"action":"insert","lines":["myInventoryList = []"],"id":75}],[{"start":{"row":22,"column":1},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":76},{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"remove","lines":[" "],"id":77}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":["#"],"id":78}],[{"start":{"row":23,"column":1},"end":{"row":23,"column":2},"action":"insert","lines":[" "],"id":79}],[{"start":{"row":23,"column":2},"end":{"row":23,"column":48},"action":"insert","lines":["Define an empty list to hold the car inventory"],"id":80}],[{"start":{"row":24,"column":20},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":81},{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":82},{"start":{"row":27,"column":0},"end":{"row":27,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":27,"column":1},"end":{"row":27,"column":2},"action":"insert","lines":[" "],"id":83},{"start":{"row":27,"column":2},"end":{"row":28,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":28,"column":0},"end":{"row":48,"column":42},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:","    csvReader = csv.reader(csvFile, delimiter=',')  ","    lineCount = 0  ","    for row in csvReader:","        if lineCount == 0:","            print(f'Column names are: {\", \".join(row)}')  ","            lineCount += 1  ","        else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')"],"id":84}],[{"start":{"row":27,"column":2},"end":{"row":27,"column":34},"action":"insert","lines":["Copying the CSV file into memory"],"id":85}],[{"start":{"row":48,"column":42},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":86},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]},{"start":{"row":49,"column":4},"end":{"row":50,"column":0},"action":"insert","lines":["",""]},{"start":{"row":50,"column":0},"end":{"row":50,"column":4},"action":"insert","lines":["    "]},{"start":{"row":50,"column":4},"end":{"row":51,"column":0},"action":"insert","lines":["",""]},{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"remove","lines":["    "],"id":87}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":1},"action":"insert","lines":["#"],"id":88}],[{"start":{"row":51,"column":1},"end":{"row":51,"column":2},"action":"insert","lines":[" "],"id":89}],[{"start":{"row":51,"column":2},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":90}],[{"start":{"row":52,"column":0},"end":{"row":55,"column":22},"action":"insert","lines":["for myCarProperties in myInventoryList:","    for key, value in myCarProperties.items():","        print(\"{} : {}\".format(key,value))","        print(\"-----\")"],"id":91}],[{"start":{"row":55,"column":22},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":92},{"start":{"row":56,"column":0},"end":{"row":56,"column":8},"action":"insert","lines":["        "]},{"start":{"row":56,"column":8},"end":{"row":57,"column":0},"action":"insert","lines":["",""]},{"start":{"row":57,"column":0},"end":{"row":57,"column":8},"action":"insert","lines":["        "]},{"start":{"row":57,"column":8},"end":{"row":58,"column":0},"action":"insert","lines":["",""]},{"start":{"row":58,"column":0},"end":{"row":58,"column":8},"action":"insert","lines":["        "]},{"start":{"row":58,"column":8},"end":{"row":59,"column":0},"action":"insert","lines":["",""]},{"start":{"row":59,"column":0},"end":{"row":59,"column":8},"action":"insert","lines":["        "]},{"start":{"row":59,"column":8},"end":{"row":60,"column":0},"action":"insert","lines":["",""]},{"start":{"row":60,"column":0},"end":{"row":60,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":60,"column":4},"end":{"row":60,"column":8},"action":"remove","lines":["    "],"id":93},{"start":{"row":60,"column":0},"end":{"row":60,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":51,"column":1},"end":{"row":51,"column":2},"action":"insert","lines":[" "],"id":94}],[{"start":{"row":51,"column":2},"end":{"row":51,"column":28},"action":"insert","lines":["Printing the car inventory"],"id":95}]]},"ace":{"folds":[],"scrolltop":119.99999422986997,"scrollleft":0,"selection":{"start":{"row":11,"column":25},"end":{"row":11,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":8,"state":"start","mode":"ace/mode/python"}},"timestamp":1736177708144,"hash":"191c7da5cd6503ab90fd496a936c48fcf67b8c6f"}