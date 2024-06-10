## Preparation to run
1. Clone the repository
2. Create and activate virtual environment
```commandline 
python -m venv venv
GitBash: source venv/Scripts/activate
Windows: venv\Scripts\activate
Linux: source venv/bin/activate
```
3. Install dependencies
```commandline 
pip install -r requirements.txt
```
## Variations of running
1. Get binary packages which in sisyphus, but not in p10
```commandline 
python main.py --s
```
2. Get binary packages which in p10, but not in sisyphus
```commandline 
python main.py --p
```
3. Get binary packages which version-release in sisyphus higher than p10
```commandline 
python main.py --sh
```
After running you will receive json files which names will start with sisyphus, p10, sisyphus_higher respectively. If you run CLI script without params or with any other parametr, for example:
```commandline 
python main.py
python main.py --qq
etc...
```
you will recieve three files at once.
