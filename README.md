# thoughtfulAi
Submission for Support Engineer role

Project:
A simple Python utility to determine the type of shipping based on package dimensions and mass.

--

Features:  
-Accepts package dimensions: width, height, length  
-Accepts package mass  
-Returns a shipping category based on size and weight rules  
	Outputs: Rejected, Special or Standard  

---
shipping.py Contains the sort() function  

Usage:  

from shipping import sort  

Example usage:  
shipping_type = sort(width=10, height=5, length=15, mass=12)  
print (f"Shipping type: {shipping_type}")  # Output: e.g., "Shipping type: Standard: No Bulky No Heavy"  
