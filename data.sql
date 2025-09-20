INSERT INTO league (id, name, team_count)
VALUES
(1, 'Premier League', 20),
(2, 'La Liga', 20),
(3, 'Serie A', 20),
(4, 'Bundesliga', 18),
(5, 'Ligue 1', 20),
(6, 'Eredivisie', 18),
(7, 'Primeira Liga', 18),
(8, 'MLS', 27),
(9, 'Turkish Super Lig', 20),
(10, 'J-League', 18);


INSERT INTO stadium (id, name, capacity, location)
VALUES
(1, 'Old Trafford', 74879, 'Manchester, England'),
(2, 'Camp Nou', 99354, 'Barcelona, Spain'),
(3, 'San Siro', 80018, 'Milan, Italy'),
(4, 'Allianz Arena', 75000, 'Munich, Germany'),
(5, 'Parc des Princes', 47929, 'Paris, France'),
(6, 'Johan Cruyff Arena', 54765, 'Amsterdam, Netherlands'),
(7, 'Estadio da Luz', 64642, 'Lisbon, Portugal'),
(8, 'Mercedes-Benz Stadium', 71000, 'Atlanta, USA'),
(9, 'Vodafone Park', 41903, 'Istanbul, Turkey'),
(10, 'Nissan Stadium', 72000, 'Yokohama, Japan');

INSERT INTO team (id, name, league_id, stadium_id, coach)
VALUES
(1, 'Manchester United', 1, 1, 'Erik ten Hag'),
(2, 'Barcelona', 2, 2, 'Xavi Hernandez'),
(3, 'AC Milan', 3, 3, 'Stefano Pioli'),
(4, 'Bayern Munich', 4, 4, 'Thomas Tuchel'),
(5, 'Paris Saint-Germain', 5, 5, 'Luis Enrique'),
(6, 'Ajax', 6, 6, 'Alfred Schreuder'),
(7, 'Benfica', 7, 7, 'Roger Schmidt'),
(8, 'Atlanta United', 8, 8, 'Gonzalo Pineda'),
(9, 'Besiktas', 9, 9, 'Senol Gunes'),
(10, 'Yokohama F. Marinos', 10, 10, 'Kevin Muscat');
;

INSERT INTO player (id, name, surname, nationality, age, team_id)
VALUES
(1, 'Cristiano', 'Ronaldo', 'Portugal', 38, 5),
(2, 'Lionel', 'Messi', 'Argentina', 36, 2),
(3, 'Marcus', 'Rashford', 'England', 26, 1),
(4, 'Zlatan', 'Ibrahimovic', 'Sweden', 42, 3),
(5, 'Robert', 'Lewandowski', 'Poland', 35, 4),
(6, 'Frenkie', 'de Jong', 'Netherlands', 27, 6),
(7, 'Joao', 'Felix', 'Portugal', 24, 7),
(8, 'Thiago', 'Almada', 'Argentina', 23, 8),
(9, 'Cenk', 'Tosun', 'Turkey', 32, 9),
(10, 'Andres', 'Iniesta', 'Spain', 40, 10),
(11, 'Erling', 'Haaland', 'Norway', 23, 1),
(12, 'Kylian', 'Mbappe', 'France', 25, 5),
(13, 'Kevin', 'De Bruyne', 'Belgium', 32, 1),
(14, 'Sergio', 'Ramos', 'Spain', 37, 5),
(15, 'Jadon', 'Sancho', 'England', 24, 1),
(16, 'Paulo', 'Dybala', 'Argentina', 30, 3),
(17, 'Luka', 'Modric', 'Croatia', 38, 2),
(18, 'Neymar', 'Junior', 'Brazil', 32, 2),
(19, 'Virgil', 'van Dijk', 'Netherlands', 33, 4),
(20, 'Gianluigi', 'Donnarumma', 'Italy', 25, 5),
(21, 'Pedri', 'Gonzalez', 'Spain', 21, 2),
(22, 'Mason', 'Mount', 'England', 25, 1),
(23, 'Raheem', 'Sterling', 'England', 29, 4),
(24, 'Romelu', 'Lukaku', 'Belgium', 31, 3),
(25, 'Joshua', 'Kimmich', 'Germany', 29, 4),
(26, 'Harry', 'Kane', 'England', 31, 9),
(27, 'Bruno', 'Fernandes', 'Portugal', 29, 1),
(28, 'Eden', 'Hazard', 'Belgium', 33, 2),
(29, 'Achraf', 'Hakimi', 'Morocco', 25, 5),
(30, 'Alphonso', 'Davies', 'Canada', 23, 4);


INSERT INTO player_stat (id, scored, games_mark, games_played, player_id)
VALUES
(1, 15, 8.5, 30, 1),
(2, 12, 8.8, 29, 2),
(3, 10, 7.9, 28, 3),
(4, 7, 8.2, 27, 4),
(5, 23, 9.1, 31, 5),
(6, 5, 7.5, 28, 6),
(7, 9, 8.3, 29, 7),
(8, 6, 7.8, 27, 8),
(9, 11, 7.9, 30, 9),
(10, 3, 6.9, 20, 10);

