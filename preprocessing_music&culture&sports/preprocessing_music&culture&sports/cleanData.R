#dealing with the cultureCrust and symphony first

cultureCrust <- readLines("/Users/zhihanli/Desktop/datasets for csv/cultureCrust_Final.txt")
symphony <- readLines("/Users/zhihanli/Desktop/datasets for csv/symphony_final.txt")
cC <- data.frame(cultureCrust, stringsAsFactors = FALSE)
s <- data.frame(symphony, stringsAsFactors = FALSE)

record_date <-c()
eventDate <- c()
eventName <-c()
exactTime <-c()
Location <-c()

indexOfDate <-c()
countDate <- 0 #number of date

for (i in 1:nrow(cC)){
  line <- cC[i, 1]
  if (grepl("^\\w{3},\\s\\w{3}\\s\\d{1,2},\\s\\d{4}$", line)) {
    record_date <- c(record_date, line)  # Update the date
    countDate <- countDate+1
    
  }else if ((i-countDate+2)%%3 == 0){
    eventDate <-c(eventDate,record_date[countDate])
    eventName <-c(eventName,cC[i,1])
    exactTime <-c(exactTime,cC[i+1,1])
    Location <-c(Location,cC[i+2,1])
  }
}
organized_CultureC <- data.frame(Date = eventDate, Event = eventName, Time = exactTime, Location = Location, stringsAsFactors = FALSE)



record_date <-c()
eventDate <- c()
eventName <-c()
exactTime <-c()
Location <-c()

indexOfDate <-c()
countDate <- 0 #number of date

for (i in 1:nrow(s)){
  line <- s[i, 1]
  if (grepl("^\\w{3},\\s\\w{3}\\s\\d{1,2},\\s\\d{4}$", line)) {
    record_date <- c(record_date, line)  # Update the date
    countDate <- countDate+1
    
  }else if ((i-countDate+2)%%3 == 0){
    eventDate <-c(eventDate,record_date[countDate])
    eventName <-c(eventName,s[i,1])
    exactTime <-c(exactTime,s[i+1,1])
    Location <-c(Location,s[i+2,1])
  }
}
organized_symphony <- data.frame(Date = eventDate, Event = eventName, Time = exactTime, Location = Location, stringsAsFactors = FALSE)
write.csv(organized_CultureC, "CultureCEvent.csv", row.names = FALSE)
write.csv(organized_symphony, "symphonyEvent.csv", row.names = FALSE)


#dealing with the opera

operaL <- readLines("/Users/zhihanli/Desktop/datasets for csv/opera_Final.txt")
operaL <- operaL[operaL != "" & !grepl("^\\s*$", operaL)]
opera <- data.frame(operaL, stringsAsFactors = FALSE)

eventName<-c()
eventDate<-c()
exactTime<-c()
Location<-c()

for (i in 1:nrow(opera)){
  if ((i+3)%%4 == 0){
    eventName <-c(eventName,opera[i,1])
    eventDate <-c(eventDate,opera[i+1,1])
    exactTime <-c(exactTime,opera[i+2,1])
    Location <-c(Location,opera[i+3,1])
  }
}
organized_opera <- data.frame(Date = eventDate, Event = eventName, Time = exactTime, Location = Location, stringsAsFactors = FALSE)
write.csv(organized_opera, "operaEvent.csv", row.names = FALSE)

