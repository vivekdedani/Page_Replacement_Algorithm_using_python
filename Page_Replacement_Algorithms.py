#!/usr/bin/env python
# coding: utf-8

# In[5]:


def fifo(pagestring,msize):
 mptr,hit,Faults = 0,0,0
 memory = [-1 for i in range(msize)]
 for i in pagestring:
  flag = 0
  for j in memory:
   if j==int(i):
    hit += 1
    flag = 1
    break
  if(flag==0):
   Faults += 1
   memory[mptr] = int(i)
   mptr += 1
   if(mptr==msize):
    mptr=0
  print(memory)
 print("Hits=",hit," Faults=",Faults)


# In[6]:


def lru(pagestring,msize):
 mptr,hit,Faults = 0,0,0
 memory = [-1 for i in range(msize)]
 for i in range(len(pagestring)):
  flag = 0
  for j in memory:
   if j==int(pagestring[i]):
    hit += 1
    flag = 1
    break
  if(flag==0):
   Faults += 1
   if(mptr >=msize):
    left = pagestring[0:i]
    dist = [-1 for i in range(10)]
    present = [-1 for i in range(10)]
    
    for j in range(len(left)):
     k = int(left[j])
     dist[k] = i-j
     for l in range(len(memory)):
      if memory[l]==int(left[j]):
       present[k] = l
       break
    max,num = 0,0
    for j in range(len(dist)):
     if(dist[j] > max and present[j] > -1):
      max = dist[j]
      num = present[j]
    memory[num] = int(pagestring[i])
   else:
    memory[mptr] = int(pagestring[i])
    mptr += 1
  print(memory)
 print("Hits=",hit," Faults=",Faults)


# In[8]:


def optimal(pagestring, msize):
    mptr, hit, Faults = 0, 0, 0
    memory = [-1 for i in range(msize)]
    for i in range(len(pagestring)):
        flag = 0
        for j in memory:
            if j == int(pagestring[i]):
                hit += 1
                flag = 1
                break
        if flag == 0:
            Faults += 1
            if mptr >= msize:
                dist = [-1 for i in range(10)]
                present = [-1 for i in range(10)]
                for j in range(len(memory)):
                    for k in range(i+1, len(pagestring)):
                        if memory[j] == int(pagestring[k]):
                            present[j] = k
                            break
                max_dist = -1
                replace_page_index = -1
                for j in range(len(memory)):
                    if present[j] == -1:
                        replace_page_index = j
                        break
                    if present[j] > max_dist:
                        max_dist = present[j]
                        replace_page_index = j
                if replace_page_index != -1:
                    memory[replace_page_index] = int(pagestring[i])
                else:
                    memory[0] = int(pagestring[i])
            else:
                memory[mptr] = int(pagestring[i])
                mptr += 1
        print(memory)
    print("Hits = ", hit, " Faults = ", Faults)


# In[9]:


def main():
    x = input("Enter the page string : ")
    m = int(input("Enter the size of memory : "))
    fifo(x,m)
    lru(x,m)
    optimal(x,m)

main()


# In[ ]:




