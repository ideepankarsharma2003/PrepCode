# library(palmerpenguins)
# summary(penguins)
# View(penguins)




# # library(ggplot2)


library(tidyverse)
library(Tmisc)
data(quartet)
# Anscombe's quartet ---> Four datasets that have nearly identical summary statistics

quartet %>%
    group_by(set) %>%
    summarise(mean = mean(x), sd(x), mean(y), sd(y), cor(x, y))


ggplot(quartet, aes(x, y)) +
    geom_point() +
    geom_smooth(method = lm, se = FALSE) +
    facet_wrap(~set)
