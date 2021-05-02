/* 지시사항
멤버십 등급이 1등급인 고객을 찾아 
해당 고객의 아이디와 전체 기간에 대한 누적 구매액을 구하고 
출력 예시의 컬럼 명을 참고하여 컬럼 명을 변경한 후 출력하시오. */

select user_id as "고객 아이디", sum(l.price) as "누적 구매액"
from customer as c, library as l, orderInfo as o
where o.buyer_id = c.user_id and l.book_id = o.book_id and membership = 1
group by user_id;
