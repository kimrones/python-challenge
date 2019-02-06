# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:53:31 2019

@author: rones
"""

import os
import csv

PLtotal = 0
total_months = 0
GInum = 0
GDnum = 0
first = 'y'
#def financial_analysis(data):
      
       
 #     PLrow=int(row[1])
      
#      PLtotal += PLrow
       
    
with open('budget_data.csv', newline='') as csvfile:
   budgetreader = csv.reader(csvfile, delimiter=',')
   
   next(budgetreader, None)
 #   writer = csv.writer(csvfile)
       
   
   for row in budgetreader:
       
  #     financial_analysis(row)
  #        writer.writerow(row)
  
      total_months += 1
      
      PLrow=int(row[1])
      
      PLtotal += PLrow
      
      
      
      if GInum < int(row[1]):
         GInum = int(row[1])
         Idate = row[0]
     
      if GDnum > int(row[1]):
         GDnum = int(row[1])
         Ddate = row[0]

      while first == 'y':
          initial_value = int(row[1])
          first = 'n'
        
      final_value = int(row[1])
      
   average_change = round(((final_value - initial_value) / initial_value) * 100, 2)
   
      
     
   
print("Financial Analysis")
print("-------------------------------------") 
print(f"Total number of months: {total_months}")
print(f"Net Total: {PLtotal}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {Idate} ({GInum})")
print(f"Greatest Decrease in Profits: {Ddate} ({GDnum})")


with open('financial_analyst.txt', 'w', newline = '') as csvfile:
    
    txtfile = csv.writer(csvfile, delimiter=' ')
    
    
    txtfile.writerow("Financial Analysis")

    txtfile.writerow("----------------------------")
    
    txtfile.writerow(f"Total number of months: {total_months}")
    
    txtfile.writerow(f"Net Total: {PLtotal}")
    
    txtfile.writerow(f"Average Change: {average_change}")
    
    txtfile.writerow(f"Greatest Increase in Profits: {Idate} ({GInum})")
    
    txtfile.writerow(f"Greatest Decrease in Profits: {Ddate} ({GDnum})")

    
    


   