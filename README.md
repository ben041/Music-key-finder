# ToneCipher 🎵🔑  

ToneCipher is an intelligent **Music Key Finder** that analyzes uploaded audio files to identify the musical key, correlations, and alternative keys. Designed for musicians, producers, and enthusiasts, it offers a streamlined way to uncover the musical essence of any track.  

---

## Features  
- 🎶 **Key Detection**: Identify the primary and alternative musical keys.  
- 📈 **Correlation Analysis**: Get insights into the strength of detected keys.  
- 🎧 **Audio Playback**: Listen to the uploaded audio directly within the application.  
- 🖥️ **User-Friendly Interface**: Simple and elegant UI for easy interaction.  

---

## Installation Guide  
Follow these steps to set up and run ToneCipher on your local machine.  

### 1. Clone the Repository  
```bash  
git clone https://github.com/your-username/ToneCipher.git  
cd ToneCipher  
```  

### 2. Set Up a Virtual Environment  
- **Windows**:  
  ```bash  
  python -m venv env  
  .\env\Scripts\activate  
  ```  
- **macOS/Linux**:  
  ```bash  
  python3 -m venv env  
  source env/bin/activate  
  ```  

### 3. Install Required Libraries  
Run the following command to install the necessary dependencies:  
```bash  
pip install -r requirements.txt  
```  

### 4. Apply Migrations  
Set up the database with Django migrations:  
```bash  
python manage.py makemigrations  
python manage.py migrate  
```  

### 5. Run the Development Server  
Start the Django development server to access the app:  
```bash  
python manage.py runserver  
```  

### 6. Access the Application  
Open your browser and navigate to:  
```
http://127.0.0.1:8000/
```  

---

## How to Use ToneCipher  
1. **Upload Audio File**: Select an audio file in the upload section.  
2. **View Results**: Check the detected musical key, correlation, and alternative key information.  
3. **Playback Audio**: Use the built-in audio player to listen to the file.  

---

## Technologies Used  
- **Backend**: Django  
- **Frontend**: HTML, CSS, JavaScript  
- **Audio Analysis**: Python libraries for audio processing  

---

## Contributing  
We welcome contributions to improve ToneCipher! Feel free to fork the repository and submit a pull request.  

---

## License  
ToneCipher is licensed under the MIT License.  

---

### Author  
**Ben041**  
*A music and tech enthusiast dedicated to empowering creativity with innovative tools.*  

Enjoy using **ToneCipher** and explore the musical universe! 🎶