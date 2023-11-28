DROP TABLE IF EXISTS movies;
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    genre TEXT,
    year INTEGER,
    imdb_rating REAL
);
INSERT INTO movies ('id','name','genre','year','imdb_rating') 
VALUES

1,The Godfather,"Crime, Drama",1972,9.2
2,The Silence of the Lambs,"Crime, Drama, Thriller",1991,8.6
3,Star Wars: Episode V - The Empire Strikes Back,"Action, Adventure, Fantasy",1980,8.7
4,The Shawshank Redemption,Drama,1994, 9.3
5,The Shining,"Drama, Horror",1980,8.4
6,Casablanca,"Drama, Romance, War",1942, 8.5
7,One Flew Over the Cuckoo's Nest,Drama,1975, 8.7
8,Indiana Jones and the Raiders of the Lost Ark,"Action, Adventure",,1981, 8.4
9,The Lord of the Rings: The Return of the King"Action, Adventure, Drama",2003,9
10,Star Wars: Episode IV - A New Hope,"Action, Adventure, Fantasy",1977,8.6
11,The Dark Knight,"Action, Crime, Drama",2008,9
12,The Godfather: Part II,"Crime, Drama",1974, 9
13,Aliens,"Action, Adventure, Sci-Fi",1986, 8.4