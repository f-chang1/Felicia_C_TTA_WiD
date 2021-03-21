create database teams;
use teams;
show databases;

CREATE TABLE club (
    club_id INT AUTO_INCREMENT,
    player VARCHAR(100),
    age INT,
    PRIMARY KEY (club_id)
);

CREATE TABLE team (
    team_id INT AUTO_INCREMENT,
    player VARCHAR(100),
    team_name VARCHAR(100),
    PRIMARY KEY (team_id)
);

INSERT INTO club(player, age)
VALUES('John', 30),('Jane', 22),('Mary', 31),('David', 22),('Amelia', 27),('James', 27),('Joe', 31);

INSERT INTO team (player, team_name)
VALUES('John', 'Team A'),('Mary', 'Team A'),('Amelia', 'Team B'),('Joe', 'Team B');

SELECT club_id, club.player, age
FROM club 
INNER JOIN team
ON club.player = team.player;

SELECT * FROM club;
SELECT * FROM team;

SELECT * FROM team
WHERE team_name = "Team B";

SELECT * FROM club, team
WHERE club.player = team.player AND team_name = "Team A";

SELECT * FROM club
WHERE age between 20 and 30;