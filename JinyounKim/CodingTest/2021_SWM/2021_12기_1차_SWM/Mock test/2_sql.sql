/* 현재 TABLE들 조회
SHOW TABLES; 
*/ 

/* INSERT INTO customer (id, name, birthday, mileage) VALUES (1, 'Elice', "2010-01-15", 100);
INSERT INTO customer (id, name, birthday, mileage) VALUES (2, 'Cheshire', "2005-03-10", 100);
INSERT INTO customer (id, name, birthday, mileage) VALUES (3, 'Dodo', "2010-04-30", 100); */
INSERT INTO customer (id, name, birthday, mileage) 
VALUES 
    (1, 'Elice', "2010-01-15", 100),
    (2, 'Cheshire', "2005-03-10", 100),
    (3, 'Dodo', "2010-04-30", 100)
;

SELECT * FROM customer;