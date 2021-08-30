cp config/main.py main.py
cp config/env-dump .env
cp config/seeding.py seeding.py  
python3 seeding.py
rm seeding.py
rm config/main.py
rm config/env-dump
