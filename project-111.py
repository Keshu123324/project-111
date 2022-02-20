import random as rand
from tkinter import Y
import plotly.figure_factory as ff
import statistics as s
import plotly.graph_objects as go
import pandas as pd


df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

#calculating the mean and the standard deviation of the population data
population_mean=s.mean(data)
print("The population_mean is: ", population_mean)
std_deviation=s.stdev(data)
print("The standard deviation of population is: ",std_deviation)

#function to get the mean of the given data samples
def random_set_of_mean(counter):
    data_set=[]
    for i in range(0,counter):
        index=rand.randint(0,len(data)-1)
        value=data[index]
        data_set.append(value)

    mean=s.mean(data_set)
    return mean

#pass the no. of time you want the mean of the data points as a parameter in range function in for loop

mean_list=[]
for i in range(0,100):
    set_of_means=random_set_of_mean(30)
    mean_list.append(set_of_means)

#calculating the mean and the standard deviation of the sampling data
sampling_mean=s.mean(mean_list)
print("The sampling mean is: ", sampling_mean)
std_deviation=s.stdev(mean_list)
print("The standard deviation of sampling is: ",std_deviation)

#finding standard deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = population_mean-std_deviation, population_mean+std_deviation
second_std_deviation_start, second_std_deviation_end = population_mean-(std_deviation*2), population_mean+(std_deviation*2)
third_std_deviation_start, third_std_deviation_end = population_mean-(std_deviation*3), population_mean+(std_deviation*3)

#plotting the graph
mean=s.mean(data)
fig=ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[0,0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0,0.20], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0,0.20], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, first_std_deviation_start], y=[0,0.20], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0,0.20], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, first_std_deviation_start], y=[0,0.20], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, second_std_deviation_end], y=[0,0.20], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

#finding the z score using the formula
z_score = (sampling_mean-mean)/std_deviation
print("THe z score is =",z_score)

