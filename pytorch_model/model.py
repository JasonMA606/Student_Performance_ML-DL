# torch imports
import torch.nn.functional as F
import torch.nn as nn


# TODO: Complete this classifier
class BinaryClassifier(nn.Module):
    """
    Define a neural network that performs binary classification.
    The network should accept your number of features as input, and produce 
    a single sigmoid value, that can be rounded to a label: 0 or 1, as output.

    Notes on training:
    To train a binary classifier in PyTorch, use BCELoss.
    BCELoss is binary cross entropy loss, documentation: https://pytorch.org/docs/stable/nn.html#torch.nn.BCELoss
    """

    def __init__(self, input_features, hidden_dim, output_dim):
        """
        Initialize the model by setting up linear layers.
        Use the input parameters to help define the layers of your model.
        :param input_features: the number of input features in your training/test data
        :param hidden_dim: helps define the number of nodes in the hidden layer(s)
        :param output_dim: the number of outputs you want to produce
        """
        super(BinaryClassifier, self).__init__()

        # define any initial layers, here
        hidden1 = hidden_dim
        hidden2 = hidden_dim
        hidden3 = hidden_dim
        self.fc1 = nn.Linear(input_features, hidden1)
        self.fc2 = nn.Linear(hidden1, hidden2)
        self.fc3 = nn.Linear(hidden2, hidden3)
        self.fc4 = nn.Linear(hidden3, output_dim)
        self.Dropout = nn.Dropout(0.1)
        self.sig = nn.Sigmoid()

    def forward(self, x):
        """
        Perform a forward pass of our model on input features, x.
        :param x: A batch of input features of size (batch_size, input_features)
        :return: A single, sigmoid-activated value as output
        """
        # define the feedforward behavior
        out = F.relu(self.fc1(x))
        out = self.Dropout(out)
        out = F.relu(self.fc2(out))
        out = self.Dropout(out)
        out = F.relu(self.fc3(out))
        out = self.Dropout(out)
        out = self.fc4(out)
        return self.sig(out)
