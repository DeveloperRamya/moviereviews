import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you've already loaded your data into the 'movies_data' DataFrame

# Bar plot: Top 10 movies by IMDb rating
top_movies = movies_data.nlargest(10, 'IMDb Rating')
plt.figure(figsize=(12, 6))
sns.barplot(x='IMDb Rating', y='movie_name', data=top_movies, palette='viridis')
plt.title('Top 10 Movies by IMDb Rating')
plt.xlabel('IMDb Rating')
plt.ylabel('Movie Name')
plt.show()

# Scatter plot: IMDb rating vs. Gross total
plt.figure(figsize=(10, 6))
sns.scatterplot(x='IMDb Rating', y='gross_total', data=movies_data, color='blue')
plt.title('IMDb Rating vs. Gross Total')
plt.xlabel('IMDb Rating')
plt.ylabel('Gross Total (in millions)')
plt.show()

# Box plot: Distribution of IMDb ratings
plt.figure(figsize=(10, 6))
sns.boxplot(x='IMDb Rating', data=movies_data, color='orange')
plt.title('Distribution of IMDb Ratings')
plt.xlabel('IMDb Rating')
plt.show()