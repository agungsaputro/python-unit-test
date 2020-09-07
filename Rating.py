
def rating_film(n):
    if n == int:
        raise TypeError
    if n >= 21:
        return ("DEWASA")
    elif 13 <= n < 21:
        return ("REMAJA")
    elif 9 <= n < 13:
        return ("BIMBINGAN ORANG TUA")
    elif n < 9:
        return ("SEMUA UMUR")

print(rating_film(12))
    