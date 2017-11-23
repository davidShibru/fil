'''
d = int(input('chis'))
i = d
while (d != (i*(-1))):
  try:
    m = d/i
  except ZeroDivisionError:
    print ('0')
  finally:
    print (m)
    i = i -1
'''

def delenie(des):
  d = des
  i = d
  while (d != (i*(-1))):
    try:
      m = d/i
      print (m)
    except ZeroDivisionError:
      print ('0')
    finally:
      i = i -1
delenie(int(input('chis')))