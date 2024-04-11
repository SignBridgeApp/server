apt install -y wget zip unzip
chmod 777 gloss2sign.sh text2gloss.sh gloss2pose.sh
pip3 install -r requirements.txt

./gloss2sign.sh
./text2gloss.sh
./gloss2pose.sh
