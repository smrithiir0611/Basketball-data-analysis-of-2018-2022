# Basketball-data-analysis-of-2018-2022

This repository contains an analysis of college basketball team performance from 2018 to 2022. It includes data exploration, correlation analysis, and key visualizations. The project compares AI-generated insights with local analysis to validate results.

## Dataset

The dataset contains 60 records covering multiple teams and seasons. It includes stats such as wins, losses, points per game, assists, turnovers, personal fouls, and more.

## Objectives

1. To identify which teams showed the most improvement in wins over these seasons.  
2. To analyze which statistics have the strongest positive and negative correlations with wins.  
3. To validate AI-generated visualizations by comparing them with locally created charts.  
4. To extract actionable insights to guide coaching decisions.

## Methods

1. Data was loaded and processed using Pandas.  
2. Summary statistics and correlation analyses were performed to find key factors influencing wins.  
3. Visualizations including bar charts, histograms, scatter plots, pie charts, and box plots were created using Matplotlib and Seaborn.  
4. Side-by-side comparisons of AI-generated and local visualizations ensured accuracy and consistency.

## Results

1. Assists and points per game show strong positive correlation with wins.  
2. Turnovers and personal fouls have negative correlation with wins.  
3. Visualizations generated locally and by AI align well, confirming the validity of the analysis.

## Project Structure

1. data_explore.py – Initial dataset exploration and summary statistics.  
2. validate_correlations.py – Correlation analysis between variables.  
3. validate_improvement.py – Analysis of improvement in wins across seasons.  
4. validate_summary_stats.py – Verification of summary statistics.  
5. data_visualize.py – Script to generate all main visualizations.  
6. barchart_viz_ctgpt.py – Bar chart of total wins per team.  
7. histogram_validationcode.py – Histogram of points scored distribution.  
8. scatter_validation.py – Scatter plot of assists vs points per game.  
9. piechart_validationcode.py – Pie chart showing win percentage by team.  
10.boxplot_validationcode.py – Box plot of points per game distribution by team.  
11.teamstats.csv – Dataset with team stats and season information.

## How to Run

1. Clone this repository.  
2. Make sure Python 3.x is installed with `pandas`, `matplotlib`, and `seaborn` packages.  
3. Run the scripts in this order:  
   - data_explore.py
   - validate_correlations.py  
   - validate_improvement.py  
   - validate_summary_stats.py 
   - data_visualize.py



