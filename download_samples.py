import os
import requests
from PIL import Image
from io import BytesIO

# Create directories if they don't exist
directories = ['minimalist', 'vibrant', 'natural', 'urban']
for directory in directories:
    os.makedirs(f'static/sample_images/{directory}', exist_ok=True)

# Sample image URLs (using Unsplash API)
image_urls = {
    'minimalist': [
        'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=800&auto=format&fit=crop&q=60',  # Minimalist interior
        'https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=800&auto=format&fit=crop&q=60'   # Minimalist architecture
    ],
    'vibrant': [
        'https://images.unsplash.com/photo-1513151233558-d860c5398176?w=800&auto=format&fit=crop&q=60',  # Colorful abstract
        'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&auto=format&fit=crop&q=60'   # Vibrant patterns
    ],
    'natural': [
        'https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=800&auto=format&fit=crop&q=60',  # Forest scene
        'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&auto=format&fit=crop&q=60'   # Mountain landscape
    ],
    'urban': [
        'https://images.unsplash.com/photo-1487958449943-2429e8be8625?w=800&auto=format&fit=crop&q=60',  # City skyline
        'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=60'   # Urban architecture
    ]
}

def download_and_save_image(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.save(save_path, 'JPEG', quality=85)
            print(f"Successfully downloaded and saved {save_path}")
        else:
            print(f"Failed to download image from {url}")
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")

# Download images for each category
for category, urls in image_urls.items():
    for i, url in enumerate(urls, 1):
        save_path = f'static/sample_images/{category}/{category}{i}.jpg'
        download_and_save_image(url, save_path)

print("All sample images downloaded successfully!") 