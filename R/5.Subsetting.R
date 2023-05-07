data

#to know about the col and row
dim(data)

#to know the no. of rows(we have to specify the col)
length(Years)
#to know the no. of col(we have to specify the table name)
length(data)

#calling the rows of specific col
Years[7:10]
#calling the rows and cols of specific data
data[7:10, ]
#cal mean salary of specific gender 
mean(Salary[Gender == "M"])
mean(Salary[Gender == "W"])
levels(Gender)

#subsetting data according to male and female

male <- data[Gender == "M",]
Female <- data[Gender == "W",]
dim(male)
dim(Female)
summary(Gender)

Malesales <- data[Gender == "M" & Salary>60000,]
Malesales

Malesales[1:4,]

mtcars

mtcars_small <- mtcars[1:10,]
mtcars_small

mtcars_small[which(mtcars_small$am == 0),]

mtcars_small[which(mtcars_small$gear>3),]

subset(mtcars,am == 0,select = c('hp','cyl'))

#dplyr

library(dplyr)

select(mtcars, cyl,hp)
filter(mtcars,am == 0)

library(sqldf)

sqldf("select cyl from mtcars_small")

