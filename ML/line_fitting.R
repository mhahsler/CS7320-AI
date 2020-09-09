#' # Line fitting
#'
#' Model function $h_w(x) = w_1 x + w_0$ calculates $\hat{y}$
y_hat <- function(x, w0, w1) w1 * x + w0

#' Used loss function $L(h_w) = \sum_{j=2}^N (y_j - h_w(x_j))$
L2 <- function(y, y_hat) sum((y - y_hat)^2)

#' ## Simulate some data with noise
N <- 100
real_w0 <- 3
real_w1 <- 7

x <- runif(N, 0, 1)
y <-  y_hat(x, real_w0, real_w1) + rnorm(N, sd = 1)

xy <- data.frame(x, y)
head(xy)

plot(xy)
abline(a = real_w0, b = real_w1, col = "green")

#' ## Visualize the loss function
#' 
#' Create a grid of w0 and w1 values
resolution <- 25
grid <- data.frame(
  w0 = rep(seq(0, 10, length.out = resolution), times = resolution),
  w1 = rep(seq(0, 10, length.out = resolution), each = resolution)
)

grid$L2 <- with(xy, 
  apply(grid, MARGIN = 1, FUN = function(w) 
    L2(y, y_hat(x, w["w0"], w["w1"]))
  )
)

#' Find minimum grid cell
opt <- grid[which.min(grid$L2), ]
opt

#' Plot loss function surface
pmat <- persp(matrix(grid$L2, nrow = resolution), 
  xlab = "w0", ylab = "w1", zlab = "loss")
points(
  trans3d(
    x = opt[,"w0"]/max(grid[,"w0"]), 
    y = opt[,"w1"]/max(grid[,"w1"]), 
    z = opt[,"L2"], 
    pmat = pmat), 
  col = "red", lwd = 2)

#' plot regression line
plot(xy)
abline(a = real_w0, b = real_w1, col = "green")
abline(a = opt[,"w0"], b = opt[,"w1"], col = "red")

#' ## Analytic solution
#'
#' Loss is minimized at:
#' 
#' $w_1 = \frac{N(\sum x_j y_j) - (\sum x_j)(\sum y_j)}{N(\sum x_j^2) - (\sum x_j)^2}$
#' 
#' $w_0 = \frac{\sum y_j - w_1 (\sum x_j)}{N}$

w1 <- with(xy, (N * sum(x*y) - sum(x)*sum(y)) / (N * sum(x^2) - sum(x)^2))
w1

w0 <- with(xy, (sum(y) - w1 * sum(x)) / N)
w0

plot(xy)
abline(a = real_w0, b = real_w1, col = "green")
abline(a = w0, b = w1, col = "red")

#' ## Gradient descent

#' ### Batch gradient descent

line_BGD <- function(xy, alpha = 0.001, eps = 1e-6) {
  
  #' start with some points from the parameter space
  w0 <- 0
  w1 <- 0
  
  # we use loss improvement > eps to check for convergence
  step <- 0
  improvement <- Inf
  loss <- L2(xy$y, y_hat(xy$x, w0, w1))
  
  history <- data.frame(w0, w1, loss)
  #' update weights
  while (improvement > eps) {
    old_loss <- loss
    step <- step + 1
    
    w0 <- with(xy, w0 + alpha * sum(y - y_hat(x, w0, w1)))
    w1 <- with(xy, w1 + alpha * sum((y - y_hat(x, w0, w1)) * x))
    
    loss <- L2(xy$y, y_hat(xy$x, w0, w1))
    improvement <- old_loss - loss
  
    history <- rbind(history, data.frame(w0, w1, loss))
  }
  list(w = c(w0 = w0, w1 = w1), history = history)
}

w <- line_BGD(xy) 
w$w

#' Learning curve
plot(w$history$loss, type = "l", xlab = "steps", ylab = "loss")

#' Learning path
pmat <- persp(matrix(grid$L2, nrow = resolution), 
  xlab = "w0", ylab = "w1", zlab = "loss")
lines(
  trans3d(
    x = w$history[,"w0"]/max(grid[,"w0"]), 
    y = w$history[,"w1"]/max(grid[,"w1"]), 
    z = w$history[,"loss"], 
    pmat = pmat), 
  col = "red", lwd = 2)


plot(xy)
abline(a = real_w0, b = real_w1, col = "green")
abline(a = w$w["w0"], b = w$w["w1"], col = "red")


#' ### SGD with minibatch
#' 
#'  Convergence is a problem since loss on all the data can increase.
#'  I use for convergence a number of tries with a loss improvement less than eps. I also reduce alpha over time using $\alpha/t^\delta$ for better convergence. 
line_SGD <- function(xy, alpha = 0.001, delta = 1e-6, eps = 1e-6, 
  tries = 10, batch_size = 10) {
  
  #' start with some points from the parameter space
  w0 <- 0
  w1 <- 0
  
  # we use loss improvement > eps to check for convergence
  step <- 0
  improvements <- 0
  loss <- L2(xy$y, y_hat(xy$x, w0, w1))
  
  history <- data.frame(w0, w1, loss)
  
  #' update weights
  while (improvements < tries) {
    old_loss <- loss
    step <- step + 1
    
    mb <- xy[sample(nrow(xy), size = batch_size),]
    w0 <- with(mb, w0 + alpha/step^delta * sum(y - y_hat(x, w0, w1)))
    w1 <- with(mb, w1 + alpha/step^delta * sum((y - y_hat(x, w0, w1)) * x))
    
    loss <- L2(xy$y, y_hat(xy$x, w0, w1))
    improvement <- old_loss - loss
    if(improvement < eps) improvements <- improvements + 1
    else improvements <- 0
    
    history <- rbind(history, data.frame(w0, w1, loss))
  }
  list(w = c(w0 = w0, w1 = w1), history = history)
}

w <- line_SGD(xy) 
w$w

#' Learning curve
plot(w$history$loss, type = "l", xlab = "steps", ylab = "loss")

#' Learning path
pmat <- persp(matrix(grid$L2, nrow = resolution), 
  xlab = "w0", ylab = "w1", zlab = "loss")
lines(
  trans3d(
    x = w$history[,"w0"]/max(grid[,"w0"]), 
    y = w$history[,"w1"]/max(grid[,"w1"]), 
    z = w$history[,"loss"], 
    pmat = pmat), 
  col = "red", lwd = 2)


plot(xy)
abline(a = real_w0, b = real_w1, col = "green")
abline(a = w$w["w0"], b = w$w["w1"], col = "red")
