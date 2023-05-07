#how to import csv or txt in r

#to know about the func
help(read.csv)
?read.csv


#importing data


#read.csv
#file.choose will help you directly select the file in file manager
data<- read.csv(file.choose(),header = TRUE)
#to assume first row as data not as colname we have to keep header as false
data1<- read.csv(file.choose(),header = FALSE)
data
data1


#read.table
#sep is to represent comma sep file
#to import as the csv files
data2<- read.table(file.choose(),header = T, sep=",")
data2

#sep is to represent tan sep file
#to import as the txt files
data2<- read.table(file.choose(),header = T, sep="\t")
data2

#read.delim()
#to import as the txt files
data3<- read.delim(file.choose(),header = T)
data3

#how to import excel file
#we can import data from environment or the below is the option
library(readxl)
df_gss <- read_excel("C:/Users/viswa/Downloads/GLOBAL SUPER STORE 2016 SALES.xlsx", 
                                            sheet = "Orders", 
                                            col_types = c("numeric", "text", "numeric", "numeric", "skip", 
                                                          "text", "text", "text", "numeric","text", "text", 
                                                          "text", "text", "text","text", "text", "text", 
                                                          "text", "numeric", "numeric", "numeric", "numeric", 
                                                          "numeric", "text"), na = "NA", n_max = 10)
df_gss
