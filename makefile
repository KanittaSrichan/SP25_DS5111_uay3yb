default:
	@cat makefile

# Create and set up the virtual environment
env:
	python3.12 -m venv env
	. env/bin/activate && pip install -r requirements.txt

# Update pip and install requirements
update: env
	. env/bin/activate && pip install --upgrade pip
	. env/bin/activate && pip install -r requirements.txt

# Fetch the HTML for Yahoo Gainers
ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

# Convert the Yahoo Gainers HTML to CSV
ygainers.csv: ygainers.html
	. env/bin/activate && python3 -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

# Fetch the HTML for WSJ Gainers
wsjgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=500 https://www.wsj.com/market-data/stocks/us/movers > wsjgainers.html

# Convert the WSJ Gainers HTML to CSV
wsjgainers.csv: wsjgainers.html
	. env/bin/activate && python -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('wsjgainers.csv')"

# Lint the code and run tests
lint:
	pylint bin/gainers/
	pytest -vvx tests

# Run tests
test: lint
	pytest -vvx tests

# Run the gainer script
gainers:
	python get_gainer.py $(SRC)
