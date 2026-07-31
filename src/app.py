import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from pathlib import Path

# Project paths
BASE_DIR = Path(".").resolve()
MODEL_DIR = BASE_DIR / "models"

# Use BASELINE CNN model (change filename if needed)
MODEL_PATH = MODEL_DIR / "baseline_cnn_final.keras"
CLASS_NAMES_PATH = MODEL_DIR / "class_names.npy"

# Load model and class names
print("Loading baseline CNN model from:", MODEL_PATH)
model = load_model(str(MODEL_PATH))

print("Loading class names from:", CLASS_NAMES_PATH)
class_names = np.load(str(CLASS_NAMES_PATH), allow_pickle=True)

IMG_SIZE = (224, 224)


def predict_leaf(image):
    if image is None:
        return {"Predicted class": "Please upload an image.", "Confidence": "0.0000"}

    # Ensure PIL Image and RGB
    if isinstance(image, np.ndarray):
        img = Image.fromarray(image)
    else:
        img = image

    img = img.convert("RGB").resize(IMG_SIZE)

    # Preprocess
    arr = img_to_array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)

    # Predict
    preds = model.predict(arr, verbose=0)
    idx = int(np.argmax(preds, axis=1)[0])
    confidence = float(np.max(preds))
    label = str(class_names[idx])

    return {
        "Predicted class": label,
        "Confidence": f"{confidence:.4f}"
    }


with gr.Blocks(title="Plant Leaf Disease Detection (Baseline CNN)") as demo:
    gr.Markdown(
        "Upload a plant leaf image to get a predicted disease class using the baseline CNN "
        "trained on the PlantVillage split dataset (CSC60904 group project)."
    )

    with gr.Row():
        img_input = gr.Image(type="numpy", label="Upload leaf image")
        output = gr.JSON(label="Prediction")

    btn = gr.Button("Predict", variant="primary")
    btn.click(fn=predict_leaf, inputs=img_input, outputs=output)


if __name__ == "__main__":
    demo.launch()