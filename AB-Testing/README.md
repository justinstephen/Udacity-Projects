# Experiment Design

## **Metric Choice**

**Invariant Metrics:**
* Number of cookies
* Number of clicks
* Click-through-probability

**Evaluation Metrics:**
* Gross Conversion
* Net Conversion

**Metric Rationale:**
* **Number of cookies** was selected as it is a very evenly distributed metric across both the control and experiment groups
* **Number of user-ids** was not selected as an invariant metric as we would like to test this change on *new visitors*, who may or may not necessarily be assigned a user-id yet. This was not selected as an evaluation metric, although it is being used in the evaluation metrics for gross conversion and net conversion.
* **Number of clicks** is another metric that would be excellent as an invariant metric, as it should be the same across both groups.
* **Click through probability** is also unaffected by the change we are making and should be the same across the control and experiment groups.
* **Gross Conversion** is driving to the heart of what we would like to test here. This will help us explore the impact of our change by evaluating the amount of users who still complete checkout after completing the small quiz about how much time they have to dedicate to the course.
* **Retention** was originally selected as an evaluation metric, but unfortunately this data would take far too long to collect for statistical significance, as the pool of users is so much smaller than the pool of page views.
* **Net conversion** was selected as our other evaluation metric as it gives us an accurate representation of those who complete the first 14 days and decide that they would like to continue taking the course.

For **gross conversion** we will be looking for a decrease, and for **net conversion**, an increase.

## Measuring Standard Deviation
| **Metric**| **Standard Deviation**|
| :---|---:|
| Gross conversion|.0202|
| Net conversion|.0156|

Because each of these metrics uses cookies as their denominator, and we are using the cookies as our unit of diversion, an analytical estimate will be appropriate.

## Sizing
### Number of Samples vs. Power
The Bonferroni correction was not needed, and the amount of page views needed will be **685325**.

### Duration vs. Exposure
I would divert 50% of the traffic to this change, which would require 35 days to run. This is the section of the analysis where it was determined that the **retention** metric would simply take too long to track.

The experiment is not necessarily risky, even though it discourages people from signing up if they do not have the time. The amount of people who continue should have a higher conversion rate. This means that the net change should not have much impact, although user satisfaction should be much h igher. If it were determined that the experiment needed to be run in a shorter time period, a larger amount of traffic could be diverted without much risk.

# Experiment Analysis
## Sanity Checks
| **Metric**| **Lower bound**|**Upper bound**|**Observed**|**Passes**|
| :---|---:|---:|---:|---:|
| Number of cookies|.4988|.5012|.5006|**Yes**|
| Number of clicks|.4959|.5041|.5005|**Yes**|
| Click-through-probability|.0812|.0830|.0822|**Yes**|
Each of the sanity checks passes. These will be appropriate invariant metrics just as we initially thought.

## Result Analysis
### Effect Size Tests
| **Metric**| **Lower bound**|**Upper bound**|**Statistical Significance**|**Practical Significance**|
| :---|---:|---:|---:|---:|
| Gross conversion|-0.0291|-0.120|**Yes**|**Yes**|
| Net conversion|-0.0116|0.0018|**No**|**No**|

### Sign Tests
| **Metric**| **p-value**|**Statistical Significance**|
| :---|---:|---:|
| Gross conversion|.0026|**Yes**|
| Net conversion|.6776|**No**|

### Summary
I did not use the Bonferroni correction, as we require both of these metrics to show both significance, and not just one. The results from the effect size test and sign test do not show discrepancies, although we can now see that net conversion was not impacted as we thought it might.

## Recommendation
Gross conversion was negatively impacted by the change as expected. Net conversion was not impacted as we had hoped. By adding the quiz we are discouraging users from signing up if they do not have an appropriate amount of time, which will decrease the amount of users who sign up and are unhappy with the product. Without a decrease in net conversion though, this is an acceptable change that will (at the very least), not decrease revenue. My recommendation is to explore other designs that outline the expectations and course material but increase net conversion.

# Follow-Up Experiment
## Experiment 1
For a follow up experiment, I would like to test adding a pop-up for users who were seven days into the 14-day trial. This pop-up would offer a brief survey about how the course was going up to this point, and provide a link to offer feedback or help. This would at the very least provide feedback to Udacity about how the users feel seven days into the trial, and at the best, help people who had maybe stumbled or were unsure of their progress.

My hypothesis would be that **retention** would increase after implemnting this poll for users in the middle of the 14-day trial.

The unit of diversion would be by **user-id**, although it may be fair to offer this feature to all users and compare the metrics to past data.

The invariant metric would be number of **user-ids**.

The evaluation metric would be **retention** although we would also like to view the probability of people completing the survey. We could compare the satisfaction rating of the poll to the retention rate of those users. We would hopefully see a higher retention rate among all trial users, and hopefully gain valuable feedback about what specifically the user is having issues with (if anything at all).

## Experiment 2
For a follow up experiment, I would want to test expanding the 14-day trial into a 30-day trial. This would give the students more time to explore the material and get a feel for how long the courses might take. Nanodegrees have many courses and each course has its own material and challenges. This would allow them to fully explore all the courses and final projects as well as pace the material.

My hypothesis would be that **Gross Conversion**, **Net Conversion**, and **Retention** would increase with the 30-day trial.

The unit of diversion would be by cookie, although it may be disingenuous to provide a 14-day trial to some users and a 30-day to others. In this case it may be better to offer the 30-day trial as a promotion and compare the data to historical data.

The invariant metrics would be the same as before, **number of cookies**, **number of clicks**, and **click through conversion**. We would especially be interested in how many more people click on the "Start Now" button.

The evaluation metrics would be **Gross Conversion**, **Net Conversion**, and **Retention**. We would be interested in seeing how many people click on the start now button (which would hopefully increase with a longer trial time), but also that people would be more inclined to continue past the trial period.

We would be looking for a positive increase in gross conversion and net conversion, but the real confirmation would be an increase in **Retention**.

# Sources
https://vwo.com/ab-testing/
