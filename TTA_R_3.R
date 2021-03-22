library(ggplot2)
library(readxl)
library(ggalt)
library(remotes)

data <- read_excel("cost_curve_data.xlsx", sheet = "costdata")

p1 <- ggplot(data, aes(y=central, x=date, colour=product, fill=product)) + 
  geom_xspline(size=0.8) + 
  geom_ribbon(aes(ymin=low, ymax=high), alpha=0.2, show.legend = FALSE, colour = NA) +
  theme_light() + 
  scale_y_continuous("Price (£ / kg)", limits = c(0,NA), expand = c(0,0),
                     sec.axis = sec_axis(~ . * 25.37710376, name = "Price (£/ MWh)")) +
  scale_colour_manual(values = c("Product 2"="blue", "Product 3"="red", "Product 1"="green")) +
  scale_fill_manual(values = c("Product 2"="blue", "Product 3"="red", "Product 1"="green")) + 
  scale_x_continuous(expand = c(0,0)) + 
  ggtitle("Cost curves")

ggsave(file="plot_test.png",plot=p1, width = 297, height = 210, units = "mm")
dev.off()
