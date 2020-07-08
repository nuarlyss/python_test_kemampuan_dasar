#konversi mata uang usd2eur

dmatauang2idr = {'IDR': 1, 'USD': 14425, 'EUR': 16225}
 
def usd2eur(usd):
  
  USD = dmatauang2idr['USD'] * usd
  
  EUR = USD / dmatauang2idr['EUR'] 
  value = EUR
  return value
 
print(usd2eur(1000))
