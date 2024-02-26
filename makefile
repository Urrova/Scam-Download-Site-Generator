run:
	python __main__.py

setup: requirements.txt
	pip install -r requirements.txt

windows:
	pyinstaller --onefile  --name ScamDownloadSiteGenerator __main__.py