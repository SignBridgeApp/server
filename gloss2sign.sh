#!/bin/bash

URL="https://github.com/SignBridgeApp/models/releases/download/v0.0/gloss2sign.zip"
ZIP_FILE="gloss2sign.zip"
TARGET_DIR="gloss2sign"

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

pip3 install --pre -f https://dist.mxnet.io/python 'mxnet==2.0.0b20220206'
apt install -y sentencepiece
