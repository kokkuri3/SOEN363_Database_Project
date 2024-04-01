-- Reservation Trigger : Checks for overlapping reservations before allowing a new reservation to be inserted into the reservation table. If an overlap is detected, it raises an error to prevent the insertion.
DELIMITER $$
CREATE TRIGGER check_overlapping_reservations BEFORE INSERT ON reservation
FOR EACH ROW
BEGIN
    DECLARE existing_count INT;
    SET existing_count = (
        SELECT COUNT(*)
        FROM Reservation
        WHERE car_id = NEW.car_id
          AND (
            (NEW.rental_date BETWEEN rental_date AND return_date)
            OR (NEW.return_date BETWEEN rental_date AND return_date)
            OR (NEW.rental_date <= rental_date AND NEW.return_date >= return_date)
          )
    );
    IF existing_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Overlapping reservation detected';
    END IF;
END$$
DELIMITER ;
