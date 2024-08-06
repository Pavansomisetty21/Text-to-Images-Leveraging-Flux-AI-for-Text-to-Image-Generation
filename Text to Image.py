import os
import streamlit as st
import fal_client
from PIL import Image
import requests
from io import BytesIO

# Set the environment variable
os.environ['FAL_KEY'] = 'your api key'

def generate_image(prompt):
    handler = fal_client.submit(
        "fal-ai/flux/dev",
        arguments={
            "prompt": prompt,
            "image_size": "landscape_4_3",
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
            "num_images": 1,
            "enable_safety_checker": True
        },
    )
    result = handler.get()
    return result['images'][0]['url']

def display_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def main():
    st.title("Text to Image Generation")
    
    prompt = st.text_area("Enter the prompt for image generation:", 
                          "create a photo visualizing serene front view of Spiderman with fire on body is look like a ghost rider and he was riding a bike or horse which have fire and entire scenery at endless road on the desert at night with a sky with stars and without moon.")

    if st.button("Generate Image"):
        with st.spinner("Generating image..."):
            image_url = generate_image(prompt)
            st.success("Image generated successfully!")
            st.image(display_image(image_url), caption="Generated Image")

if __name__ == "__main__":
    main()
