data

Salary[1:5]

#returns true or false
temp <- Salary>60000
temp[1:5]

#0 1 returns
temp2 <- as.integer(Salary>60000)
temp2

#making diff data where gender is w and job is high 
femjobsat <- Gender == "W" & JobSat == "high"
femjobsat[1:5]

#cbind - to add col
datamore <- cbind(data,femjobsat)
datamore

#remove all data from evnvi
rm(list = ls())
