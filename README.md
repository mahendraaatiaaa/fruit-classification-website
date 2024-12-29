# 🌟 Image Classification 🌟
Final Deep Learning Project : Fruit Classification Website

Fruit Classification is a simple website that could classify the fruits into **10 different classes** and the website using simple Machine Learning model and combines with the basic of Deep Learning Model with HTML, CSS, JavaScript with Flask app

# 🗝 Explanation

1. **Classes /  Category** : For this website, we used **10 different classes** for classify/identify images : **Grapes, Apple, Starfruit, Orange, Kiwi, Mango, Pineapple, Banana, Watermelon, Strawberry**

2. **The Model Architecture** : For this website, the architecture we used **SimpleNet2D** with the custom from Simple CNN ( Convolutional Neural Network )

3. **Model Convertion** : The first, the model is build from PyTorch and then its convert to .pth file. From .pth file, convert again to ONNX so its could help build it with the website

4. **Dataset** : For this website, we collected the different dataset from Google and Kaggle. The dataset used for this model consists of **2,000 images** in total, with **10 distinct fruit classes: grape, apple, starfruit, orange, kiwi, mango, pineapple, banana, watermelon, and strawberry.** Each class is represented by 200 images, which are split into training, validation, and testing datasets. For each class, there are **150 images in the training dataset, 30 images in the validation dataset, and 20 images in the testing dataset.** All images in the dataset have a white background, ensuring uniformity across the images for consistent model training and evaluation. So the ratio for this dataset is **15:3:2**

5. **The Development of Website** : For this website, we build the website using HTML, CSS, JavaScript with Flask App so its could build the website

# 💡 How to Upload the Photos :

1. Upload the fruit photos that matched the rules we made before
2. The photos wil be doing precosessing data to ONNX for classification
3. After that, the result will come out with all the 10 different classes with the highest prediction

Here is some rules that should be aware of : 
* The background must be plain white.
* The image must not be a 2D or 3D illustration.
* The image should feature one fruit positioned at the center.
* The fruit must have a natural appearance and common characteristics.
* The fruit must not be rotten or show signs of decay.
* The image size must be 177x177 pixels.

# 💻 Website 
Here is the final look of the website : 

![image](https://github.com/user-attachments/assets/7ab735b9-fa60-450d-827c-a13db7c4ca8f)

# 🗂 Repositories 
* Model Repositories :
* Website Repositories : https://github.com/mahendraaatiaaa/fruit-classification-website/
* Website Deployment : https://nabilamutiarasusetio.pythonanywhere.com/

# 🔐 The Editor :
* Nabila Mutiara Susetio : https://github.com/nabilamutiara/
* Tatia Mahendra : https://github.com/mahendraaatia/
