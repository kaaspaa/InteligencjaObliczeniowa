import pandas as pd
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


df = pd.read_csv('iris.csv', delimiter=',', encoding="utf-8-sig")
c1 = df.columns[0]
print(df.head())
rows, cols = df.shape
print(rows)
print(cols)
# b
label_names = df['species'].unique()
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
x_train['sepal_length'] = (train_data['sepal_length'] - min_value)/(max_value - min_value)
x_test['sepal_length'] = (train_data['sepal_length'] - min_value)/(max_value - min_value)

min_value = x_train['sepal_width'].min()
max_value = x_train['sepal_width'].max()
x_train['sepal_width'] = (x_train['sepal_width'] - min_value)/(max_value - min_value)
x_test['sepal_width'] = (x_test['sepal_width'] - min_value)/(max_value - min_value)

min_value = x_train['petal_length'].min()
max_value = x_train['petal_length'].max()
x_train['petal_length'] = (x_train['petal_length'] - min_value)/(max_value - min_value)
x_test['petal_length'] = (x_test['petal_length'] - min_value)/(max_value - min_value)

min_value = x_train['petal_width'].min()
max_value = x_train['petal_width'].max()
x_train['petal_width'] = (x_train['petal_width'] - min_value)/(max_value - min_value)
x_test['petal_width'] = (x_test['petal_width'] - min_value)/(max_value - min_value)
# Build the model

model = Sequential()

model.add(Dense(10, input_shape=(4,), activation='relu', name='fc1'))
model.add(Dense(10, activation='relu', name='fc2'))
model.add(Dense(3, activation='softmax', name='output'))

# Adam optimizer with learning rate of 0.001
optimizer = Adam(lr=0.001)
model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

print('Neural Network Model Summary: ')
print(model.summary())

# Train the model
y_train = np_utils.to_categorical(y_train, num_classes=3)
y_test = np_utils.to_categorical(y_test, num_classes=3)
model.fit(x_train, y_train, verbose=2, batch_size=5, epochs=200)
