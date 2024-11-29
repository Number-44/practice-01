import random as r
ml= ["a", "d", "s", "g", 3, 2, "z"]
print(type(ml),ml[3],)
if "s" in ml:
    print ("that is true !")
[print(l) for l in ml]

#####################################################################

klo=["master","hex","readily"]
print([ml[-1]])
klo.pop(2)
klo.remove("master")
print(klo)


#####################################################################


for i in ml:
    print(i)
for p in range(len(ml)):
    print(ml[p])


#####################################################################


ol=0
while ol<len(ml):
    print(f" the while loop : {ol} : {ml[ol]}")
    ol+=1


#####################################################################

[print(h) for h in klo]
lin=0
while lin<5:
    print(f"lin is : {lin}")
    lin+=1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []


#####################################################################


for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)



#####################################################################


[print(b) for b in fruits if b != "kiwi"]



#####################################################################


myTuple=(1,2,3,4,5,6,7,8,9)
print(myTuple[0:4],f" the length of the tuple is : {len(myTuple)}")


#####################################################################


def x(art):
   print(f"the art is : {art}")


x(" movie !")
x("love you programming : python !")
piano=("tuple",)
print(type(piano))

print(myTuple[-4:])

mlist=list(myTuple)
print(type(mlist))
mlist.insert(0,11)
print(mlist)

myTuple=tuple(mlist)
print(type(myTuple))


y=(11,)
myTuple +=y
print(myTuple)


#####################################################################


num01=int(len(myTuple))
num01 +=1

for z in range(0,num01):
   myTuple01=tuple()
   myTuple01 += myTuple
   print(myTuple01[0:z])


#####################################################################

(one,two,*three,four,five)=myTuple01
print(f"this is three : {three}")
print(four)
print(five)



#####################################################################
for j in myTuple01:
   print(f" this is a for loop and the j is {j}")

[print(f" this is {j}")for j in myTuple01]

jack = 0
while jack < len(myTuple01):
   print(myTuple01[jack])
   jack+=1


#####################################################################


thisSet={1,2,3,4,5,6,7,8,9,18}
print(thisSet)
print(type(thisSet))

thisSet01={1,11,2,22,3,33,4,44,5,55}

koper=thisSet.intersection(thisSet01)
print(koper)

evila=thisSet.difference(thisSet01)
print(evila)

dnkn=thisSet.symmetric_difference(thisSet01)
print(dnkn)
   
