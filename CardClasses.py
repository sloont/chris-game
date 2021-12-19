class AdventurerCard:
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.type = data['type'].split('/')

        if data['value'] == 'null':
            self.value = None
        else:
            splitValue = data['value'].split(' ')
            self.value = {
                'type': splitValue[1],
                'amount': splitValue[0],
            }
        
        self.description = data['description'] if data['description'] != 'null' else None
        
