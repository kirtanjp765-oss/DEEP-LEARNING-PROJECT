import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# ==============================
# STEP 1: LOAD DATA
# ==============================

print("📥 Loading dataset...")

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalize data (0–255 → 0–1)
x_train = x_train / 255.0
x_test = x_test / 255.0

print("✅ Data Loaded!\n")


# ==============================
# STEP 2: BUILD MODEL
# ==============================

print("🧠 Building model...")

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("✅ Model Ready!\n")


# ==============================
# STEP 3: TRAIN MODEL
# ==============================

print("🏋️ Training model...")

history = model.fit(
    x_train, y_train,
    epochs=5,
    validation_data=(x_test, y_test)
)

print("✅ Training Complete!\n")


# ==============================
# STEP 4: EVALUATE MODEL
# ==============================

test_loss, test_acc = model.evaluate(x_test, y_test)

print(f"🎯 Test Accuracy: {test_acc:.4f}")


# ==============================
# STEP 5: VISUALIZE RESULTS
# ==============================

plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.title("Model Accuracy")
plt.show()


# ==============================
# STEP 6: SAVE MODEL
# ==============================

model.save("mnist_model.h5")
print("💾 Model Saved Successfully!")
