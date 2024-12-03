"""
Core emotion detection functionality
"""
import cv2
from deepface import DeepFace
import numpy as np
from datetime import datetime
from typing import Dict, Union, List, Optional

class EmotionDetector:
    """
    A powerful and easy-to-use emotion detection class.
    
    Examples:
        Basic usage:
            >>> from krezy import EmotionDetector
            >>> detector = EmotionDetector()
            >>> result = detector.detect_emotions('image.jpg')
            >>> print(result['emotions'])
        
        Real-time detection:
            >>> detector = EmotionDetector()
            >>> detector.start_video_stream()
    """
    
    def __init__(self, detector_backend: str = 'opencv'):
        """
        Initialize the EmotionDetector.
        
        Args:
            detector_backend: Face detection backend ('opencv', 'ssd', 'mtcnn', 'retinaface')
        """
        self.detector_backend = detector_backend
    
    def detect_emotions(self, input_data: Union[str, np.ndarray, List[Union[str, np.ndarray]]]) -> Dict:
        """
        Detect emotions in images.
        
        Args:
            input_data: Can be:
                - Path to image file
                - NumPy array (BGR image)
                - List of image paths or NumPy arrays
                
        Returns:
            Dict containing:
                - success: Boolean indicating if detection was successful
                - emotions: Dict of emotion scores (if successful)
                - dominant_emotion: Most prominent emotion (if successful)
                - error: Error message (if not successful)
                - timestamp: ISO format timestamp
        """
        try:
            result = DeepFace.analyze(
                img_path=input_data,
                actions=['emotion'],
                enforce_detection=False,
                detector_backend=self.detector_backend
            )
            
            if isinstance(result, list):
                result = result[0]
            
            return {
                'success': True,
                'emotions': result['emotion'],
                'dominant_emotion': result['dominant_emotion'],
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def start_video_stream(self, camera_id: int = 0, display_output: bool = True) -> None:
        """
        Start real-time emotion detection from video stream.
        
        Args:
            camera_id: Camera device ID
            display_output: Show visualization window
        """
        cap = cv2.VideoCapture(camera_id)
        
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Flip frame for selfie view
                frame = cv2.flip(frame, 1)
                
                # Analyze frame
                result = self.detect_emotions(frame)
                
                if display_output:
                    self._display_results(frame, result)
                    
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                        
        finally:
            cap.release()
            if display_output:
                cv2.destroyAllWindows()
    
    def _display_results(self, frame: np.ndarray, result: Dict) -> None:
        """Display emotion detection results on frame."""
        if result['success']:
            # Create overlay for text
            overlay = frame.copy()
            cv2.rectangle(overlay, (10, 10), (250, 150), (0, 0, 0), -1)
            alpha = 0.4
            frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
            
            # Display emotions
            y_pos = 35
            emotions = result['emotions']
            dominant_emotion = result['dominant_emotion']
            
            for emotion, score in emotions.items():
                text = f"{emotion}: {score:.1f}%"
                color = (0, 255, 0) if emotion == dominant_emotion else (255, 255, 255)
                cv2.putText(frame, text, (15, y_pos),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                y_pos += 20
        else:
            cv2.putText(frame, "No face detected", (15, 35),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        
        cv2.imshow('Emotion Detection', frame)
