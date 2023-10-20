import random
import sys
import time

PAUSE = 0.15
#Change it to 0.0 and see what happens

#Rows of DNA animation

ROWS = [
  '         ##', # Index 0 has no {}.
  '        #{}-{}#',
  '       #{}---{}#',
  '      #{}-----{}#',
  '     #{}------{}#',
  '    #{}------{}#',
  '    #{}-----{}#',
  '     #{}---{}#',
  '      #{}-{}#',
  '        ##',
  '       #{}-{}#',
  '       #{}---{}#' ,
  '      #{}-----{}#' ,
  '      #{}------{}#' ,
  '       #{}------{}#' ,
  '        #{}-----{}#' , 
  '         #{}---{}#' ,
  '          #{}-{}#' ,
  '           #{}-{}#' ,
]

#123456789 measure the number of spaces

try: 
  print('DNA Visualization || Risa Luthor')
  print('Press CTRL-C on keyboard to quit...')
  time.sleep(2)
  rowIndex = 0
  
  #Main loop of program || Started
  while True:
    #incrementing for to draw a next row:
    rowIndex = rowIndex +1
    if rowIndex == len(ROWS):
      rowIndex = 0
      
    #Row indexes 0 and 9 don't have nucldeotides:
    if rowIndex == 0 or rowIndex ==9:
      print(ROWS[rowIndex])
      continue
    
    randomSelection = random.randint(1,4)
    if randomSelection ==1:
      leftNucleotide, rightNucleotide = 'A', 'T'
    elif randomSelection ==2:
      leftNucleotide, rightNucleotide = 'T', 'A'
    elif randomSelection ==3:
      leftNucleotide, rightNucleotide = 'C', 'G'
    elif randomSelection ==4:
      leftNucleotide, rightNucleotide = 'G', 'C'
      
    #Print the row
    print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
    time.sleep(PAUSE)
    
except: 
  SystemExit()
#This will end the program, when click CTRL-C.
