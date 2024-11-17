use footballdb;

DROP TRIGGER IF EXISTS prevent_modification_on_fmatch;
DROP TRIGGER IF EXISTS prevent_delete_on_fmatch;
DELIMITER //

CREATE TRIGGER prevent_modification_on_fmatch
BEFORE UPDATE ON fmatch
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modifications are not allowed on fmatch table.';
END //

CREATE TRIGGER prevent_delete_on_fmatch
BEFORE DELETE ON fmatch
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deletion is not allowed on fmatch table.';
END //

DELIMITER ;

DROP TRIGGER IF EXISTS prevent_double_zero_insert;
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
