/*
문제
https://programmers.co.kr/learn/courses/30/lessons/59409  
*/

SELECT ANIMAL_ID, NAME, 
    IF(SEX_UPON_INTAKE LIKE 'Neutered%' or SEX_UPON_INTAKE LIKE 'Spayed%', 'O', 'X') AS 중성화
        FROM ANIMAL_INS
;

/*
SELECT  ANIMAL_ID,
        NAME,
        # 정규식 사용 REGEXP 'a|b' => a와 b가 포함되면 참
        IF(SEX_UPON_INTAKE REGEXP 'Neutered|Spayed', 'O' , 'X') AS 중성화
FROM    ANIMAL_INS
*/