/*
문제
https://programmers.co.kr/learn/courses/30/lessons/59414
*/

SELECT ANIMAL_ID, NAME, date_format(DATETIME, '%Y-%m-%d')
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;