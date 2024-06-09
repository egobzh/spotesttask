import requests
import rpm_vercmp

class Parse:
    def __init__(self):
        self.packets = []

    def get_data(self):
        """Receives data about binary packages from the site. Urls in variables
        sisyphus and p10 can be changed if you need."""
        sisyphus = requests.get(url='https://rdb.altlinux.org/api/export/branch_binary_packages/sisyphus')
        p10 = requests.get(url='https://rdb.altlinux.org/api/export/branch_binary_packages/p10')
        result = {'archs': []}

        for packet in sisyphus.json()['packages']:
            if packet['arch'] not in result['archs']:
                result['archs'].append(packet['arch'])
                result[packet['arch']] = {}
                result[packet['arch']][packet['name']] = {'sisyphus': packet['version'],
                                                          'p10': None}
            else:
                if packet['name'] in result[packet['arch']]:
                    result[packet['arch']][packet['name']]['sisyphus'] = packet['version']
                else:
                    result[packet['arch']][packet['name']] = {'sisyphus': packet['version'],
                                                              'p10': None}

        for packet in p10.json()['packages']:
            if packet['arch'] not in result['archs']:
                result['archs'].append(packet['arch'])
                result[packet['arch']] = {}
                result[packet['arch']][packet['name']] = {'sisyphus': None,
                                                          'p10': packet['version']}
            else:
                if packet['name'] in result[packet['arch']]:
                    result[packet['arch']][packet['name']]['p10'] = packet['version']
                else:
                    result[packet['arch']][packet['name']] = {'sisyphus': None,
                                                          'p10': packet['version']}
        self.packets = result

    def get_p10(self):
        """Get binary packages which in p10, but not in sisyphus."""
        result = {'archs':[]}
        for arch in self.packets['archs']:
            packets = []
            for packet in self.packets[arch]:
                if self.packets[arch][packet]['sisyphus'] == None and self.packets[arch][packet]['p10']:
                    packets.append(packet)
            if packets:
                result['archs'].append(arch)
                result[arch] = packets
        return result

    def get_sisyphus(self):
        """Get binary packages which in sisyphus, but not in p10."""
        result = {'archs':[]}
        for arch in self.packets['archs']:
            packets = []
            for packet in self.packets[arch]:
                if self.packets[arch][packet]['sisyphus'] and self.packets[arch][packet]['p10'] == None:
                    packets.append(packet)
            if packets:
                result['archs'].append(arch)
                result[arch] = packets
        return result

    def sisyphus_higher(self):
        """Get binary packages which version-release in sisyphus higher than p10."""
        result = {'archs': []}
        for arch in self.packets['archs']:
            packets = []
            for packet in self.packets[arch]:
                if self.packets[arch][packet]['sisyphus'] and self.packets[arch][packet]['p10']:
                    if rpm_vercmp.vercmp(self.packets[arch][packet]['sisyphus'], self.packets[arch][packet]['p10']) > 0:
                        packets.append(packet)
            if packets:
                result['archs'].append(arch)
                result[arch] = packets
        return result