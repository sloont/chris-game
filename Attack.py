class Attack:
    def __init__(self, attacker, defender):
        
        self.attacker = attacker
        self.defender = defender
        self.payload = attacker.get_damage() - defender.get_defense()

        self.defender_health_pre = self.defender.get_health()
        self.defender_health_post = self.defender_health_pre

    def attack(self, defender):
        self.defender_health_post = self.defender_health_pre - self.payload
        defender.modify_health(-self.payload)

    def log_combat(self):
        return {
            'attacker': self.attacker.get_name(),
            'defender': self.defender.get_name(),
            'damage': self.payload,
            'defender_health_pre': self.defender_health_pre,
            'defender_health_post': self.defender_health_post,
        }

            
        
        