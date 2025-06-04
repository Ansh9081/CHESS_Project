from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import re
import cv2

piece_symbols = ['p', 'n', 'b', 'r', 'q', 'k', 'P', 'N', 'B', 'R', 'Q', 'K', ' ']

app = Flask(__name__)
model = tf.keras.models.load_model(r"C:\Users\ASUS\OneDrive\Desktop\chess_ai\Backend\CNN\my_model.keras")

def onehot_from_fen(fen):
    eye = np.eye(13)
    output = np.empty((0, 13))
    fen = re.sub('[-]', '', fen)
    fen = re.sub(r'[^prbnkqPRBNKQ12345678]', '', fen)

    for char in fen:
        if(char in '12345678'):
            output = np.append(
              output, np.tile(eye[12], (int(char), 1)), axis=0)
        else:
            idx = piece_symbols.index(char)
            output = np.append(output, eye[idx].reshape((1, 13)), axis=0)

    return output

def fen_from_onehot(one_hot):
    output = ''
    for j in range(8):
        for i in range(8):
            if(one_hot[j][i] == 12):
                output += ' '
            else:
                output += piece_symbols[one_hot[j][i]]
        if(j != 7):
            output += '-'

    for i in range(8, 0, -1):
        output = output.replace(' ' * i, str(i))

    return output

def images_to_square(img,width,height):
  squares = []
  for i in range(0,8):
    for j in range(0,8):
      new_img = img[i*height//8:i*height//8+height//8,j*width//8:j*width//8+width//8]
      squares.append(new_img)

  return np.array(squares)


def preprocess_image(img_path):
    height =240
    width =240

    # change to Grey scal
    img = cv2.imread(img_path, cv2.COLOR_BGR2GRAY)

    # resize the image to the desired size
    gray_image = cv2.resize(img, (width, height))

    # Normalize the image
    gray_image =(gray_image - np.min(gray_image)) / (np.max(gray_image) - np.min(gray_image))

    squares = images_to_square(gray_image,height,width)
    return squares


@app.route('/predict', methods=['POST'])
def predict():
    formData = request.json  # Get input data from the frontend
    print(formData)
    print("hello")
    # input_tensor = tf.convert_to_tensor(data['input'])
    # prediction = model.predict(input_tensor)
    # return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
