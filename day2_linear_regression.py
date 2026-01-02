#dummy data to make model learn - x(random numbers data) y(the true numbers)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

#initialized w on 0 and w is The thing we adjust to reduce loss

w = 0

# The predict function uses x and w to guess what y should be.

def predict(x, w):
    return x * w

# The loss function measures how far the prediction is from the real answer.

def loss(y_true, y_pred):
    return (y_true - y_pred) ** 2

# Evaluate tests how good a specific w is

def evaluate(w):
    print(f"\nEvaluating w = {w}")
    total_loss = 0

    for xi, yi in zip(x, y):
        y_pred = predict(xi, w)
        l = loss(yi, y_pred)
        total_loss += l
        print(f"x={xi}, y={yi}, y_pred={y_pred}, loss={l}")

    print(f"Total loss: {total_loss}")


evaluate(0) #loss  (Dependig on the evaluating number the loss was decreasing massively)
evaluate(0.5) #loss
evaluate(1) #loss
evaluate(2) #perfect
evaluate(3) #loss
