##!/bin/bash

repository="https://github.com/KeanDelly/DigitalPhotoFrame"

localFolder="/"

git clone "$repository" "$localFolder"

python main.py