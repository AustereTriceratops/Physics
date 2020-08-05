# Bak Sneppen Model

![](https://i.imgur.com/IoGMJw4.png)

A basic model of evolutionary behavior that shows self-organization and "avalanche" dynamics. 

## How it works
Agents in the model are arranged in a line and assigned random fitnesses between 0 and 1. Since this is a 1-D model, we can graph its time evolution with a 2-D heatmap as above.
At each timestep, the agent with the lowest fitness and its two neighbors go extinct and are replaced by three new species with random fitnesses. 
The reason a species neighbors are also targeted is to explicitly model codependence between some species in an ecosystem - 
if one species dies out, then it's likely that the other species which depend on it will die out as well.

Thanks to this, when the population has a high fitness overall then this process can target a single region for a long period of time. 
This is known as an "avalanche", and these form the tops of the "towers" in the figure above. 
