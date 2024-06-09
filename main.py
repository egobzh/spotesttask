from packetsparse import Parse
import sys
import json
import time

def json_to_file(name,data):
    with open(f'{name}.json', 'w') as outfile:
        json.dump(data, outfile)

def main():
    parser = Parse()
    try:
        parser.get_data()
    except:
        print('Cant get data:( Try again later or check urls for validity in module!!')
        return

    if len(sys.argv) == 1:
        timestring = time.strftime("%Y%m%d-%H%M%S")
        result = parser.get_sisyphus()
        json_to_file('sisyphus_' + timestring, result)
        result = parser.get_p10()
        json_to_file('p10_' + timestring, result)
        result = parser.sisyphus_higher()
        json_to_file('sisyphus_higher_' + timestring, result)
    else:
        if sys.argv[1] == '--s':
            result = parser.get_sisyphus()
            timestring = time.strftime("%Y%m%d-%H%M%S")
            json_to_file('sisyphus_'+timestring, result)
        elif sys.argv[1] == '--p':
            result = parser.get_p10()
            timestring = time.strftime("%Y%m%d-%H%M%S")
            json_to_file('p10_'+timestring, result)
        elif sys.argv[1] == '--sh':
            result = parser.sisyphus_higher()
            timestring = time.strftime("%Y%m%d-%H%M%S")
            json_to_file('sisyphus_higher_'+timestring, result)
        else:
            timestring = time.strftime("%Y%m%d-%H%M%S")
            result = parser.get_sisyphus()
            json_to_file('sisyphus_' + timestring, result)
            result = parser.get_p10()
            json_to_file('p10_' + timestring, result)
            result = parser.sisyphus_higher()
            json_to_file('sisyphus_higher_' + timestring, result)

if __name__ == '__main__':
    main()