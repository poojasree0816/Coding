from datetime import datetime
dt1="2019-01-01 09:45:56"
#dt1=input()
dt1arr=dt1.split(" ")
dt1date=dt1arr[0].split("-")
dt1time=dt1arr[1].split(":")
dt2="2019-01-01 15:45:56"
#dt2=input()
dt2arr=dt2.split(" ")
dt2date=dt2arr[0].split("-")
dt2time=dt2arr[1].split(":")
d1 = datetime(int(dt1date[0]), int(dt1date[1]), int(dt1date[2]), int(dt1time[0]), int(dt1time[1]), int(dt1time[2]))  
d2 = datetime(int(dt2date[0]), int(dt2date[1]), int(dt2date[2]), int(dt2time[0]), int(dt2time[1]), int(dt2time[2]))
duration = d1 - d2 
duration_in_s = int(duration.total_seconds())
durationhours=duration_in_s//3600
duration_in_s=duration_in_s- (durationhours*3600)
durationmins=duration_in_s//60
duration_in_s=duration_in_s-(durationmins*60)
if(durationhours < 10):
    if(durationhours<0):
        durationhours=0-durationhours
    durationhours=str("0")+str(durationhours)
if(durationmins < 10):
    if(durationmins<0):
        durationmins=0-durationmins
    durationmins=str(0)+str(durationmins)
if(duration_in_s < 10):
    if(duration_in_s<0):
        duration_in_s=0-duration_in_s
    duration_in_s=str(0)+str(duration_in_s)
colon=":"
ans=str(durationhours)+colon+str(durationmins)+colon+str(duration_in_s)
print(ans)
