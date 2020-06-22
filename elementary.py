
def humanSize(minumero,nsfx,last):
	try: 
		float(minumero)
	except: 
		print('please, enter a positive number')
		return False

	minumero = float(minumero)
	SUBFIX = ['B','KB','MB','GB','PB','EB','ZB','YB']
	minumero = str(minumero)
	minumeropices = minumero.split('.')
	minumero = minumeropices[0]
	if len(minumero)>20:
		print('%s %s',(minumero, 'YB'))
		return False
	if len(minumero)<=3:
		if last == 0:
			answer = '%s.%s %s'%(minumero,minumeropices[1],SUBFIX[nsfx])
		else:
			answer = '%s.%s %s'%(minumero,last,SUBFIX[nsfx])
		print(answer)
		return minumero
	else:
		nsfx += 1
		try:
			lastnum = minumero[-3:][0]
		except:
			lastnum = 0
		minumero = minumero[:-3]
		return humanSize(minumero,nsfx,lastnum)

minumero = input("Enter a no negative number : ") 
humanSize(minumero,nsfx = 0,last=0)



