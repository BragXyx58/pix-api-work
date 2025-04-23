import tkinter as tk
from PIL import Image, ImageTk
import requests

API_KEY = "49887861-a27d8d00b4dfe3cbeb0f42094"

def random_image_url():
    url = f"https://pixabay.com/api/?key={API_KEY}&q=random&image_type=photo&per_page=50"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['hits']:
            import random
            image_url = random.choice(data['hits'])['webformatURL']
            return image_url
        else:
            print("No pic")
    else:
        print(f"API error: {response.status_code}")
    return None

def update_image():
    image_url = random_image_url()
    if image_url:
        img = Image.open(requests.get(image_url, stream=True).raw)
        img = img.resize((400, 300))
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk

root = tk.Tk()
root.title("image")
label = tk.Label(root)
label.pack()
btn = tk.Button(root, text="Next Image", command=update_image)
btn.pack(pady=10)
root.mainloop()