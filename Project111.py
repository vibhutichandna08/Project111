import pandas as pd
import statistics as s
import plotly.graph_objects as go
import plotly.figure_factory as pf
import random

df = pd.read_csv('Project111_data.csv')
data = df['reading_time'].tolist()
popMean = s.mean(data)
print(popMean)


def randomsetofmean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = s.mean(dataset)
    return mean
    


meanlist = []


def setup():
    for i in range(0, 100):
        setofmeans = randomsetofmean(30)
        meanlist.append(setofmeans)
    listmean = s.mean(meanlist)
    liststd = s.stdev(meanlist)
    first_std_start, first_std_end = popMean-liststd, popMean+liststd
    second_std_start, second_std_end = popMean-(liststd*2), popMean+(liststd*2)
    third_std_start, third_std_end = popMean-(liststd*3), popMean+(liststd*3)
    newsamplemean = s.mean(data)
    z_score = (newsamplemean-listmean)/liststd
    print('Mean of sampling distribution: ', listmean)
    print('Standard deviation of sampling distribution: ', liststd)
    print('Mean of sample1: ', newsamplemean)
    print('Z Score: ', z_score)
    plot_graph(listmean, first_std_end, second_std_end,
               third_std_end, newsamplemean)


def plot_graph(listmean, first_std_end, second_std_end, third_std_end, newsamplemean):
    fig = pf.create_distplot([meanlist], ['student marks'], show_hist=False)
    fig.add_trace(go.Scatter(x=[listmean, listmean], y=[
                  0, 0.20], mode='lines', name='Mean'))
    fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[
                  0, 0.17], mode='lines', name='std 1'))
    fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[
        0, 0.17], mode='lines', name='std 2'))
    fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[
        0, 0.17], mode='lines', name='std 3'))
    fig.add_trace(go.Scatter(x=[newsamplemean, newsamplemean], y=[
        0, 0.17], mode='lines', name='New Sample Mean'))
    fig.show()


setup()
