import random
import matplotlib.pyplot as plt

coin_outcomes=["heads","tails"]
def flipping(n):
  i=0
  j=0
  for _ in range(n):
    if str(random.choice(coin_outcomes))=="heads":i+=1
    else:j+=1
  return i,j

#def plotting(x,y):
  #plt.hlines(0.5,min(x),max(x))
  #plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
  #plt.ylim(0,1) 
  #plt.xlim(min(x),max(x))
  #plt.show()

head=0
flips=0
Hx,Hy=[],[]
while(True):
  print("Enter Number of Coin flips:")
  n=int(input())
  if n==0:break
  i,j=flipping(n)
  head+=i
  flips+=n
  head_value=head/flips
  Hx.append(flips)
  Hy.append(head_value)
  #plotting(Hx,Hy)
  print(head_value)