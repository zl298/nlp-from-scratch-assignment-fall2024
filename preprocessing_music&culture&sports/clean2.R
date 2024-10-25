
frickL <- readLines("/Users/zhihanli/Desktop/datasets for csv/frick_eventOnly.txt")
historyCenter <- readLines("/Users/zhihanli/Desktop/datasets for csv/historycenter_eventOnly.txt")
museumsL <- readLines("/Users/zhihanli/Desktop/datasets for csv/musumes_eventonly.txt")
#Remove the blank
frickL <- frickL[frickL != "" & !grepl("^\\s*$", frickL)]
historyCenter <- historyCenter[historyCenter != "" & !grepl("^\\s*$", historyCenter)]
museumsL <- museumsL[museumsL != "" & !grepl("^\\s*$", museumsL)]

frick <- data.frame(frickL, stringsAsFactors = FALSE)
hC <- data.frame(historyCenter, stringsAsFactors = FALSE)
ms <- data.frame(museumsL, stringsAsFactors = FALSE)
#start frick==================================
eventName<-c()
eventDate<-c()
exactTime<-c()
Intro<-c()

for (i in 1:nrow(frick)){
  if ((i+3)%%4 == 0){
    eventName <-c(eventName,frick[i,1])
    eventDate <-c(eventDate,frick[i+1,1])
    exactTime <-c(exactTime,frick[i+2,1])
    Intro <-c(Intro,frick[i+3,1])
  }
}
organized_frick <- data.frame(Date = eventDate, Event = eventName, Time = exactTime, Introduction = Intro, stringsAsFactors = FALSE)
write.csv(organized_frick, "frickEvent.csv", row.names = FALSE)

#start hC==================================
eventName<-c()
eventDate<-c()
exactTime<-c()
Intro<-c()

for (i in 1:nrow(hC)){
  if ((i+3)%%4 == 0){
    eventDate <-c(eventDate,hC[i,1])
    exactTime <-c(exactTime,hC[i+1,1])
    eventName <-c(eventName,hC[i+2,1])
    Intro <-c(Intro,hC[i+3,1])
  }
}
organized_hC<- data.frame(Date = eventDate, Event = eventName, DetailedInfo = exactTime, Introduction = Intro, stringsAsFactors = FALSE)
write.csv(organized_hC, "hCEvent.csv", row.names = FALSE)

#start ms==================================
eventName<-c()
eventDate<-c()
whichmuseums<-c()
typeofActivity<-c()

for (i in 1:nrow(ms)){
  if ((i+3)%%4 == 0){
    eventDate <-c(eventDate,ms[i,1])
    eventName <-c(eventName,ms[i+1,1])
    if(ms[i+2,1]=="Science Center"){
      whichmuseums <-c(whichmuseums,"Carnegie Science Center")
    }else{
      whichmuseums <-c(whichmuseums,ms[i+2,1])
    }
    typeofActivity <-c(typeofActivity,ms[i+3,1])
  }
}
organized_ms<- data.frame(Date = eventDate, Event = eventName, museumName = whichmuseums, ActivityType = typeofActivity, stringsAsFactors = FALSE)
write.csv(organized_ms, "msEvent.csv", row.names = FALSE)

