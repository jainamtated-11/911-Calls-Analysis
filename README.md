

# 911 Calls Data Analysis

This project performs an exploratory data analysis (EDA) of 911 emergency calls. The data includes various information such as the time of the call, the reason for the call, and the location. The goal of this analysis is to uncover patterns in 911 calls, visualize trends, and gain insights into the factors affecting call frequency.

## Project Overview

### Dataset:
The dataset contains the following columns:
- **lat**: Latitude of the 911 call
- **lng**: Longitude of the 911 call
- **desc**: Description of the emergency
- **zip**: Zipcode of the call location
- **title**: The emergency type and subcategory
- **timeStamp**: Time when the call was made
- **twp**: Township where the emergency was reported
- **addr**: Address of the emergency
- **e**: Dummy variable (always 1)

### Key Objectives:
1. **Reason for 911 Calls**: Extract the primary reasons (categories) for 911 calls.
2. **Time-Based Analysis**: Explore patterns across different hours, days, and months.
3. **Trend Visualizations**: Visualize call frequencies using line plots, count plots, and heatmaps.
4. **Geographical Analysis**: Analyze the spatial distribution of calls using lat/lng data (not yet implemented).
5. **Clustering of Calls**: Use clustering techniques for call patterns by time (e.g., hours and days).

## Libraries Used:
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Matplotlib**: For basic plotting.
- **Seaborn**: For advanced visualizations.
- **Datetime**: To manipulate date and time data.

## Data Analysis and Visualizations:
1. **Reason for Calls**: Extracted from the `title` column and visualized using count plots.
2. **Time-Based Insights**:
   - Created new columns such as `hour`, `weekday`, and `month` from the `timeStamp` column.
   - Analyzed calls across different times of the day, days of the week, and months of the year.
   - Visualized using count plots, line plots, and regression plots.
3. **Heatmaps**:
   - Created heatmaps to analyze the distribution of 911 calls by time of day and day of the week.
   - Cluster maps were used to identify patterns in the calls.
4. **Reason-Specific Trends**:
   - For each reason (e.g., EMS, Fire, Traffic), analyzed daily trends over time using line plots.

## How to Run:
1. Install the required libraries:
   ```bash
   pip install numpy pandas matplotlib seaborn
   ```
2. Download the dataset from [this link](https://www.kaggle.com/mchirico/montcoalert) (or upload your dataset to the appropriate file path).
3. Run the `911_calls_analysis.py` script to generate all visualizations.

## Future Enhancements:
- **Geographical Analysis**: Use `lat` and `lng` columns to create geographical heatmaps of 911 calls.
- **Machine Learning**: Predict call frequency using time series forecasting or classification algorithms.
  
## Conclusion:
This project provides insights into 911 calls data, including the most frequent reasons for calls, the time of day and week they are most likely to occur, and visual representations of these trends.
