modelName <- "linearRegression"
InputDataFileName="dataset.data"
training = 40

dataset <- read.csv(InputDataFileName)      
dataset <- dataset[sample(nrow(dataset)),]
totalDataset <- nrow(dataset)

target  <- names(dataset)[21]
inputs <- setdiff(names(dataset),target)

trainDataset <- dataset[1:(totalDataset * training/100),c(inputs, target)]
testDataset <- dataset[(totalDataset * training/100):totalDataset,c(inputs, target)]

formula <- as.formula(paste(target, "~", paste(c(inputs), collapse = "+")))
model   <- lm(formula, trainDataset)

Predicted <- predict(model, testDataset)
Actual <- as.double(unlist(testDataset[target]))

r <- cor(Actual,Predicted )
r <- round(r,2)

rms <- mean((Actual-Predicted)^2)
rms <- sqrt(rms)
rms <- round(rms,2)

acceptablepriceerror = 2500

accuracy <- mean(abs(Actual-Predicted) <=acceptablepriceerror)
accuracy <- round(accuracy,4) *100

png(filename=paste(modelName,"-ScatterPlot.png",sep=''))
plot(Actual,Predicted,main=paste("Actual Vs Predicted\n",modelName),xlab="Predicted", ylab="Actual")
abline(lm(Actual ~ Predicted),col="Blue")
dev.off()

result <- data.frame(modelName,r,R,rms,accuracy, totalTime)[1:1,]

write.csv(result, file=paste(modelName,"-Evaluation-Result.csv",sep=''), row.names=FALSE)
write.csv(data.frame(Actual,Predicted), file=paste(modelName,"-ActualPredicted-Result.csv",sep=''), row.names=FALSE)

save.image(file=paste(modelName,"-Model.RData",sep=''))