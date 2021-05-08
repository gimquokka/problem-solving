/* 
문제
https://programmers.co.kr/learn/courses/30/lessons/59413
참고 
https://chanhuiseok.github.io/posts/db-6/
 */

-- 코드를 입력하세요
SET @hour := -1;

SELECT @hour := @hour+1 AS HOUR, 
    (SELECT COUNT(*) 
    FROM ANIMAL_OUTS 
    WHERE HOUR(DATETIME) = @hour) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23;