#write.table
data
#by default r will give row name so set row name as false
write.table(data,file = "Exporteddata.csv",sep = ",",row.names = FALSE)
#to save in a specific loc we have to give path in file
write.table(data,file = "C:\\Users\\viswa\\OneDrive\\Desktop\\Exporteddata.txt",sep = "\t",row.names = FALSE)
write.table(data,
            file = "C:\\Users\\viswa\\OneDrive\\Desktop\\Exporteddata1.txt",
            sep = " ",row.names = FALSE)
#it will return no. of rows and col
dim(data)

#to get the names of the col
names(data)

#to cal mean 
mean(data$Year)

data$Year

#after attach statement we can only work on the data entered in attach cmd
attach(data)
data
mean(Plan)
Plan
#this cmd helps to detach the data
detach(data)

names(data)
attach(data)
class(Post)
class(Pre)
class(Years)

levels(Years)
levels(JobSat)
levels(Plan)
levels(Gender)

summary(data)


x<- c(0,1,0,1,0,1,1,1,1,0)

class(x)
summary(x)
x<- as.factor(x)
class(x)
summary(x)