# Krezy - Cross-Platform Emotion Detection

A powerful and easy-to-use emotion detection library for Python that works seamlessly across web, mobile, and desktop applications.

## ✨ Features

- 🎯 **Real-time Emotion Detection**
  - Analyzes emotions from live video feeds
  - Supports webcam input
  - Fast and efficient processing

- 🔍 **Multiple Detection Backends**
  - OpenCV (default, fastest)
  - RetinaFace (most accurate)
  - MTCNN
  - SSD

- 📊 **Rich Emotion Analysis**
  - 7 basic emotions: Happy, Sad, Angry, Fear, Surprise, Disgust, Neutral
  - Percentage scores for each emotion
  - Dominant emotion detection
  - Timestamp tracking

- 🌐 **Cross-Platform Support**
  - Web applications (Flask)
  - Mobile apps (Kivy)
  - Desktop software (CustomTkinter)
  - Platform-specific optimizations

## 🚀 Installation

Install the package based on your needs:

```bash
# Core package (emotion detection only)
pip install krezy

# For web applications
pip install krezy[web]

# For mobile applications
pip install krezy[mobile]

# For desktop applications
pip install krezy[desktop]

# For all platforms
pip install krezy[all]
```

Note: Do NOT use `pip install krezy_web` - that's not the correct package name. The correct format is `krezy[web]`.

## 📖 Quick Start

### Basic Emotion Detection

```python
from krezy import EmotionDetector

# Initialize detector
detector = EmotionDetector()

# Analyze an image
result = detector.detect_emotions('path/to/image.jpg')
print(result['emotions'])  # Shows emotion percentages
print(result['dominant_emotion'])  # Shows strongest emotion
```

### Web Application

```python
from krezy.web import create_app

# Create a Flask web app with emotion detection
app = create_app()
app.run(debug=True)

# Your emotion detection is now available at:
# - http://localhost:5000/ (web interface)
# - http://localhost:5000/analyze (API endpoint)
```

### Mobile Application

```python
from krezy.mobile import create_app

# Create a Kivy mobile app with emotion detection
app = create_app()
app.run()
```

### Desktop Application

```python
from krezy.desktop import create_app

# Create a modern desktop app with emotion detection
app = create_app()
app.run()
```

## 🎮 Advanced Usage

### Custom Backend Selection

```python
from krezy import EmotionDetector

# Use RetinaFace for better accuracy
detector = EmotionDetector(detector_backend='retinaface')

# Use MTCNN for balanced performance
detector = EmotionDetector(detector_backend='mtcnn')
```

### Real-time Video Analysis

```python
from krezy import EmotionDetector

detector = EmotionDetector()

# Start webcam analysis with visualization
detector.start_video_stream(camera_id=0, display_output=True)
```

## 📋 Requirements

- Python 3.7+
- OpenCV
- DeepFace
- Platform-specific requirements are handled automatically during installation

## 🔧 Troubleshooting

Common issues and solutions:

1. **No face detected**
   - Ensure good lighting conditions
   - Check if face is clearly visible
   - Try different detector backend

2. **Performance issues**
   - Use 'opencv' backend for speed
   - Reduce video resolution
   - Check system resources

3. **Installation errors**
   - Ensure Python 3.7+ is installed
   - Update pip: `python -m pip install --upgrade pip`
   - Install platform-specific dependencies first

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

Need help? Try these resources:
- [GitHub Issues](https://github.com/itsaakif/krezy/issues)
- Email: aakifmudel@gmail.com
