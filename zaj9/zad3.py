import pandas as pd
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


df = pd.read_csv('diabetes.csv', delimiter=',', encoding="utf-8-sig")
c1 = df.columns[0]
print(df.head())
rows, cols = df.shape
print(rows)
print(cols)
# b
label_names = df['class'].unique()
print(label_names)
index_and_label = list(enumerate(label_names))
print(index_and_label)

label_to_index = dict((label, index) for index, label in index_and_label)
print(label_to_index)

df = df.replace(label_to_index)

df = df.sample(frac=1)
# c
train_data = df.iloc[:120, :]
test_data = df.iloc[120:, :]

x_train = train_data.iloc[:120, 1:-1]
y_train = train_data.iloc[:120, -1:]

x_test = test_data.iloc[120:, 1:-1]
y_test = test_data.iloc[120:, -1:]
# a
min_value = train_data[c1].min()
max_value = train_data[c1].max()
x_train['pregnant-times'] = (train_data['pregnant-times'] - min_value)/(max_value - min_value)
x_test['pregnant-times'] = (train_data['pregnant-times'] - min_value)/(max_value - min_value)

min_value = x_train['glucose-concentr'].min()
max_value = x_train['glucose-concentr'].max()
x_train['glucose-concentr'] = (x_train['glucose-concentr'] - min_value)/(max_value - min_value)
x_test['glucose-concentr'] = (x_test['glucose-concentr'] - min_value)/(max_value - min_value)

min_value = x_train['blood-pressure'].min()
max_value = x_train['blood-pressure'].max()
x_train['blood-pressure'] = (x_train['blood-pressure'] - min_value)/(max_value - min_value)
x_test['blood-pressure'] = (x_test['blood-pressure'] - min_value)/(max_value - min_value)

min_value = x_train['skin-thickness'].min()
max_value = x_train['skin-thickness'].max()
x_train['skin-thickness'] = (x_train['skin-thickness'] - min_value)/(max_value - min_value)
x_test['skin-thickness'] = (x_test['skin-thickness'] - min_value)/(max_value - min_value)

min_value = x_train['insulin'].min()
max_value = x_train['insulin'].max()
x_train['insulin'] = (x_train['insulin'] - min_value)/(max_value - min_value)
x_test['insulin'] = (x_test['insulin'] - min_value)/(max_value - min_value)

min_value = x_train['mass-index'].min()
max_value = x_train['mass-index'].max()
x_train['mass-index'] = (x_train['mass-index'] - min_value)/(max_value - min_value)
x_test['mass-index'] = (x_test['mass-index'] - min_value)/(max_value - min_value)

min_value = x_train['pedigree-func'].min()
max_value = x_train['pedigree-func'].max()
x_train['pedigree-func'] = (x_train['pedigree-func'] - min_value)/(max_value - min_value)
x_test['pedigree-func'] = (x_test['pedigree-func'] - min_value)/(max_value - min_value)

min_value = x_train['age'].min()
max_value = x_train['age'].max()
x_train['age'] = (x_train['age'] - min_value)/(max_value - min_value)
x_test['age'] = (x_test['age'] - min_value)/(max_value - min_value)
# Build the model

model = Sequential()

model.add(Dense(10, input_shape=(8,), activation='relu', name='fc1'))
model.add(Dense(10, activation='relu', name='fc2'))
model.add(Dense(2, activation='softmax', name='output'))

# Adam optimizer with learning rate of 0.001
optimizer = Adam(lr=0.001)
model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

print('Neural Network Model Summary: ')
print(model.summary())

# Train the model
y_train = np_utils.to_categorical(y_train, num_classes=2)
y_test = np_utils.to_categorical(y_test, num_classes=2)
model.fit(x_train, y_train, verbose=2, batch_size=5, epochs=200)
