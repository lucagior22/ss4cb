def A(sorted_numbers,target_value):
	E=target_value;D=sorted_numbers;B=0;C=len(D)-1
	while B<=C:
		A=(B+C)//2;F=D[A]
		if F==E:return A
		elif E<F:C=A-1
		else:B=A+1
	return-1