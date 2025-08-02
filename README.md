# Basketball-data-analysis-of-2018-2022
This repository contains an analysis of college basketball team performance from 2018 to 2022. It includes data exploration, correlation analysis, and key visualizations. The project compares AI-generated insights with local analysis to validate results.

Dataset:
The dataset has 60 records covering multiple teams and seasons, with stats including wins, losses, points per game, assists, turnovers, and more.

Objectives:

1. To identify which teams showed the most improvement in wins over these seasons.

2. To analyze which statistics have the strongest positive and negative correlations with wins.

3. To validate AI-generated visualizations by comparing with locally created charts.

4. To extract actionable insights to guide coaching decisions.

Methods:

1.Data was loaded and processed using Pandas.

2.Summary statistics and correlation analyses were performed to identify key factors influencing wins.

3.Visualizations such as bar charts, histograms, scatter plots, pie charts, and box plots were created with Matplotlib and Seaborn.

4.Side-by-side comparison of AI-generated and local visualizations ensured accuracy and consistency.

Results:

1.Assists and points per game show strong positive correlation with wins.

2.Turnovers and personal fouls are negatively correlated with wins.

3.Visualizations align well between AI-generated and local analysis, confirming the validity of findings.

How to Run

Clone this repo.

Make sure Python 3.x is installed with pandas, matplotlib, and seaborn.

Run scripts in order:

data_explore.py for initial exploration.

validate_correlation.py for correlation checks.

validate_visualizations.py for visualization validation.
