🏰 Chessboard Piece Detection Using CNN

This project leverages **Convolutional Neural Networks (CNN)** to detect and place chess pieces on a virtual chessboard based on an input image.


📝 Overview

The goal of this project is to:
✅ Take an input photo of a chessboard.  
✅ Use a trained CNN model to detect the positions of chess pieces (white/black, type of piece).  
✅ Reconstruct the chessboard by placing the detected pieces in their correct positions.


🚀 Features
- **Input:** An image of a chessboard (photo or screenshot).
- **Output:** A virtual chessboard with pieces placed in the same positions as in the photo.
- **Model:** A CNN trained to identify each piece and square.
- **Preprocessing:** Image processing to segment the chessboard and map grid coordinates.
- **Visualization:** Graphical output of the detected board state.


🎯 Model
Architecture: Convolutional Neural Network (CNN)

Trained on: Images of chessboards with different piece arrangements

Output: Piece classification (type, color) and grid positions

🏆 Results
Accuracy: ~98% on test images

Robust detection even with slight image distortion and lighting variation

📚 Future Work
Integrate with a chess engine for move suggestions

Support 3D chessboards and real-time video input

🤝 Contributing
Pull requests are welcome! Please open an issue first to discuss what you would like to change.
