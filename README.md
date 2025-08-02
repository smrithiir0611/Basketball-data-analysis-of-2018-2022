# basketball-data-analysis-of-2018-2022
This repository contains an analysis of college basketball team performance from 2018 to 2022. It includes data exploration, correlation analysis, and key visualizations. The project compares AI-generated insights with local analysis to validate results.

Dataset
The dataset has 60 records covering multiple teams and seasons, with stats including wins, losses, points per game, assists, turnovers, and more.

Objectives
Identify which teams showed the most improvement in wins over these seasons.

Analyze which statistics have the strongest positive and negative correlations with wins.

Validate AI-generated visualizations by comparing with locally created charts.

Extract actionable insights to guide coaching decisions.

Methods
Data was loaded and processed using Pandas.

Summary statistics and correlation analyses were performed to identify key factors influencing wins.

Visualizations such as bar charts, histograms, scatter plots, pie charts, and box plots were created with Matplotlib and Seaborn.

Side-by-side comparison of AI-generated and local visualizations ensured accuracy and consistency.

Results
Assists and points per game show strong positive correlation with wins.

Turnovers and personal fouls are negatively correlated with wins.

Visualizations align well between AI-generated and local analysis, confirming the validity of findings.

How to Run
Clone this repo.

Make sure Python 3.x is installed with pandas, matplotlib, and seaborn.

Run scripts in order:

data_explore.py for initial exploration

validate_correlation.py for correlation checks

validate_visualizations.py for visualization validation
