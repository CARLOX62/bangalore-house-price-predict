# 🏠 Bangalore House Price Prediction

This is a machine learning web application that predicts **house prices in Bangalore**, India based on key features like **location**, **square footage**, **number of bedrooms**, and **bathrooms**. The model uses historical housing data and Ridge Regression for robust predictions.

<p align="center">
  <img src="https://img.shields.io/github/languages/top/CARLOX62/bangalore-house-price-predict" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/CARLOX62/bangalore-house-price-predict" alt="Last Commit">
  <img src="https://img.shields.io/github/repo-size/CARLOX62/bangalore-house-price-predict" alt="Repo Size">
</p>

---

## 🌐 Live Demo

🔗 **Try the App**:(http://localhost:8501/)  

---

## 📸 App Screenshot

![Screenshot (59)](https://github.com/user-attachments/assets/63fdd111-fec8-441b-a3a0-c35ff94916ed)


---

## 📂 Project Structure

```
.
├── BHP.csv               # Original dataset
├── Cleaned_data.csv      # Cleaned and processed dataset
├── main.py               # Core Python script (model & prediction)
├── price.ipynb           # Jupyter Notebook for EDA & model training
├── RidgeModel.pkl        # Trained Ridge Regression model (serialized)
├── background.jpg        # Background image (optional for UI)
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 🧠 Key Features

✅ Built with **Python** and **Scikit-learn**  
✅ Data preprocessing and cleaning  
✅ Outlier handling and dimensionality reduction  
✅ Trained **Ridge Regression model**  
✅ Easy predictions using pre-trained model  
✅ Optional background visuals for UI enhancement

---

## ⚙️ Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/CARLOX62/bangalore-house-price-predict.git
cd bangalore-house-price-predict
```

### 2️⃣ Install dependencies

If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

Otherwise, install manually:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### 3️⃣ Run the Project

**Option A**: Use the Jupyter Notebook for EDA:

```bash
jupyter notebook price.ipynb
```

**Option B**: Run the main script (console-based or can be modified for web UI):

```bash
python main.py
```

---

## 🛠️ How to Use

1. Modify `Cleaned_data.csv` with your own housing dataset if needed.
2. Re-train the model using `main.py` or reuse the existing model (`RidgeModel.pkl`).
3. Make predictions based on new inputs using the script or build a web interface (Streamlit, Flask, etc.).

---

## 📊 Model and Dataset Info

- 🗃 **Dataset Source**: Kaggle/Bangalore Housing Dataset
- 📉 Model Used: **Ridge Regression**
- 🔢 Features Used:
  - Total square feet
  - Location (converted using encoding)
  - Number of bathrooms
  - Number of bedrooms (BHK)

---

## 📈 Output Example

```
Location: Electronic City Phase II
Sqft: 1000
Bath: 2
BHK: 3

Predicted Price: ₹ 56.2 Lakhs

![Screenshot (60)](https://github.com/user-attachments/assets/fa36220e-1eec-444e-ba75-35a5fa46f368)


```

---

## 📝 Notes

- `.ipynb_checkpoints/` contains autosaves — can be ignored.
- `RidgeModel.pkl` is a serialized ML model.
- No frontend UI is integrated yet — can be extended using Flask or Streamlit.

---

## 📧 Contact

📩 Email: [aniketkumarsonu62@gmail.com](mailto:aniketkumarsonu62@gmail.com)  
🔗 GitHub: [CARLOX62](https://github.com/CARLOX62)

---

## ✅ Contribution

Pull requests are welcome! For major changes, please open an issue first.

---


