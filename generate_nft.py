from PIL import Image
import os

# File paths
background_path = "E:/NFTTest2/layers/background/boy.png"
hats_folder = "E:/NFTTest2/layers/hat"
shirts_folder = "E:/NFTTest2/layers/shirt"
output_folder = "E:/NFTTest2/output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the base image
background = Image.open(background_path)

# Function to layer images
def create_nft(background, hat_path, shirt_path, output_path):
    # Open hat and shirt images
    hat = Image.open(hat_path).convert("RGBA")
    shirt = Image.open(shirt_path).convert("RGBA")

    # Resize hat and shirt to match the background size
    hat = hat.resize(background.size)
    shirt = shirt.resize(background.size)

    # Combine layers
    combined = background.copy()
    combined.paste(shirt, (0, 0), shirt)
    combined.paste(hat, (0, 0), hat)

    # Save the output
    combined.save(output_path)

# Iterate through all combinations of hats and shirts
hat_files = [os.path.join(hats_folder, f) for f in os.listdir(hats_folder) if f.endswith(".png")]
shirt_files = [os.path.join(shirts_folder, f) for f in os.listdir(shirts_folder) if f.endswith(".png")]

for hat_file in hat_files:
    for shirt_file in shirt_files:
        hat_name = os.path.splitext(os.path.basename(hat_file))[0]
        shirt_name = os.path.splitext(os.path.basename(shirt_file))[0]

        # Generate output file name
        output_file = os.path.join(output_folder, f"nft_{hat_name}_{shirt_name}.png")

        # Create the NFT
        create_nft(background, hat_file, shirt_file, output_file)

print("NFT collection has been created successfully!")
