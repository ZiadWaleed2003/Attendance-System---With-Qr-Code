# 🚀 Attendance System with QR Code Scanner  

![App Screenshot](![alt text](image.png))  

## 📌 Overview  
This **smart Attendance System** simplifies attendance tracking by using **QR code scanning**. Unlike typical attendance systems, this application supports **both live and digital QR code scanning**, allowing for flexible and efficient attendance management.  

---

## 🔥 Features  

✅ **Multi-Camera Support**  
- Works with **Laptop/PC cameras** (built-in or external).  
- Supports **Mobile phone cameras via IV Webcam** (connect using an IP address).  

✅ **Scans Local QR Code Images**  
- You can **upload an image** containing a QR code instead of scanning a live one.  
- The system will **decode the QR code from the image and process it**.  

✅ **Automated Attendance Logging**  
- Extracts student IDs from QR codes and **automatically logs attendance**.  
- Uses **Pandas** to handle attendance records efficiently.  

✅ **CSV Export**  
- Saves attendance records in **CSV format** for easy access.  

✅ **Custom Save Directory**  
- Users can **choose where to store attendance files** for better organization.  

✅ **Lightweight & Fast**  
- Built with **Python and Tkinter**, ensuring a smooth and responsive experience.  

---

## 🛠 Installation  

1️⃣ **Download** the `setup.exe` file from the [Releases](https://github.com/ZiadWaleed2003/Attendance-System---With-Qr-Code/releases/tag/v1.0.0).  
2️⃣ **Run the installer** and follow the on-screen instructions.  
3️⃣ **Launch the application** and start scanning QR codes!  

---

## 🎯 How to Use  

### **1️⃣ Choosing the Camera Input**  
- By default, the app will use the **built-in laptop/PC camera**.  
- To use a **mobile phone camera**, follow these steps:  
  1. Install **IP Webcam** on your phone.  
  2. Open IP Webcam and copy the **IP address** shown.  
  3. Paste the **IP address** into the application.  
  4. The video feed from your mobile camera will now appear on your PC!  

### **2️⃣ Scanning QR Codes (Live or from an Image)**  
- **Live Scanning**: Hold a QR code in front of the camera, and the system will **automatically decode it**.  
- **Scanning from an Image**: Click **Upload Image**, select a file, and the app will **process the QR code from the image**.  

### **3️⃣ Attendance Logging**  
- The system expects each **QR code to contain a numerical student ID** (e.g., `2026100` or `12345`).  
- After scanning, the student's ID is **logged into a CSV file with the arrival time for each student**.  
- The file is **saved to the folder of your choice** for later access.  

---

## 📥 Requirements  

- **Windows OS** (Tested on Windows 10/11)  
- **Camera** (PC Camera OR Mobile Camera via IV Webcam)  
- **QR codes containing only numeric student IDs** (e.g., `2026100`, `12345`)  

---

## 📣 Feedback & Issues  

If you have any issues, suggestions, or feature requests, feel free to **open an issue** on this repository.  

🚀 **Enjoy a smarter, more flexible way to track attendance!**  
