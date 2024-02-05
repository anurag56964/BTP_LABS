# //////////////// STUDENT INFO /////////////////

# Student Name : Anurag Das
# Student ID   : 126031228
# Email        : adas35@myseneca.ca

# ///////////////////////////////////////////////

import matplotlib.pyplot as plt

def graphSnowfall(t):
  
  # Read and Save Data from txt
  snowfall_amount = []
  with open(t, 'r') as txtFile:
    for line in txtFile:
      try:
        # converting each line(numbers) to float numbers
        # line.strip() avoids any newline character or spaces
        # and only reads the number
        amount = float(line.strip()) 
        snowfall_amount.append(amount)
      except ValueError:
        print(f"ERROR READING LINE - {line.strip()}")
        #Shows Error But Also Continues
        continue
  # Setting Up Ranges
  ranges = ['0-10', '11-20', '21-30', '31-40', '41-50']
  # Initializes all ranges to zero like; [0, 0, 0, 0, 0]
  counts = [0] * len(ranges)

  for amount in snowfall_amount:
    if 0 <= amount <= 10:
        counts[0] += 1
    elif 11 <= amount <= 20:
        counts[1] += 1
    elif 21 <= amount <= 30:
        counts[2] += 1
    elif 31 <= amount <= 40:
        counts[3] += 1
    elif 41 <= amount <= 50:
        counts[4] += 1


  # PLOTTING DATA FOR GRAPH
  plt.figure(figsize=(10, 6))
  plt.bar(ranges, counts, color='black')
  plt.title('Snowfall Accumulation')
  plt.xlabel('Snowfall Range (cm)')
  plt.ylabel('Occurrences')
  plt.xticks(ranges)
  plt.show()

# Lets Set Example File Path
path = 'data.txt'
graphSnowfall(path)

