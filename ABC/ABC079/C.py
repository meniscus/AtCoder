# きたない。。。。
def get_formula(a,b,c,d) :
	for f1 in range(2) :
		s = str(a)
		if (f1 == 0) :
			s += "+"
		else : 
			s += "-"
		
		s += str(b)
		for f2 in range(2) :
			s2 = s
			if (f2 == 0) :
				s2 += "+"
			else : 
				s2 += "-"
			
			s2 += str(c)
			for f3 in range(2) :
				s3 = s2
				if (f3 == 0) :
					s3 += "+"
				else : 
					s3 += "-"
				
				s3 += str(d)
				if (eval(s3) == 7) :
					return s3

a,b,c,d = [int(i) for i in list(input())]

print(get_formula(a,b,c,d) + "=7")