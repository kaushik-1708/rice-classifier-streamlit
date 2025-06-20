# 🌾 GrainPalette - A Deep Learning Odyssey in Rice Type Classification

This project is part of an internship titled **"GrainPalette - A Deep Learning Odyssey in Rice Type Classification Through Transfer Learning."**  
It classifies rice grain types using a fine-tuned MobileNetV2 model and provides a clean UI built with Streamlit.

---

## 💡 Features

- Upload a rice grain image
- Predicts the rice variety using deep learning
- Built with **Transfer Learning** (MobileNetV2)
- Simple and clean web UI using **Streamlit**

---

## 🧠 Model Information

- Base Model: MobileNetV2 (`imagenet` weights)
- Fine-tuned on a dataset of 5 rice classes:
  - Arborio
  - Basmati
  - Ipsala
  - Jasmine
  - Karacadag
- Trained using `tensorflow.keras`

---

## 📂 Project Structure

```
GrainPalette/
├── app.py                   # Streamlit frontend
├── rice_classifier_mobilenetv2.h5  # Trained model
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## 🔧 Running Locally

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Launch the Streamlit app

```bash
streamlit run app.py
```

---

## ☁️ Deploying on Streamlit Cloud

> To make the project accessible online:

1. Push the code to a GitHub repository.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New App** → Select your GitHub repo
4. Set `app.py` as the entry point
5. Ensure `requirements.txt` includes:
   ```
   streamlit
   tensorflow-cpu==2.12.0
   numpy
   pillow
   ```
6. Click **Deploy** — your app will be live at a public URL!

---

## 📜 License

This project is developed as part of an academic internship.  
Model and UI created for educational and demo purposes.
