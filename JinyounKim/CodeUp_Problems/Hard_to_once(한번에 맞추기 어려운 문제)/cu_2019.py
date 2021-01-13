# Print out root eaquation result with given input
a, b, c = map(int, input().split())

if (b**2-4*a*c) > 0:
	print('%.2f'%((-b+(b**2-4*a*c)**0.5)/(2*a)))
	print('%.2f'%((-b-(b**2-4*a*c)**0.5)/(2*a)))
elif (b**2-4*a*c) == 0:
	print('%.2f'%((-b)/(2*a)))
else:
	# Be careful demoninator < 0
	print('%.2f'%(-b/(2*a)), '+', '%.2f'%(((-(b**2)+4*a*c)**0.5)/(2*abs(a))), 'i', sep = '')
	print('%.2f'%(-b/(2*a)), '-', '%.2f'%(((-(b**2)+4*a*c)**0.5)/(2*abs(a))), 'i', sep = '')