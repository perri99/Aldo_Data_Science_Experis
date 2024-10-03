import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image

# Define the CNN architecture
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 7 * 7, 512)
        self.fc2 = nn.Linear(512, 10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# Le classi del dataset FashionMNIST
classes = ('T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot')


# Load the saved model
model = CNN()
model.load_state_dict(torch.load('03-10/cnn_fashionMNIST.pth'))
model.eval()

# Preprocess the custom image
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, ), (0.5, ))
    ])
    
    img = Image.open(image_path).convert('L')
    img = transform(img)
    img = img.unsqueeze(0)
    
    return img

# Make predictions
def predict_image(model, image_path):
    img = preprocess_image(image_path)
    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs, 1)
    predicted_class = classes[predicted[0]]
    print(f'Predicted Class: {predicted_class}')
    return predicted_class

# Example usage: Upload and predict a custom image
image_path = '03-10/shirt.jpeg'
predict_image(model, image_path)

def predict_confidence(model, image_path):
    img = preprocess_image(image_path)
    with torch.no_grad():
        outputs = model(img)
        probabilities = torch.softmax(outputs, dim=1)
        return {classes[i]: float(probabilities[0][i]) * 100 for i in range(len(classes))}

print(predict_confidence(model, image_path))
