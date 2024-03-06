# imports
from openai import OpenAI  # OpenAI Python library to make API calls
import requests  # used to download images
import os  # used to access filepaths

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# set a directory to save DALL·E images to
image_dir_name = "images"
image_dir = os.path.join(os.curdir, image_dir_name)

# create the directory if it doesn't yet exist
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

# print the directory to save to
print(f"{image_dir=}")

# create an image

# set the prompt
prompt = """In the form of wartime art poster from 1980s:
russian actress struts down the street as if she was on runway; sultry yet unspoken mystique and allure; french style makeup; focus on subject, detailed face; ambient warm street atmosphere; well-lit, contrasting shadows; grainy texture; minimal colour palette""" 

# call the OpenAI API
generation_response = client.images.generate(
    model = "dall-e-3",
    prompt=prompt,
    n=1,
    quality="hd",
    size="1024x1024",
    response_format="url",
)

# print response

print(generation_response)

generated_image_name = "generated_image.png"  # any name you like; the filetype should be .png
generated_image_filepath = os.path.join(image_dir, generated_image_name)
generated_image_url = generation_response.data[0].url  # extract image URL from response# Handle None case for generation_response.data


if generation_response.data is None:
    print("No image was generated. Check your prompt and try again.")
else:
    for image_info in generation_response.data:
        if image_info.url is not None:
            generated_image_url = image_info.url  # ensure URL is not None
            generated_image_response = requests.get(generated_image_url)

            if generated_image_response.status_code == 200:
                generated_image = generated_image_response.content  # download the image as bytes

                # Save the image to the filesystem
                with open(generated_image_filepath, 'wb') as f:
                    f.write(generated_image)
                print(f"Image saved to {generated_image_filepath}")
            else:
                print(f"Failed to download the image. Status code: {generated_image_response.status_code}")
        else:
            print("No image URL was provided in the response.")