INSERT INTO referee (id, name, surname, age, gender, position)
VALUES
(1, 'Michael', 'Oliver', 38, 1, 'Center Referee'),
(2, 'Antonio', 'Mateu', 46, 1, 'Assistant Referee'),
(3, 'Bjorn', 'Kuipers', 51, 1, 'Fourth Official'),
(4, 'Stephanie', 'Frappart', 40, 0, 'Center Referee'),
(5, 'Cuneyt', 'Cakir', 47, 1, 'Center Referee'),
(6, 'Sian', 'Massey-Ellis', 37, 0, 'Assistant Referee'),
(7, 'Daniele', 'Orsato', 47, 1, 'Center Referee'),
(8, 'Clement', 'Turpin', 41, 1, 'Assistant Referee'),
(9, 'Danny', 'Makkelie', 41, 1, 'VAR Referee'),
(10, 'Felix', 'Brych', 48, 1, 'Center Referee'),
(11, 'Mark', 'Clattenburg', 48, 1, 'Center Referee'),
(12, 'Nicola', 'Rizzoli', 52, 1, 'VAR Referee'),
(13, 'Bibiana', 'Steinhaus', 44, 0, 'Center Referee'),
(14, 'Howard', 'Webb', 53, 1, 'Center Referee'),
(15, 'Carlos', 'Velasco', 51, 1, 'Assistant Referee'),
(16, 'Sara', 'Gama', 34, 0, 'Fourth Official'),
(17, 'Artur', 'Dias', 43, 1, 'Center Referee'),
(18, 'Marija', 'Kurtes', 38, 0, 'Assistant Referee'),
(19, 'William', 'Collum', 45, 1, 'VAR Referee'),
(20, 'Ovidiu', 'Hategan', 42, 1, 'Center Referee'),
(21, 'Kateryna', 'Monzul', 42, 0, 'Center Referee'),
(22, 'Martin', 'Atkinson', 53, 1, 'Fourth Official'),
(23, 'Esther', 'Staubli', 43, 0, 'Assistant Referee'),
(24, 'Gianluca', 'Rocchi', 50, 1, 'Center Referee'),
(25, 'Stephanie', 'Lapa', 39, 0, 'VAR Referee');

INSERT INTO referee_team (id, referee_qty)
VALUES
(1, 4),
(2, 5),
(3, 4),
(4, 3),
(5, 4),
(6, 5),
(7, 4),
(8, 4),
(9, 4),
(10, 4);

INSERT INTO start_lineup (id, team_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO fmatch (id, home_team_id, away_team_id, referee_team_id, home_start_lineup, away_start_lineup, stadium_id, team_league_id)
VALUES
(1, 1, 2, 1, 1, 2, 1, 1),
(2, 3, 4, 2, 3, 4, 3, 2),
(3, 5, 6, 3, 5, 6, 5, 3),
(4, 7, 8, 4, 7, 8, 7, 4),
(5, 9, 10, 5, 9, 10, 9, 5),
(6, 2, 3, 6, 2, 3, 2, 6),
(7, 4, 5, 7, 4, 5, 4, 7),
(8, 6, 7, 8, 6, 7, 6, 8),
(9, 8, 9, 9, 8, 9, 8, 9),
(10, 10, 1, 10, 10, 1, 10, 10),
(11, 1, 3, 2, 1, 3, 1, 1),
(12, 2, 4, 1, 2, 4, 2, 2),
(13, 5, 7, 3, 5, 7, 3, 3),
(14, 6, 8, 2, 6, 8, 4, 4),
(15, 7, 9, 1, 7, 9, 5, 5),
(16, 8, 10, 3, 8, 10, 6, 6),
(17, 1, 4, 2, 1, 4, 7, 1),
(18, 2, 5, 3, 2, 5, 8, 2),
(19, 3, 6, 1, 3, 6, 9, 3),
(20, 4, 7, 2, 4, 7, 10, 4),
(21, 5, 8, 3, 5, 8, 1, 5),
(22, 6, 9, 1, 6, 9, 2, 6),
(23, 7, 10, 2, 7, 10, 3, 7),
(24, 8, 1, 3, 8, 1, 4, 8),
(25, 9, 2, 1, 9, 2, 5, 9);

INSERT INTO goal (id, time, player_id, player_team_id, match_id)
VALUES
(1, 12.5, 1, 1, 1),
(2, 34.0, 2, 2, 1),
(3, 45.5, 3, 3, 2),
(4, 67.0, 4, 4, 2),
(5, 89.5, 5, 5, 3),
(6, 21.0, 6, 6, 3),
(7, 39.0, 7, 7, 4),
(8, 52.5, 8, 8, 4),
(9, 74.0, 9, 9, 5),
(10, 90.0, 10, 10, 5);

INSERT INTO player_has_start_lineup (start_lineup_id, player_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(1, 11),
(2, 12),
(3, 13),
(4, 14),
(5, 15),
(6, 16),
(7, 17),
(8, 18),
(9, 19),
(10, 20),
(1, 21),
(2, 22),
(3, 23),
(4, 24),
(5, 25),
(6, 26),
(7, 27),
(8, 28),
(9, 29),
(10, 30);




INSERT INTO referee_has_referee_team (id, referee_id, referee_team_id)
VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 1, 2),
(12, 1, 3),
(13, 2, 3),
(14, 2, 4),
(15, 3, 4),
(16, 3, 5),
(17, 4, 5),
(18, 4, 6),
(19, 5, 6),
(20, 5, 7),
(21, 6, 7),
(22, 6, 8),
(23, 7, 8),
(24, 7, 9),
(25, 8, 9),
(26, 8, 10),
(27, 9, 10),
(28, 9, 1),
(29, 10, 1),
(30, 10, 2);

INSERT INTO match_stat (match_id, yellow_card, red_card, goals, possession)
VALUES
(1, 2, 0, 3, 57.5),
(2, 3, 1, 4, 49.8),
(3, 1, 0, 2, 65.2),
(4, 4, 1, 5, 47.6),
(5, 2, 0, 3, 52.3),
(6, 3, 1, 4, 58.1),
(7, 1, 0, 2, 44.7),
(8, 2, 1, 3, 55.9),
(9, 4, 0, 5, 60.5),
(10, 3, 1, 4, 46.8);
