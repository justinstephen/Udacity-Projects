## Summary:
For this project I decided to use a dataset of baseball players that includes the players' weight, height, handedness, and home run totals. I thought it would be interesting to look at the effect a player's size had on the amount of home runs that player hit. The weight is indicated in pounds while the height is measured in inches. It appears as though weight has a positive relationship on the amount of home runs a player hits, while it is best to have an average height.

## Design:
For the initial design I decided to use a scatterplot, as this is an excellent way to compare two features. After initial feedback, it seemed that this was too much data for the chart, and so I decided to switch to a bar chart, to make the data much easier to view. The data was first filtered, to not include players who had a batting average of zero, as these players were often not batting at all. The home run totals of each player were also binned and averaged into different weight categories (every 10 pounds for weight, and every 2 inches for height). This allowed me to easily see if there was any relationship between these variables and the players home run averages. These average were plotted out on a bar chart, using these weight bins as categories, but also formatted as continuous variables so that we could explore the weight and height as they increase and decrease. These  I added a line to the chart as well to provide greater visibility into the change between each category of weights/heights. Initially I had split the data based on handedness, but I decided that this was not valuable information to what the visualization was trying to portray. I had also initially explored the relationship between batting average and home runs, but after modifying the way the initial data was displayed, I decided it was not relevant to the variables being explored. 

## Feedback:
### Feedback #1:
Perhaps a possible relationship may be easier to detect from a kind of plot that reduces the visible amount of data, and rather provides some kind of summary. Right now, there is a large number of data points, and I find it hard to infer their distribution. Maybe a regression line (for each handedness-group) could point to any trend? Or turning one of the axes' variables into a categorical variable by forming groups and then making a boxplot?

### Feedback #2:
**What do you notice in the visualization?**
-The data is clean and easy to follow. I enjoy the fact that it isn't trying to tell too much in one graph. The first thing that I noticed in the data is the fact that there aren't any switch hitters (no matter their weight or height) that hit above 350 home runs.

**What questions do you have about the data?**
-I would like to know if the weight that they used for the data set is an average of their weight throughout their career or possibly the highest weight they were in their career 

**What relationships do you notice?**
-In the top ten amount of home runs hit (in the height and weight graphs) both were split even between left and right handers

**What do you think is the main takeaway from this visualization?**
-There doesn't seem to be a correlation between height/weight and home runs these players hit.

**Is there something you don’t understand in the graphic?**
-No, i understand all of the data. The visualization is clean, straightforward, and simple without boring me.

### Feedback #3:
**What do you notice in the visualization?**
The first thing I noticed about the data is that it is all tightly clustered in one region.

**What questions do you have about the data?**
What is the meaning of the legend? (B L R)

**What relationships do you notice?**
Like the description says, it is difficult to notice if there is any relationship at all.

**What do you think is the main takeaway from this visualization?**
That a players size does not effect the players home runs.

**Is there something you don’t understand in the graphic?**
I do not understand what the legend is.

### Feedback #4:
I found the groupings around the 5s digit on weight pretty interesting as a psychological thing, how we usually round to the 5s place on weight almost impulsively.  It also seems like 74" is the sweet spot when it comes to home runs for height, though that may not be the intended effect, just what the glance provides. It'd be interesting to see if the home run averages vs count could be weighted to something, though I don't know enough to say what that might be.

### Feedback #5:
--Udacity Project Feedback--

## Resources:
* http://dimplejs.org/examples_viewer.html?id=scatter_standard 
* http://dimplejs.org/examples_viewer.html?id=bars_vertical
