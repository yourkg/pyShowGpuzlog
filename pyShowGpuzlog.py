#show GPU-Z log
#baseline v0.001
#modify yourkg 09.19.21


import matplotlib.pyplot as plt

def printImg():
    with open('GPU-Z Sensor Log.txt', 'r') as f:
        line_list=f.read().splitlines()

    x=[]
    k1=[]
    k2=[]
    k3=[]
    jj=0
    print(len(line_list))
    kk=len(line_list)-1000
    for line in line_list:
        if jj<=kk:
            jj+=1
            continue
        l = line.replace(' ','').split(',')
        x.append(jj)
        try:
            k1.append(float(l[3]))
        except:
            k1.append(k1[-1])
        try:
            k2.append(float(l[4]))
        except:
            k2.append(k2[-1])
        try:
            k3.append(float(l[5]))
        except:
            k3.append(k3[-1])
        jj+=1
        if jj-kk>=1000:
            break
    return x,k1,k2,k3
i=0
while i<1:
    x,k1,k2,k3=printImg()
    plt.plot(x,k1,'s-',color = 'r',markersize=0.1,label="GPU Temperature")
    plt.plot(x,k2,'o-',color = 'g',markersize=0.1,label="Hot Spot")
    plt.plot(x,k3,'*-',color = 'b',markersize=0.1,label="Memory Temperature")
    #plt.figure()
    plt.xlabel("t")
    plt.ylabel("℃")
    plt.legend(loc = "best")
    #plt.cla()
    plt.show()
    #plt.clf()
    i+=1
