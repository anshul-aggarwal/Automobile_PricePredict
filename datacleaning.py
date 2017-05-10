import random

attrib_list = ['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels','engine-location','wheel-base','length','width','height','curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']

make_list = ['alfa-romero','audi','bmw','chevrolet','dodge','honda','isuzu','jaguar','mazda','mercedes-benz','mercury','mitsubishi','nissan','peugot','plymouth','porsche','renault','saab','subaru','toyota','volkswagen','volvo']
fueltype_list = ['diesel','gas']
aspiration_list = ['std','turbo']
numofdoors_list = ['two','four']
bodystyle_list = ['hardtop','wagon','sedan','hatchback','convertible']
drivewheels_list = ['4wd','fwd','rwd']
enginelocation_list = ['front','rear']
enginetype_list = ['dohc','dohcv','l','ohc','ohcf','ohcv','rotor']
numofcylinders_list = {'eight' : 8,'five' : 5,'four' : 4,'six' : 6,'three' : 3,'twelve' : 12,'two' : 2}
fuelsystem_list = ['1bbl','2bbl','4bbl','idi','mfi','mpfi','spdi','spfi']

f = open("imports-85.data",'r').read()

rws = f.split("\n")
rows = [r for r in rws if r != '']

dataset = []

for row in rows:
    dt = row.split(',')
    dataset.append(dt)

#Removing missing values

cont_list = [1,18,19,21,22,25]
mean_list = [0,0,0,0,0,0]
m_id = 0

for i in cont_list:
    ctr = 0
    for dt in dataset:
        if dt[i] != '?':
            mean_list[m_id] = mean_list[m_id] + float(dt[i])
            ctr = ctr + 1
    mean_list[m_id] = round(mean_list[m_id]/ctr, 2)
    m_id = m_id + 1
    
    
m_id = 0
for i in cont_list:
    for dt in dataset:
        if dt[i] == '?':
            dt[i] = str(mean_list[m_id])
    m_id = m_id + 1
        
c_4d = 0
c_2d = 0
for dt in dataset:
    if dt[5] == 'two':
        c_2d = c_2d + 1
    elif dt[5] == 'four':
        c_4d = c_4d + 1
    
rep_cd = ''
if c_4d > c_2d:
    rep_cd = 'four'
else:
    rep_cd = 'two'
    
    
for dt in dataset:
    if dt[5] == '?':
        dt[5] = rep_cd
 

#Handling Nominal Values
    
for dt in dataset:
    for i in range(len(fueltype_list)):
        if dt[3] == fueltype_list[i]:
            dt[3] = str(i)
    
    for i in range(len(aspiration_list)):
        if dt[4] == aspiration_list[i]:
            dt[4] = str(i)
    
    for i in range(len(numofdoors_list)):
        if dt[5] == numofdoors_list[i]:
            dt[5] = str(i)
    
    for i in range(len(enginelocation_list)):
        if dt[8] == enginelocation_list[i]:
            dt[8] = str(i)
    

for dt in dataset:
    try:
        dt[15] = str(numofcylinders_list[dt[15]])
    except:
        print(dt[15])

removal_list = [2,6,7,14,17]

attrib_list = attrib_list + bodystyle_list + drivewheels_list + enginetype_list + fuelsystem_list

for dt in dataset:
    for bstyle in bodystyle_list:
        if dt[6] == bstyle:
            dt.append('1')
        else:
            dt.append('0')
    
    for dwr in drivewheels_list:
        if dt[7] == dwr:
            dt.append('1')
        else:
            dt.append('0')
    
    for etype in enginetype_list:
        if dt[14] == etype:
            dt.append('1')
        else:
            dt.append('0')
    
    for fst in fuelsystem_list:
        if dt[17] == fst:
            dt.append('1')
        else:
            dt.append('0')


ot = open("dataset.data", 'w')

for i in range(len(attrib_list)):
    if i not in removal_list:
        ot.write(attrib_list[i])
        if i != len(attrib_list) - 1:
            ot.write(",")

for dt in dataset:
    ot.write("\n")
    for i in range(len(attrib_list)):
        if i not in removal_list:
            ot.write(dt[i])
            if i != len(attrib_list) - 1:
                ot.write(",")

ot.close()













