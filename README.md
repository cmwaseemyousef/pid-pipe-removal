# P&ID Pipe Removal Project  

This project removes pipes from P&ID technical diagrams while preserving symbols using **OpenCV and Deep Learning**.

## Features  
- **Preprocesses images** (grayscale, noise reduction, edge detection).  
- **Removes pipes using morphological operations & inpainting**.  
- **Preserves symbols** with contour detection.  
- **Extracts text from symbols using Tesseract OCR**.  
- **Stores extracted metadata in JSON format**.  

## 📌 Project: Automatic Pipe Removal from Technical Diagrams  
This project focuses on automatically removing connecting pipes from P&ID technical diagrams while preserving symbols using Python, OpenCV, and Deep Learning (U-Net, optional).

### 📌 Problem Statement  
Engineering diagrams contain symbols (pumps, valves, sensors) connected by pipes. The task is to remove all pipes while preserving symbols.

- **Input**: Technical diagram (P&ID) with symbols & pipes.
- **Output**: The same diagram with pipes removed but symbols intact.

### 📌 Solution Approach  
✔ **Step 1**: Convert PDF-based diagrams to PNG images.  
✔ **Step 2**: Preprocess images (grayscale, edge detection).  
✔ **Step 3**: Use morphological operations to detect pipes.  
✔ **Step 4**: Apply image inpainting to remove detected pipes.  
✔ **Step 5**: Detect symbols & extract text metadata using OCR.  
✔ **Step 6 (Optional)**: Train a U-Net deep learning model for better accuracy.  

### 📌 Technologies Used  
| Library | Purpose |
|---------|---------|
| OpenCV  | Image processing & pipe detection |
| NumPy   | Image operations & array handling |
| Matplotlib | Visualization of results |
| Tesseract OCR | Text extraction from diagrams |
| TensorFlow/Keras | U-Net deep learning model (optional) |
| pdf2image | Convert P&ID PDF files to PNG images |

## 📌 Installation & Setup  
### 1️⃣ Install Required Libraries  
Run the following command in your VS Code terminal:
```bash
pip install opencv-python numpy matplotlib pdf2image pytesseract tensorflow
```

### 2️⃣ Install Poppler (For PDF to Image Conversion)  
**Windows**: Download & extract from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/).  
Add `C:\poppler\bin` to your system **PATH**.  
**Linux/macOS**: Run:
```bash
sudo apt install poppler-utils
```

## 📌 How to Run the Code  
### **Step 1: Convert PDF to Images**  
Run:
```bash
python convert_pdf.py
```
✅ **Output**: Saves P&ID diagrams as PNG images.

### **Step 2: Preprocess Images**  
Run:
```bash
python preprocess.py
```
✅ **Output**: Prepares binary images with pipes & symbols separated.

### **Step 3: Remove Pipes**  
Run:
```bash
python remove_pipes.py
```
✅ **Output**: Saves cleaned images with pipes removed.

### **Step 4: Detect Symbols**  
Run:
```bash
python detect_symbols.py
```
✅ **Output**: Highlights detected symbols.

### **Step 5: Extract Text Labels (OCR)**  
Run:
```bash
python extract_text.py
```
✅ **Output**: Extracted engineering metadata printed in the terminal.

### **(Optional) Step 6: Train U-Net Model**  
Run:
```bash
python train_unet.py
```
✅ **Output**: Trains deep learning model for improved pipe removal.

## 📌 Results  
### **Before and After Example:**  
| Original Diagram | Processed Output (Pipes Removed) |
|------------------|--------------------------------|

## 📌 Video Explanation  
🎥 **Watch the Video Demo**  
This video explains:
- The approach used.
- Challenges faced & how they were solved.
- A live demo of the solution.

## 📌 Contribution & Issues  
Feel free to contribute or raise issues in this repository!