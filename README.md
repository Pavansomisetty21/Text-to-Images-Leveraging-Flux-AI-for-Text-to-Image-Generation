# Text-to-Images-Leveraging-Flux-API-for-Text-to-Image-Generation
we explores the fascinating domain of text-to-image generation using the powerful capabilities of the Flux API. The objective is to transform textual descriptions into vivid and accurate visual representations, leveraging state-of-the-art artificial intelligence

FLUX.1 AI is an advanced text-to-image generation model that transforms detailed text prompts into stunning, high-quality images. Utilizing a 12B parameter rectified flow transformer, it offers exceptional prompt adherence, visual quality, and style diversity. Users can select from three models: FLUX.1 [pro], FLUX.1 [dev], and FLUX.1 [schnell], catering to various needs from commercial applications to rapid prototyping. The model excels in generating intricate scenes and supports diverse aspect ratios, making it a versatile tool for artists and designers alike.

Black Forest Labs, a startup formed by some of the original Stable Diffusion minds, has unleashed a family of models called Flux, and they’re absolutely insane. These models are so good at text rendering that they’ve got even the most seasoned AI artists talking.

Three Models, Three Strengths:

`Flux Pro` is the powerhouse, offering incredible image quality but available only through APIs .

`Flux Dev` is open-weight, allowing developers to tinker and experiment, but it’s not for commercial use.

`Flux Schnell` is the most accessible, with open source licensing and available on Hugging Face, making it perfect for personal projects or integrations with tools like Diffusers or Comfy UI.

1. Calling the API

Install the client

The client provides a convenient way to interact with the model API.

```python
pip install fal-client
```
2. Schema
2.1 Input
#
`prompt`    *string*

The prompt to generate an image from.

`image_size`     ImageSize | Enum

The size of the generated image. Default value: landscape_4_3

Possible values: "square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"

`num_inference_steps`      integer

The number of inference steps to perform. Default value: 28

`seed `       integer

The same seed and the same prompt given to the same version of the model will output the same image every time.

`guidance_scale` float

The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you. Default value: 3.5

`sync_mode`    boolean

If set to true, the function will wait for the image to be generated and uploaded before returning the response. This will increase the latency of the function but it allows you to get the image directly in the response without going through the CDN.

`num_images`    integer

The number of images to generate. Default value: 1

`enable_safety_checker`    boolean

If set to true, the safety checker will be enabled. Default value: true


```python
{
  "prompt": "create a photo visualizing serene yoga poses of Spiderman in a natural setting promoting mental and physical well-being.",
  "image_size": "landscape_4_3",
  "num_inference_steps": 28,
  "guidance_scale": 3.5,
  "num_images": 1,
  "enable_safety_checker": True
}
```

2.2 Output
#

`images`    list<Image>

The generated image files info.

`timings`    Timings

`seed` integer

Seed of the generated Image. It will be the same value of the one passed in the input or the randomly generated that was used in case none was passed.

`has_nsfw_concepts`    list<boolean>

Whether the generated images contain NSFW concepts.

`prompt`    string

The prompt used for generating the image.


{
  "images": [
    {
      "url": "",
      "content_type": "image/jpeg"
    }
  ],
  "prompt": ""
}






# Example for Generating Image from Text
``` python
import os
import fal_client
from PIL import Image
import requests
from io import BytesIO
from IPython.display import display

# Set the environment variable
os.environ['FAL_KEY'] = 'Your FAL api key'

# Submit the request
handler = fal_client.submit(
    "fal-ai/flux/dev",
    arguments={
        "prompt": "create a photo visualizing serene yoga poses of Spiderman in a natural setting promoting mental and physical well-being.",
        "image_size": "landscape_4_3",
        "num_inference_steps": 28,
        "guidance_scale": 3.5,
        "num_images": 1,
        "enable_safety_checker": True
    },
)

result = handler.get()
print(result)

# Extract the image URL from the result
image_url = result['images'][0]['url']

# Function to load and display the image in Jupyter Notebook
def display_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    display(img)

# Define the prompt template
template = """The image has been loaded successfully from the URL: {url}
Now, displaying the image...
"""

# Function to format the prompt and display the image
def process_image(url):
    prompt_text = template.format(url=url)
    display_image(url)
    return prompt_text

# Invoke the process_image function with the image URL
response = process_image(image_url)
print(response)
```

## output 

The  output for the above code is as 

![Image](https://fal.media/files/koala/JkGwq09qZJvJn9m-Z7WgJ.png)
