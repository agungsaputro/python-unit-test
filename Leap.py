def kabisat(n):
    
    if n == int:
        raise TypeError

    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False

tahun = 2000

if kabisat(tahun):
	print ('Kabisat')
else:
	print ('Bukan Kabisat')