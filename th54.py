import datetime as dt
format='%Y-%m-%dT%H:%M:%S'
t1=dt.datetime.strptime('2008-10-12T14:45:52',format)
print('Ngay' +str(t1.day))
print('Than' +str(t1.month))
print('Giay' +str(t1.minute))
print('Phut' +str(t1.second))

#define todays date and time
t2=dt.datetime.now()
diff=t2-t1
print('chenh lech bao nhieu ngay? '+str(diff.days))
      
      
