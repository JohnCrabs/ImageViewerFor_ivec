import pickle
import lib.core.ivec as ivec

# Load Data
data_path = 'data/breast_cancer_example.pkl'
data_file = open(data_path, 'rb')
x, y = pickle.load(data_file)

# Create IVEC Metadata
name = 'breast_cancer_positive'
x_dim = 1
if x.shape.__len__() >= 3:
    x_dim = x.shape[2]
    mul_x_dim = True

y_dim = 1
if y.shape.__len__() >= 3:
    y_dim = y.shape[2]

width = x.shape[1]
height = x.shape[0]

# Create IVEC
my_ivec = ivec.IVEC()

my_ivec.setMetadata(
    name=name,
    x_dim=x_dim,
    y_dim=y_dim,
    width=width,
    height=height,
    x_mode=ivec.KEY_IMG_MODE_GRAYSCALE,
    y_mode=ivec.KEY_IMG_MODE_GRAYSCALE)

if x_dim > 1:
    for i in range(0, x_dim):
        my_ivec.addData_X(x[:, :, i])
else:
    my_ivec.addData_X(x)

if y_dim > 1:
    for i in range(0, y_dim):
        my_ivec.addData_Y(y[:, :, i])
else:
    my_ivec.addData_Y(y)

# Data export
exportDirPath = 'data/'
my_ivec.save_ivec(exportDirPath)

# Data import
importFilePath = 'data/breast_cancer.ivec'
my_new_ivec = ivec.IVEC()
my_new_ivec.load_ivec(importFilePath)
my_new_ivec.print_ivec()
