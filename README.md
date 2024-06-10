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
![alt text]([https://disk.yandex.ru/i/twQynjGiuxFVFA](https://downloader.disk.yandex.ru/preview/34cd6a503250449b5d4da5c4c7289d43fce602996350f1b49c051f21d9f3db48/66674d5e/-pZJ4dvDPKeMOs0qFtstGvRcNrJoi176JzZ1X8OQ0Iw9uKAkMDfa9GOr66U91GgyMdiETpn6ydMw0U8kp9GLsg%3D%3D?uid=0&filename=%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2024-06-10_175809215.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1312x608))
