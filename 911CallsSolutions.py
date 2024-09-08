import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', None)

# Load the dataset
file_path = '/Users/jainamtated/Downloads/911.csv'
df = pd.read_csv(file_path)

# Inspect the dataframe
#print(df.info())
#print(df['title'].nunique())

# Extract reason from the title column
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])

# Display reason counts
#print(df['Reason'].value_counts())

# Plot reason counts
sns.countplot(x='Reason', data=df, palette='viridis')
plt.title('Count of 911 Calls by Reason')
plt.show()

# Convert timestamp column to datetime
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# Create new time-related columns
df['month'] = df['timeStamp'].apply(lambda time: time.month)
df['weekday'] = df['timeStamp'].apply(lambda time: time.dayofweek)
df['hour'] = df['timeStamp'].apply(lambda time: time.hour)

# Map numeric weekday to actual weekday name
dmap = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
df['weekday'] = df['weekday'].map(dmap)

# Plot count of 911 calls by weekday with reasons
sns.countplot(x='weekday', data=df, hue='Reason', palette='viridis')
plt.title('911 Calls by Day of Week')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

# Plot count of 911 calls by month with reasons
sns.countplot(x='month', data=df, hue='Reason', palette='viridis')
plt.title('911 Calls by Month')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

# Plot count of 911 calls by hour with reasons
sns.countplot(x='hour', data=df, hue='Reason', palette='viridis')
plt.title('911 Calls by Hour')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

# Group by month
bymonth = df.groupby('month').count()
df_bymonth = bymonth.reset_index()

# Print grouped data by month
print(df_bymonth)

# Linear regression plot of calls per month
sns.lmplot(x='month', y='twp', data=df_bymonth)
plt.xlabel('Month')
plt.ylabel('Number of 911 Calls')
plt.title('Linear Regression of 911 Calls over Month')
plt.show()

# Create date column for daily analysis
df['date'] = df['timeStamp'].dt.date

# Group by date
bydate = df.groupby('date').count()['lat']

# Plot daily 911 calls
plt.figure(figsize=(10, 6))
bydate.plot()
plt.title('911 Calls per Day')
plt.tight_layout()
plt.show()

# Filter data by reason and plot
for reason in df['Reason'].unique():
    df_reason = df[df['Reason'] == reason]
    byreason = df_reason.groupby('date').count()['Reason']
    plt.figure(figsize=(10, 6))
    byreason.plot()
    plt.xlabel('Date')
    plt.ylabel(reason)
    plt.title(f'911 Calls for {reason}')
    plt.tight_layout()
    plt.show()

# Create heatmaps for calls by day and hour
dayhour = df.groupby(['weekday', 'hour']).count()['Reason'].unstack()

# Heatmap of calls by day and hour
plt.figure(figsize=(12, 6))
sns.heatmap(dayhour, cmap='viridis')
plt.title('Heatmap of 911 Calls by Day and Hour')
plt.show()

# Cluster map of calls by day and hour
sns.clustermap(dayhour, cmap='viridis')
plt.show()

# Create heatmap for calls by day and month
daymonth = df.groupby(['weekday', 'month']).count()['Reason'].unstack()

# Heatmap of calls by day and month
plt.figure(figsize=(12, 6))
sns.heatmap(daymonth, cmap='coolwarm')
plt.title('Heatmap of 911 Calls by Day and Month')
plt.show()
