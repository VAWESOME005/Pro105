import csv
import pandas as pd
import plotly_express as px
import math

with open("projectData.csv", newline= '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
n = len(data)
total = 0

for x in data:
    total += float(x)

mean = total/n

print(mean)
squared_list = []

for y in data:
    num = float(y) - mean
    num_sq = num**2
    squared_list.append(num_sq)

total_sum = 0

for i in squared_list:
    total_sum += i

divided = total_sum/(n-1)

standard_deviation = math.sqrt(divided)

print(standard_deviation)


