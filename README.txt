Summary:
This program uses Python to deliver several packages.  
All packages must be delivered by 2 trucks before the deadline.
My program uses a nearest neighbor algortihm to automatically deliver each package.
The trucks are loaded manually.

I created my Python application using PyCharm 2022.3.2 (Community Edition).  
I backed up my program using GitHub.  
I alternated between programming on my personal laptop and PC.  
I used GitHub to pull my project which allowed me to program on both the laptop and PC. 

What I learned:
Programming using Python.
Version control/GitHub.
Time complexity for algorithms.
Using code to automate functions.
Using hash maps. 
Reading/writing CSV files using Python. 

My program has a time complexity of O(n^3) space complexity of O(n^3)

Pseudo code for the closest neighbor algorithm:
Function Closest neighbor:
Pass in: Truck, address, hash of packages
J = 0
Total_distance = 0
    While the length of packages in truck is greater than 0:
         For address_index and name in the list of distances:
               If the address in the list matches the address
                     J equals the address index              
          End For
          Distance = 100
          Next_package = 0
          For package_index and package in the trucks current packages:
                 For index and item in the list of distances:
                       If the package address matches the address in the list of distance:
                            Try to find the distance using J and the current index:
                                   If the distance of item J on the current Index is less than Distance:
                                          Distance equals item J on the current index
                                          Next_package equals the current package
                             End Try
                             Except find the distance swapping J and the current index:
                                   If the distance of item current index on index J is less than Distance:
                                            Distance equals item current index on index J
                                            Next_package equals the current packages
                              End Except   
                         End if
                  End For
           total_Distance equals the total_distance + the current distance
           Calculate time using the distance traveled
           Using the hashmap, set the current packages delivered time to the current time                                                                                                                    p         plus the calculated time
           If the packages delivered time modulo 100 is greater than 60:
                     Add 100 to the time and subtract 60
           End if
           Set the truck time to the trucks time plus the calculated time
           If the trucks time modulo 100 is greater than 60:
                     Add 100 to the time and subtract 60
           The address equals the current packages address
           Delete the package from the truck
             End For
     End While
   After the final loop, calculate the distance back to the hub
   Add this to the trucks time and distance traveled
End Function
