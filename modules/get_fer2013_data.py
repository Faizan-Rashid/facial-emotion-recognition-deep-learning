
from pathlib import Path
import requests
import zipfile
import os

def get_fer2013_data(destination: str,
                     remove_source: bool):

  data_path = Path("data")
  image_path = data_path / destination

  # Download
  if not image_path.is_dir():
    image_path.mkdir(parents=True, exist_ok=True)
  
  if not (data_path / "fer2013.zip").is_file():
    print(f"zip file not found downloading from kagglehub")
    # command to download fer2013 data from kaggle - https://www.kaggle.com/datasets/msambare/fer2013
    r = requests.get("https://www.kaggle.com/api/v1/datasets/download/msambare/fer2013")

    with open(data_path / "fer2013.zip", "wb") as f:
      f.write(r.content)

    # extract the zip file data into image_path
    with zipfile.ZipFile(data_path / "fer2013.zip", "r") as zip_ref:
      zip_ref.extractall(image_path)

  if remove_source:
    # remove the zip file
    os.remove(data_path / "fer2013.zip")
    print(f"Extracted {data_path/"fer2013.zip"} file to {image_path}")

  return image_path
