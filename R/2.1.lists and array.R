df12<- list("Viswa","sasd","asd",TRUE,21,23L)
df12
names(df12)<- c("name","name","name","bool","dbl","Int")
df12
df13 <- list(df12)
df12$name
a3 = list(df12,df13)
a3

df12[1] <- "pal"
df12

# to add the element in the list
append(df12,"YT")

#to remove the element
df12[-1]
df12

length(df12)

#in operator
"pal" %in% df12

#array
u1 <- c(5,10,15,20)
u2 <- seq(25,60, by = 5)
u2
m1 = array (c(u1,u2),dim = c(4,4,3))
m1

z1 <- c(9,18)
z2 <- c(27,36)
r.nam <- c("a","b","c")
c.nam <- c("x","y")
m.nam <- c("ar1","ar2")

h <- array(c(z1,z2),dim = c (2,3,2), dimnames = list(c.nam,r.nam,m.nam))
h

h[1,2,1]
h[1,3,1]
h[1:2,1:2,1]

#factors in r
x <- factor(c("single","married","single","single"),levels = c("single","married","divoreced"))

levels(x)
x[3]

levels(x) <- c(levels(x),"not sure")
x[3]<-"not sure"
x[4] <- "divoreced"
x
