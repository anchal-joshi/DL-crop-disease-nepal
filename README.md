# Nepal Crop Disease Diagnosis — CSC60904 Deep Learning

A supervised deep learning system for diagnosing plant diseases in crops
commonly grown in Nepal (tomato, potato, pepper). Built as part of Taylor's
University CSC60904 Deep Learning group assignment.

---

## Team Members

| Name                 | Student ID | Role                                                             |
|----------------------|------------|------------------------------------------------------------------|
| ANCHAL JOSHI         | [ID]       |Team Lead/Project Manager, ML Engineer, Evaluation and Ethics Lead|
| SAMAR MAHARJAN       | [ID]       | Data Engineer, ML Engineer                                       |
| BISHAL GODAR THAPA   | [ID]       | Documentation and Presentation Lead, ML Engineer                 |

<!-- UPDATE: Replace [NAME] and [ID] with actual details. -->

---

## Project Structure

```text
DL-crop-disease-nepal/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md          <= dataset download instructions
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_data_pipeline.ipynb
│   ├── 03_baseline_cnn.ipynb
│   ├── 04_transfer_learning.ipynb
│   
├── src/
│   └── app.py             <= Gradio demo (baseline CNN)
├── models/
│   ├── class_names.npy
│   ├── class_weights.npy
│   ├── baseline_cnn_best.keras
│   ├── baseline_cnn_final.keras
│   └── tl_tinyvgg_final.keras   (transfer-learning model)
├── results/
│   ├── augmentation_examples.png
│   ├── baseline_cnn_training_curves.png
│   ├── baseline_confusion_matrix.png
│   ├── baseline_history.json
│   ├── baseline_training_log.csv
│   ├── class_distribution.png
│   ├── class_distribution_all38.png
│   ├── sample_images.png
│   ├── sample_training_images.png
│   └── split_summary.csv
└── docs/
    ├── proposal.pdf
    └── final_report.pdf
```

<!-- UPDATE: If your transfer-learning model has a different filename,
     change tl_tinyvgg_final.keras to match what you actually have. -->

---

## Installation

### Step 1 — Clone the repository

```bash
git clone https://github.com/anchal-joshi/DL-crop-disease-nepal.git
cd DL-crop-disease-nepal
```

### Step 2 — Create and activate environment

You can use conda or venv.

**Option A — conda**

```bash
conda create -n dlenv python=3.10
conda activate dlenv
```

**Option B — venv**

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
```

### Step 3 — Install required packages

```bash
pip install -r requirements.txt
```

### Step 4 — Download the dataset

Follow the instructions in `data/README.md` to download and set up
the PlantVillage dataset before running any notebooks.

---

## Required Packages

| Package      | Purpose                              |
|--------------|--------------------------------------|
| tensorflow   | Model building and training          |
| numpy        | Array operations                     |
| pandas       | Data tables and CSV handling         |
| matplotlib   | Charts and visualisations            |
| seaborn      | Confusion matrix heatmap             |
| scikit-learn | Metrics and class weights            |
| Pillow       | Image loading and conversion         |
| gradio       | Demo web app                         |
| jupyter      | Running notebooks                    |

---

## How to Run

### Run notebooks in order

```text
1. notebooks/01_data_cleaning.ipynb
2. notebooks/02_data_pipeline.ipynb
3. notebooks/03_baseline_cnn.ipynb
4. notebooks/04_transfer_learning.ipynb
```

Open Jupyter with:

```bash
# If using conda
conda activate dlenv

# If using venv (Windows)
# venv\Scripts\activate

jupyter notebook
```

Then navigate to the `notebooks/` folder and open the notebooks in order.

### Run the Gradio demo

From the repository root:

```bash
# Activate your environment (example for venv on Windows)
venv\Scripts\activate

# Run the app
python src/app.py
```

The terminal will show a local URL, for example:

```text
Running on local URL: http://127.0.0.1:7860
```

Open that URL in your browser, upload a leaf image, and click **Predict**.

---

## Dataset

We use the PlantVillage dataset, which contains labelled images of plant
leaves with various diseases and healthy samples. For this project, we focus
on classes relevant to Nepal (tomato, potato, pepper).

- The full dataset is not included in the repository due to its size.
- See `data/README.md` for download and setup instructions.
- Source: https://www.kaggle.com/datasets/emmarex/plantdisease

---

## Results Summary

| Model                              | Test Accuracy |
|------------------------------------|---------------|
| Baseline CNN                       | [XX.XX]%      |
| TinyVGG (Transfer-style, fine-tuned) | [YY.YY]%      |

<!-- UPDATE: Replace [XX.XX]% and [YY.YY]% with your actual test accuracies
     from your evaluation (notebooks and/or results). -->

---

## Demo Interface

The demo is a Gradio app that loads the trained baseline CNN model and
predicts the disease class for an uploaded leaf image.

- Code: `src/app.py`
- Model: `models/baseline_cnn_final.keras`
- Labels: `models/class_names.npy`

Usage:

```bash
python src/app.py
```

Then open the URL shown in the terminal in your browser.

---

## License

This repository is for educational use as part of CSC60904 Deep Learning.
The PlantVillage dataset is subject to its own license; see the dataset
page for details.

---

## Course

CSC60904 – Deep Learning, Taylor’s University  
Academic Year: 2026
