import matplotlib.pyplot as plt

# 训练和验证的损失和准确率数据
epochs = range(10)
train_loss = [0.459, 0.263, 0.218, 0.186, 0.177, 0.178, 0.173, 0.153, 0.156, 0.167]
valid_loss = [0.301, 0.200, 0.191, 0.209, 0.148, 0.178, 0.220, 0.211, 0.232, 0.197]
train_acc = [0.832, 0.909, 0.925, 0.931, 0.942, 0.936, 0.938, 0.949, 0.941, 0.944]
valid_acc = [0.895, 0.938, 0.940, 0.933, 0.955, 0.944, 0.944, 0.944, 0.930, 0.934]

# 绘制训练和验证损失曲线
plt.figure(figsize=(10, 5))
plt.plot(epochs, train_loss, label='Train Loss', marker='o')
plt.plot(epochs, valid_loss, label='Validation Loss', marker='o')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()

# 绘制训练和验证准确率曲线
plt.figure(figsize=(10, 5))
plt.plot(epochs, train_acc, label='Train Accuracy', marker='o')
plt.plot(epochs, valid_acc, label='Validation Accuracy', marker='o')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()