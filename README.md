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
## Structure of json response
The 'archs' key in json is the list that includes available architectures. Further, by keys from 'archs' list you can recieve binary packages for this architectures.
![alt text](https://s357sas.storage.yandex.net/rdisk/e487902cd4b3f968337ca8c98baf811f7998c7d4414a3c660a51ae70edc9a396/66674d5e/ThpIr2WLzSeCMRuU8iCOGA3Rs9a99NlDCpx5td7WgxarmCgS1spbqEU6Z8wOA2bFhzK7qN1uIRIkzE6bzosreg==?uid=0&filename=изображение_2024-06-10_175809215.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&fsize=10264&hid=b82ff8f8090c1b568b35f88ddd46af76&media_type=image&tknv=v2&etag=624737bed4f81a3559dc586ea0b11b91&ts=61a8dc4479380&s=f53345c701f2ae52f55d49969fd405e4810e7115641bfddbb0a3df969b01ec5f&pb=U2FsdGVkX19QMwTW3_Ec61vzagSeFKf78Ze2XZkmdUZctpP4WKXrnsrZG1_Ku_IJNl2icBvt27jJu3sPhm1daw_ZBSV2HlCzgdL4P8yUCX4)
