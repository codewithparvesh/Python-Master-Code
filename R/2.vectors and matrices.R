x = 11
x <- 12


#the below is vector
x1 <- c(1,3,4,5,6,6,7,3)
#string vector
gender <- c("Male","Female")
#by default it will append in 1
2:6


#seq()sequence 
seq(from = 1 , to = 23, by = 7)
seq(from = 1 , to = 23, by = 1/4)
seq(from = 1 , to = 23, by = 0.25)


#rep()repetition of num the below will return 1 - 12 times
rep(1, times = 12)
rep("marin", times = 5)
rep(1:3 , time = 5)
rep(seq(from = 1 , to = 4,by = 1), times = 3)
rep(c("m","f"), times = 3)


#assigning vect
x <- 1:3
y<-c(12,12,23,21,32,14)
# we do arth ops in the vector
x+10
# i/p 1:3
# o/p [1] 11 12 13
#if two vector are of the same length we may add/sub/mul/div
#corresponding elements


#+to extract the elements
x[3]
#it will extract the third element of the x vector
x[c(1,2)]
#it will extract the one to two element of the x vector
x[x<2]
#it will extract the numbers less than 2 present in x vector

# matrix
mat <- matrix(c(1,3,3,45,45,454,43,2,3),nrow = 3,byrow = TRUE)
#row vise entry 
mat1 <- matrix(c(1,3,3,45,45,454,43,2,3),nrow = 3,byrow = FALSE)
#col vise entry
#to extract the elements from matrix
#name[row,col]
mat
mat[1,2]
#name[c(row1,row3),col2]
mat[c(2,3),c(2,3)]
#name[c(row1,row3),c(col2,col3)]
mat[2,]
#name[row,] will return the row
mat[,2]
#name[row,] will return the col
mat1 * mat
#if two matrix are of the same length we may add/sub/mul/div
#corresponding elements
mat*10
#we can also justadd/sub/mul/div the mat with any numeric value


# to checck the class of matrix
mode(mat)

#to create a diagonal matrix or identity matrix
mat3 <- diag(1,nrow =3,ncol = 3)
mat3

#transpose
mat1
t(mat1)

#creating data frame
df10 <- data.frame("ID" = 1:3,"Name"= c("Viswa","Nitin","Dinesh"),"Age" = c(21,21,19))
df10
df10["Name"]
head(df10,n=2)

#modifying the row
df10[2,"Age"] <- 20;df10

#adding rows
df11<-rbind(df10,list(4,"Sahil",23))
df11
#adding columns
cbind(df11,State = c("TN","UP","TN","HP"))
