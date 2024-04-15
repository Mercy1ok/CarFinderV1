choice1= "1. PRINT all Authorized Vehicles"
choice2 = "2. Exit"

AllowedVehiclesList = [
'Ford F-150',
'Chevrolet Silverado',
'Tesla CyberTruck',
'Toyota Tundra',
'Nissan Titan'
]

menu = """*************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter the following number below from the following menu:
1. PRINT all Authorized Vehicles
2. Exit"""

print (menu)

option = int( input("Enter your choice: "))

if option == 1:
  print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
  for vehicle in AllowedVehiclesList:
    print("               ")
    print(vehicle)
  print("               ")
  print (menu)
  
elif option == 2:
  print( "Thank you for using the AutoCountry Vehicle Finder, goodbye!")
else:
  print( "Invalid option" )