import mplcyberpunk
import matplotlib.pyplot as plt

def plot_loss_curves(history):
    """
    Returns separate loss curves for training and validation metrics.
    """
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    accuracy = history.history['accuracy']
    val_accuracy = history.history['val_accuracy']

    epochs = range(len(history.history['loss']))
    plt.style.use("cyberpunk")

    # Plot loss
    plt.figure(figsize=(16, 8))
    plt.plot(epochs, loss, label='training_loss')
    plt.plot(epochs, val_loss, label='val_loss')
    plt.title('Loss')
    plt.xlabel('Epochs')
    plt.legend(fontsize=20)
    mplcyberpunk.add_glow_effects()

    # Plot accuracy
    plt.figure(figsize=(16, 8))
    plt.plot(epochs, accuracy, label='training_accuracy')
    plt.plot(epochs, val_accuracy, label='val_accuracy')
    plt.title('Accuracy')
    plt.xlabel('Epochs')
    plt.legend(fontsize=16)
    mplcyberpunk.add_glow_effects()