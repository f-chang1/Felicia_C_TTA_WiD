# task 1
a<-c(8,3,12,9,5)
b<-c(13,7,11,2,10)
c<-c(15,6,1,14,4)

d<-cbind(a,b,c)
plot(d[,'a'],d[,'c'],main="Plot of c against a", xlab="a", ylab="c")

# task 2
df <- data.frame(name = c("Paulina","Yuko","Elazar", "Aniruddha", "Beatrice"),
                 age = c(23, 41, 32, 21, 60),
                 gender = c("female","female","male","male","female"),
                 role = c("Data scientist","Data analyst","Data engineer","Secretary","CEO"),
                 length_of_service = c(2,12,4,1,20)
)
print (df)

# task 3
library("ggplot2")
x<-1:20
y<-x^2
qplot(x,y, main = "x^2 graph",
      ylab = "x^2")

# task 4
p <-ggplot(data=df, aes(x=name , y=length_of_service)) +
  geom_bar(stat="identity") + 
  ggtitle("Employees' length of service") +
  xlab("Employee") + ylab("Length of service")
p


