default:
	@cat makefile

env:
	pipx install --python python3.12 --force .

update: env
	. env/bin/activate; pip install --upgrade pip --break-system-packages
	. env/bin/activate; pip install -r requirements.txt --break-system-packages

ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	. env/bin/activate; python3 -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wsjgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=500 https://www.wsj.com/market-data/stocks/us/movers > wsjgainers.html

wsjgainers.csv: wsjgainers.html
	python -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('wsjgainers.csv')"

lint:   # as mentioned in the comment for validation.yaml the make lint command is not working in github actions.
        # so we can do one of two things....
        # in this file, the makefile, we can do something like `. env/bin/activate; pylint bin/gainers/`   and the same for the pytest line
        # OR
        # in the validation.yaml add the `. env/bin/activate` in the line before you call `make lint` and that should get it to work
	pylint bin/gainers/
	pytest -vvx tests

test: lint

	pytest -vvx tests

gainers:
	python get_gainer.py $(SRC)
