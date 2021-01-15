# 피타고라스의 복수
https://codeup.kr/problem.php?id=2101

## Solution
A\*A  
= C\*C - B\*B  
= (C-B)\*(C+B)  

we know that C-B < C+B, so C-B<A  
then, we can iterate C-B in range of [1, A).  

Among iteration,  
we should find C-B value s.t. (A*A)%(C-B)=0 and (C-B)+(C+B) is even.  
(then, we can sure that C and D are integer)  

Among that like C and B,  
count s.t. B>A;

## Trouble Shooting
long long... 써야돼...