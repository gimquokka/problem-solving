SELECT o.buyer_id, o.buy_date, l.book_name, o.price 
from library l, orderInfo o
where 
l.book_name = Looking with Elice 
or  
("2020-07-27"<= o.buy_date and o.buy_date <= "2020-07-31")
order by l.buy_date;