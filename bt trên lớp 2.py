while True:
      value = input('nhap so nguyen tư 0 den 100: ')
      try:
          value = int(value)
      except ValueError:
          print('nhap so, please')
          continue
      if 0 <= value <=100:
          break
      else:
          print('valid range, please: 0-100')


