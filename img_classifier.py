import %matplotlib inline
%config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt
import torch
from torch import nn
import torch.nn.functional as F
from torchvision import datasets,transforms,models
from torch import optim
from PIL import Image
import numpy as np
import seaborn as sns