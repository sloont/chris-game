class AdventurerCard:
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.type = data['type'].split('/')

        if data['value'] == 'null':
            self.value = None
        else:
            split = data['value'].split(' ')
            self.value = {
                'type': split[1],
                'amount': split[0],
            }
        
        self.description = data['description'] if data['description'] != 'null' else None

#DungeonCard is unfinished. The following is a placeholder 

class DungeonCard:
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.type = data['type'].split('/')
        self.damage = data['damage']
        self.health = data['health']
        self.power = data['power']