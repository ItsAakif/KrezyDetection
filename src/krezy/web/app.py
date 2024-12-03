"""Web integration for Krezy"""
from flask import Flask, render_template, jsonify
from ..detector import EmotionDetector

class KrezyWebApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.detector = EmotionDetector()
        self._setup_routes()
    
    def _setup_routes(self):
        @self.app.route('/')
        def index():
            return "Krezy Web Integration Test Successful"
            
        @self.app.route('/analyze')
        def analyze():
            return jsonify({"status": "detector_ready"})
    
    def run(self, debug=True):
        self.app.run(debug=debug)

def create_app():
    return KrezyWebApp()

def main():
    app = create_app()
    app.run(debug=True)
