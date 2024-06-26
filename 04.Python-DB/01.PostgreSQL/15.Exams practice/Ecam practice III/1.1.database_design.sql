CREATE TABLE IF NOT EXISTS
	categories(
		id SERIAL PRIMARY KEY
		,name VARCHAR(50) NOT NULL
	)
;

CREATE TABLE IF NOT EXISTS
	addresses(
		id SERIAL PRIMARY KEY
		,street_name VARCHAR(100) NOT NULL
		,street_number INT NOT NULL CHECK (street_number > 0)
		,town VARCHAR(30) NOT NULL
		,country VARCHAR(50) NOT NULL
		,zip_code INT NOT NULL CHECK(zip_code > 0)
	)
;

CREATE TABLE IF NOT EXISTS
	publishers(
		id SERIAL PRIMARY KEY
		,name VARCHAR(30) NOT NULL
		,address_id	INT NOT NULL REFERENCES addresses ON UPDATE CASCADE ON DELETE CASCADE
		,website VARCHAR(40)
		,phone VARCHAR(20)
	)
;

CREATE TABLE IF NOT EXISTS
	players_ranges(
		id SERIAL PRIMARY KEY
		,min_players INT NOT NULL CHECK (min_players > 0)
		,max_players INT NOT NULL CHECK (max_players > 0)
	)
;

CREATE TABLE IF NOT EXISTS
	creators(
		id SERIAL PRIMARY KEY
		,first_name VARCHAR(30) NOT NULL
		,last_name VARCHAR(30) NOT NULL
		,email VARCHAR(30) NOT NULL
	)
;

CREATE TABLE IF NOT EXISTS
	board_games(
		id SERIAL PRIMARY KEY
		,name VARCHAR(30) NOT NULL
		,release_year INT NOT NULL CHECK(release_year > 0)
		,rating NUMERIC(2) NOT NULL
		,category_id INT REFERENCES categories ON UPDATE CASCADE ON DELETE CASCADE NOT NULL
		,publisher_id INT REFERENCES publishers ON UPDATE CASCADE ON DELETE CASCADE NOT NULL
		,players_range_id INT REFERENCES players_ranges ON UPDATE CASCADE ON DELETE CASCADE NOT NULL
	)
;

CREATE TABLE IF NOT EXISTS
	creators_board_games(
		creator_id INT REFERENCES creators ON UPDATE CASCADE ON DELETE CASCADE NOT NULL
		,board_game_id INT REFERENCES board_games ON UPDATE CASCADE ON DELETE CASCADE NOT NULL
	)
;
