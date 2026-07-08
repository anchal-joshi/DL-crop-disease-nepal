# Nepal Crop Disease Diagnosis — CSC60904 Deep Learning

A supervised deep learning system for diagnosing plant diseases in crops
commonly grown in Nepal (tomato, potato, maize). Built for the AI for the
Himalayas 2026 hackathon as part of Taylor's University CSC60904.

---

## Team Members

| Name | Student ID | Role |
|---|---|---|
| Member 1 | ANCHAL JOSHI | Team Lead |
| Member 2 | SAMAR MAHARJAN | Data Engineer |
| Member 3 | TBD | ML Engineer |
| Member 4 | BISHAL GODAR THAPA | Ethics & Evaluation Lead |

---

## Project Structure

```
DL-crop-disease-nepal/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md          ← dataset download instructions
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_data_pipeline.ipynb
│   ├── 03_baseline_cnn.ipynb
│   ├── 04_transfer_learning.ipynb
│   └── 05_evaluation.ipynb
├── src/
│   └── app.py             ← Streamlit demo
├── models/
│   ├── class_names.npy
│   └── class_weights.npy
├── results/
│   ├── class_distribution.png
│   ├── augmentation_examples.png
│   └── split_summary.csv
└── docs/
    ├── proposal.pdf
    └── final_report.pdf
```

---

## Installation

### Step 1 — Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/DL-crop-disease-nepal.git
cd DL-crop-disease-nepal
```

### Step 2 — Create and activate environment
```bash
conda create -n dlenv python=3.10
conda activate dlenv
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

| Package | Purpose |
|---|---|
| tensorflow | Model building and training |
| numpy | Array operations |
| pandas | Data tables and CSV handling |
| matplotlib | Charts and visualisations |
| seaborn | Confusion matrix heatmap |
| scikit-learn | Metrics and class weights |
| Pillow | Image loading and conversion |
| streamlit | Demo web app |
| jupyter | Running notebooks |

---

## How to Run

### Run notebooks in order
```
1. notebooks/01_data_cleaning.ipynb
2. notebooks/02_data_pipeline.ipynb
3. notebooks/03_baseline_cnn.ipynb
4. notebooks/04_transfer_learning.ipynb
5. notebooks/05_evaluation.ipynb
```

Open Jupyter with:
```bash
conda activate dlenv
jupyter notebook
```

### Run the Streamlit demo
```bash
conda activate dlenv
cd src
streamlit run app.py
```

A browser window will open automatically at http://localhost:8501

---

## Dataset

PlantVillage dataset — 54,305 images across 38 plant disease classes.
See `data/README.md` for full download and setup instructions.

Source: https://www.kaggle.com/datasets/emmarex/plantdisease

---

## Results Summary

| Model | Validation Accuracy |
|---|---|
| Baseline CNN | TBD after training |
| EfficientNetB0 (Transfer Learning) | TBD after training |

*(Update this table after completing notebooks 03 and 04)*

---

## Citation

D. P. Hughes and M. Salathé, "An open access repository of images for
identification of plant diseases," arXiv:1511.08060, 2015.