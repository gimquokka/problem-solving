# 산도측정
https://codeup.kr/problem.php?id=2021

## Idea
map을 사용해 빈도수를 구하고,  
이를 cnt배열과 val배열로 분리 후 cnt의 순서에 맞게 sorting.  
  
답이 나올 수 있는 값들을 저장하는 벡터 fv, sv를 만들고 cnt가 큰 순서대로 val값을 집어넣음  
<ol>
    <li> fv.size>1이면 fv내부에서 답 도출 </li>
    <li>fv.size==1이면</li> 
        <ul>sv벡터를 채워서 fv[0]과 sv벡터최대/최소를 계산해서 더 큰 값을 답으로 도출</ul>  
        <ul>만약 sv가 없으면, 답은 0 </ul>
</ol>