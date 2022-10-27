a = 2
b = 3

detik = (1000*a)+(100*b)-(10*a)
jam = detik//3600
mnt = (detik%3600)//60
dtk = ((detik%3600)%60)
print (jam,"jam",mnt,"menit",dtk,"detik")