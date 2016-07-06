df = read.csv("baseball_data.csv", header = TRUE, fill = TRUE)
filtered_df <- subset(df, avg > 0)

height_bins <- cut(filtered_df$height, 8, include.lowest=TRUE, labels=c("65-66", "67-68", 
                                                                        "69-70", "71-72",
                                                                        "73-74", "75-76", 
                                                                        "77-78", "79-80"))
filtered_df$height_bin <- height_bins

height_data <- aggregate(filtered_df$HR, by=list(height=filtered_df$height_bin), FUN=mean)

weight_bins <- cut(filtered_df$weight, 9, include.lowest = TRUE, labels=c("140-149", "150-159",
                                                                           "160-169", "170-179",
                                                                           "180-189", "190-199",
                                                                           "200-209", "210-219",
                                                                           "220-230"))
filtered_df$weight_bin <- weight_bins

weight_data <- aggregate(filtered_df$HR, by=list(height=filtered_df$weight_bin), FUN=mean)
