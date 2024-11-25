use footballdb;
-- -----------------------------------------------------
-- --------------------- Task 1 ------------------------
-- -----------------------------------------------------

-- -----------------------------------------------------
-- --------------------- On create ---------------------
-- -----------------------------------------------------

DROP TRIGGER IF EXISTS check_teams_exists;
DELIMITER //

CREATE TRIGGER check_teams_exists
BEFORE INSERT ON transfers
FOR EACH ROW
BEGIN
    -- Check if team_from exists
    IF NOT EXISTS (SELECT 1 FROM team WHERE id = NEW.team_from) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Team from ID does not exist';
    END IF;

    -- Check if team_to exists
    IF NOT EXISTS (SELECT 1 FROM team WHERE id = NEW.team_to) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Team to ID does not exist';
    END IF;
END;
//

DELIMITER ;


DROP TRIGGER IF EXISTS check_player_exists;
DELIMITER //

CREATE TRIGGER check_player_exists
BEFORE INSERT ON transfers
FOR EACH ROW
BEGIN
    -- Check if player_id exists
    IF NOT EXISTS (SELECT 1 FROM player WHERE id = NEW.player_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Player ID does not exist';
    END IF;
END;
//

DELIMITER ;

-- -----------------------------------------------------
-- --------------------- On Update ---------------------
-- -----------------------------------------------------

DROP TRIGGER IF EXISTS  check_teams_exists_update;
DELIMITER //

CREATE TRIGGER check_teams_exists_update
BEFORE UPDATE ON transfers
FOR EACH ROW
BEGIN
    -- Check if team_from exists
    IF NOT EXISTS (SELECT 1 FROM team WHERE id = NEW.team_from) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Team from ID does not exist';
    END IF;

    -- Check if team_to exists
    IF NOT EXISTS (SELECT 1 FROM team WHERE id = NEW.team_to) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Team to ID does not exist';
    END IF;
END;
//

DELIMITER ;

DROP TRIGGER IF EXISTS check_player_exists_update;
DELIMITER //

CREATE TRIGGER check_player_exists_update
BEFORE UPDATE ON transfers
FOR EACH ROW
BEGIN
    -- Check if player_id exists
    IF NOT EXISTS (SELECT 1 FROM player WHERE id = NEW.player_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Player ID does not exist';
    END IF;
END;
//

DELIMITER ;

-- -----------------------------------------------------
-- --------------------- Task 2 ------------------------
-- -----------------------------------------------------


-- -----------------------------------------------------
-- --------------------- 1 -----------------------------
-- -----------------------------------------------------

drop procedure if exists parametrized_insertion;

DELIMITER //
create procedure parametrized_insertion(in p_time float, in p_player_id int, in p_player_team_id int, in p_match_id int)
begin
insert into goal(time, player_id, player_team_id, match_id)
values (p_time, p_player_id, p_player_team_id, p_match_id);
end //
DELIMITER ;


-- -----------------------------------------------------
-- --------------------- 2 -----------------------------
-- -----------------------------------------------------

drop procedure if exists many_to_many_relation;
DELIMITER //

CREATE PROCEDURE many_to_many_relation(
    IN p_player_name text,
    IN p_player_surname text,
    IN p_lineup_id INT
)
BEGIN
    DECLARE p_player_id INT;
    DECLARE p_start_lineup_id INT;

    -- Знайти ID гравця за прізвищем та ім'ям
    SELECT id INTO p_player_id
    FROM player
    WHERE name = p_player_name AND surname = p_player_surname;

    -- Якщо гравця не знайдено, викликати помилку
    IF p_player_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Player not found';
    END IF;

    -- Знайти ID стартового складу за team_id
    SELECT id INTO p_start_lineup_id
    FROM start_lineup
    WHERE id = p_lineup_id;

    -- Якщо стартовий склад не знайдено, викликати помилку
    IF p_start_lineup_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Start lineup not found';
    END IF;

    -- Перевірити, чи зв’язок уже існує
    IF EXISTS (
        SELECT 1
        FROM player_has_start_lineup
        WHERE player_id = p_player_id AND start_lineup_id = p_start_lineup_id
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Player is already in the lineup';
    END IF;

    -- Вставити запис у стикову таблицю
    INSERT INTO player_has_start_lineup (player_id, start_lineup_id)
    VALUES (p_player_id, p_start_lineup_id);
END;
//

DELIMITER ;

-- -----------------------------------------------------
-- --------------------- 3 -----------------------------
-- -----------------------------------------------------

drop procedure if exists create_rows_in_table;
DELIMITER //
create procedure create_rows_in_table()
begin
	declare i int default 1;

    while i <= 10 do
		insert into player(name, surname, nationality, age, team_id)
        values (concat("Noname", i), concat("Noname", i), "Unknown", 20+i, i);
        set i = i +1;
	end while;
end //

DELIMITER ;


-- -----------------------------------------------------
-- --------------------- 4 -----------------------------
-- -----------------------------------------------------

drop procedure if exists get_info_about_capacity;
DELIMITER //
create procedure get_info_about_capacity(in p_type text, out result float)
begin
	declare res float default 0;
	case p_type
		when "MIN" then
			set res = (select MIN(s.capacity) from stadium as s);
		when "MAX" then
			set res = (select MAX(s.capacity) from stadium as s);
		when "SUM" then
			set res = (select SUM(s.capacity) from stadium as s);
		when "AVG" then
			set res = (select AVG(s.capacity) from stadium as s);
		ELSE
            signal SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid operation type.';
    end case;
    set result = res;
end //

DELIMITER ;

drop procedure if exists info_about_capacity;

DELIMITER //
create procedure info_about_capacity(in p_type text)
begin
CALL get_info_about_capacity(p_type, @result);
SELECT @result;
end //

DELIMITER ;

-- -----------------------------------------------------
-- --------------------- 5 -----------------------------
-- -----------------------------------------------------


drop procedure if exists create_dynamic_tables_from_leagues;
DELIMITER //

CREATE PROCEDURE create_dynamic_tables_from_leagues()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE league_name VARCHAR(255);
    DECLARE table_counter INT DEFAULT 0;
    DECLARE cur CURSOR FOR SELECT name FROM league;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    league_loop: LOOP
        FETCH cur INTO league_name;
        IF done OR table_counter = 10 THEN
            LEAVE league_loop;
        END IF;

        -- Generate a unique table name using league name and timestamp
        SET league_name = REPLACE(league_name, ' ', '_');
        SET @sql = CONCAT(
            'CREATE TABLE ', league_name, '_', UNIX_TIMESTAMP(),
            ' (id INT PRIMARY KEY AUTO_INCREMENT, column_1 VARCHAR(255));'
        );

        -- Execute the dynamic SQL
        PREPARE stmt FROM @sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        -- Increment the table counter
        SET table_counter = table_counter + 1;
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;


-- --------------------------------------------------
-- --------------------- Task 3 ---------------------
-- --------------------------------------------------

DROP TRIGGER IF EXISTS prevent_modification_on_fmatch;
DROP TRIGGER IF EXISTS prevent_delete_on_fmatch;

-- --------------------------------------------------
-- --------------------- 1 --------------------------
-- --------------------------------------------------

DELIMITER //

CREATE TRIGGER prevent_modification_on_fmatch
BEFORE UPDATE ON fmatch
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modifications are not allowed on fmatch table.';
END //

-- --------------------------------------------------
-- --------------------- 2 --------------------------
-- --------------------------------------------------

CREATE TRIGGER prevent_delete_on_fmatch
BEFORE DELETE ON fmatch
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deletion is not allowed on fmatch table.';
END //

DELIMITER ;

DROP TRIGGER IF EXISTS prevent_double_zero_insert;

-- --------------------------------------------------
-- --------------------- 3 --------------------------
-- --------------------------------------------------

DELIMITER //
CREATE TRIGGER prevent_double_zero_insert
BEFORE INSERT ON player
FOR EACH ROW
BEGIN
    IF RIGHT(NEW.age, 2) = '00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Values in column_name cannot end with two zeros.';
    END IF;
END //

DELIMITER ;
