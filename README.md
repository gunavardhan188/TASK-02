# TASK-02
Pixel manipulation for image encryption
# 🔐 Pixel Manipulation for Image Encryption (Python)

## 📘 Overview
This project demonstrates a simple yet effective **image encryption and decryption** method using **pixel manipulation** techniques in Python.  
The main idea is to scramble pixel values of an image using a secret key, making it unreadable without the correct key.

---

## 🚀 Features
- Encrypts an image using pixel manipulation.  
- Decrypts the image back to its original form.  
- Uses a **secret key** for secure encryption and decryption.  
- Simple and lightweight — works with any image format (`.png`, `.jpg`, `.jpeg`, etc.).  
- Implemented using the **Pillow (PIL)** library.

---

## 🧠 How It Works
1. The program reads the image pixel by pixel.
2. Each pixel’s **RGB value** is modified using a mathematical operation (based on the secret key).
3. The modified pixels are saved to form a new **encrypted image**.
4. To decrypt, the same key and reverse operation are applied to get the **original image** back.

---

## 📂 Project Structure

