
# Scatterplot Of IMDB

This is the Scatterplot for top 250 movies in impb 

## Documentation

[Documentation](https://linktodocumentation)

Here I built Scatterplot for top 250 movies in imbd (rating v/s votes), i scrape the apis from imdb website using requests package, i use numpy package to send requests to multiple pages, and i parse the data getting from imdb to html with the help of BeautifulSoup package, i get all movies list details using findAll method in BeautifulSoup package.
Now i get the rating and number of votes of all movies in ratings list and votes list, i sorted those lists using key value. To build a Scatterplot i import matplotlib package and i get pyplot from matplotlib package, i took votes as x-axis and ratings as y-axis in scatterplot because ratings are dependent on votes.
