class Attack:
    def __init__(self, attacker, defender):
        

        self.payload = attacker.get_damage() - defender.get_defense()

        self.defender_health_pre = defender.get_health()
        self.defender_health_post = self.defender_health_pre

        self.attack(defender)

        self.log_combat = {
            'attacker': attacker.get_name(),
            'defender': defender.get_name(),
            'damage': self.payload,
            'defender_health_pre': self.defender_health_pre,
            'defender_health_post': self.defender_health_post,
        }

    def attack(self, defender):
        self.defender_health_post = self.defender_health_pre - self.payload
        defender.modify_health(-self.payload)
        #is this where death check should go?
        
        defender.death_check()


            
        
        