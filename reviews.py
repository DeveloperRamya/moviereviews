import pandas as pd
import numpy as np
import pytest

# Define the first dataset
 data1 = {
   'index': [1, 2, 3, 4, 5],
    'movie_name': ['The Godfather', 'The Silence of the Lambs', 'Star Wars: Episode V - The Empire Strikes Back', 'The Shawshank Redemption', 'The Shining'],
    'year_of_release': [1972, 1991, 1980, 1994, 1980],
    'category': ['R', 'R', 'PG', 'R', 'R'],
    'run_time': ['175 min', '118 min', '124 min', '142 min', '146 min'],
    'genre': ['Crime, Drama', 'Crime, Drama, Thriller', 'Action, Adventure, Fantasy', 'Drama', 'Drama, Horror'],
    'imdb_rating': [9.2, 8.6, 8.7, 9.3, 8.4],
    'votes': ['1,860,471', '1,435,344', '1,294,805', '2,683,302', '1,025,560'],
    'gross_total': ['$134.97M', '$130.74M', '$290.48M', '$28.34M', '$44.02M']
}

# Define the second dataset
data2 = {
    'Position': [1, 2, 3, 4, 5],
    'Const': ['tt2085059', 'tt8425058', 'tt1210166', 'tt2084970', 'tt0133093'],
    'Title': ['Black Mirror', 'Brexit: The Uncivil War', 'Moneyball', 'The Imitation Game', 'The Matrix'],
    'IMDb Rating': [8.7, 7.0, 7.6, 8.0, 8.7],
    'Runtime (mins)': [60, 92, 133, 114, 136],
    'Year': [2011, 2019, 2011, 2014, 1999],
    'Genres': ['Drama, Mystery, Sci-Fi, Thriller', 'Biography, Drama, History', 'Biography, Drama, Sport', 'Biography, Drama, Thriller, War', 'Action, Sci-Fi'],
    'Num Votes': [619226, 17553, 453231, 808542, 2006315],
    'Release Date': ['2011-12-04', '2019-01-07', '2011-09-09', '2014-08-29', '1999-03-24'],
    'Directors': ['', 'Toby Haynes', 'Bennett Miller', 'Morten Tyldum', 'Lilly Wachowski, Lana Wachowski']
}

# Create pandas DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

Merge the two datasets on the 'index' and 'Position' columns
merged_df = pd.merge(df1, df2, left_on='index', right_on='Position')

Display the merged dataset
 print(merged_df)
# Convert 'gross_total' to numeric format
merged_df['gross_numeric'] = merged_df['gross_total'].replace('[\$,M]', '', regex=True).astype(float)

# Calculate average IMDb rating
average_rating = merged_df['IMDb Rating'].mean()

# Identify movies in the top 10% of IMDb ratings
top_10_percent = merged_df[merged_df['IMDb Rating'] > merged_df['IMDb Rating'].quantile(0.9)]

# Display the calculated values
print(f'Average IMDb Rating: {average_rating:.2f}')
print('\nMovies in the Top 10% of IMDb Ratings:')
print(top_10_percent[['movie_name', 'IMDb Rating']])

