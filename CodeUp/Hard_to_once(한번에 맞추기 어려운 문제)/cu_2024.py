def four_gigit_change(num):
	num_dict = dict()
	digit_dict = dict()
	s = ''

	num_dict = { 0: '', 1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구'}
	
	a = int(num/1000)
	b = int((num%1000)/100)
	c = int((num%100)/10)
	d = int((num%10))

	s += num_dict[a] + '천' if a > 0 else ''
	s += num_dict[b] + '백' if b > 0 else ''
	s += num_dict[c] + '십' if c > 0 else ''
	s += num_dict[d] if d > 0 else ''

	return s

n = int(input())
s = ''

a = int(n/1e8)
b = int((n%1e8)/1e4)
c = int((n%1e4))


s += four_gigit_change(a) + '억' if a>0 else ''
s += four_gigit_change(b) + '만' if b>0 else ''
s += four_gigit_change(c)if c>0 else ('영' if n == 0 else '')

print(s)



