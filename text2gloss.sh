#!/bin/bash

URL="https://github.com/SignBridgeApp/models/releases/download/v0.0/text2gloss.zip"
ZIP_FILE="text2gloss.zip"
TARGET_DIR="text2gloss"

if [ ! -d "$TARGET_DIR" ]; then
    echo "Downloading and extracting $ZIP_FILE..."

	if [ ! -d "$ZIP_FILE" ]; then
    	wget -q "$URL"
	else
    	echo "Zip $ZIP_FILE already exists. Skipping download."
	fi

	unzip -q "$ZIP_FILE" && rm "$ZIP_FILE"
	echo "Done."
else
    echo "Directory $TARGET_DIR already exists. Skipping download and extraction."
fi

