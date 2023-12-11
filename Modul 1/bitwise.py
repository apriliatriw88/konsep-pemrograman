a=9
b=5
c= a | b
print('\n=========OR========')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))
print('_____________________________ (|)')
print('nilai :',c,' ,binary :',format(c,'08b'))
c= a & b
print('\n=========AND========')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))
print('_____________________________ (&)')
print('nilai :',c,' ,binary :',format(c,'08b'))
c = a ^ b
print('\n=========XOR========')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))
print('_____________________________ (^)')
print('nilai :',c,' ,binary :',format(c,'08b'))
c = ~a
print('\n=========NOT========')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))
print('_____________________________ (~)')
print('nilai :',c,' ,binary :',format(c,'08b'))
c = a >> 1
print('\n=========>>========')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))
print('_____________________________ (>>)')
print('nilai :',c,' ,binary :',format(c,'08b'))
c= a << 1
print('\n=========<<========')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))
print('_____________________________ (<<)')
print('nilai :',c,' ,binary :',format(c,'08b'))