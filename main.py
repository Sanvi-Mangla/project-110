import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import pandas as pd

df = pd.read_csv("data.csv")
data = df["claps"].tolist()

population_mean = st.mean(data)
print("population mean is :- ",population_mean)
std_deviation = st.stdev(data)
print("standard deviation is :- ",std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = st.mean(dataset)
    return mean

mean_list = []  
for i in range(0,100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

def show_fig(mean_list):
  fig = ff.create_distplot([mean_list],["Claps"],show_hist=False)
  fig.show()

first_std_deviation_start, first_std_deviation_end = population_mean-std_deviation, population_mean+std_deviation
second_std_deviation_start, second_std_deviation_end = population_mean-(2*std_deviation), population_mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = population_mean-(3*std_deviation), population_mean+(3*std_deviation)
print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)

## plotting the graph with traces
fig = ff.create_distplot([mean_list], ["claps"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean_list, mean_list], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
