import os

# Path to your photos folder
folder = "public/photos"

# List all image files in the folder
files = os.listdir(folder)
photos = [f'"photos/{f}"' for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

# Sort files alphabetically (optional)
photos.sort()

# Generate JS array
output = "const photos = [\n  " + ",\n  ".join(photos) + "\n];"

# Save to photos-array.js
with open("public/photos-array.js", "w") as f:
    f.write(output)

print("photos-array.js generated successfully!")
