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
        self.damage = data['damage'].split(' ')[0]
        self.health = data['health'].split(' ')[0]
        self.power = data['power']

    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_type(self):
        return self.type
    def get_damage(self):
        return self.damage
    def get_health(self):
        return self.health
    def get_power(self):
        return self.power

    #maybe this will need a defense getter

    #def get_defense(self):
    #   return self.defense