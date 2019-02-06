# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 17:46:10 2019

@author: rones
"""

totalvotes = 0
name_count = {}
winner = None
import os
import csv
with open('election_data.csv', newline='') as csvfile:
   electionreader = csv.reader(csvfile, delimiter=',')
   
   next(electionreader, None)
   
   for voter, county, name in electionreader:
       
       totalvotes += 1
       
       if name in name_count:
           name_count[name] += 1
       else:
           name_count[name] = 1
       
       if winner is None or name_count[name] > name_count[winner]:
           winner = name
       
   print("Election Results")
   print("----------------------------")
   print(f"Total votes: {totalvotes}") 
   print("----------------------------")
   for name in name_count:
       print (f"{name}: {round((name_count[name]/totalvotes)*100,2)}% {name_count[name]}")
   print("----------------------------")
   print(f"Winner: {winner}")
   
     
with open('election_results.txt', 'w', newline = '') as csvfile:
    
    txtfile = csv.writer(csvfile, delimiter=' ')
    
    txtfile.writerow("Election Results")
    txtfile.writerow("----------------------------")
    txtfile.writerow(f"Total votes: {totalvotes}") 
    txtfile.writerow("----------------------------")
    
    for name in name_count:
       txtfile.writerow(f"{name}: {round((name_count[name]/totalvotes)*100,2)}% {name_count[name]}")
    txtfile.writerow("----------------------------")
    txtfile.writerow(f"Winner: {winner}")
            
       