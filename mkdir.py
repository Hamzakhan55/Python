import os

if(not os.path.exists("Data")):
    os.mkdir("Data")

# for i in range(0,200):
#     os.mkdir(f"Data/Day {i+1}")


for i in range(0,200):
    os.rename(f"Data/Day {i+1}", f"Data/Tutorial {i+1}")