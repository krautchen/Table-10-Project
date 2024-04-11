def attack(self,target):
    """Generic attack

    Returns:
        str: Total damage or non-damage
    Side effects:
        Possibly modifies the target's hp
    """
    if d6(self.dexterity)+self.dexterity > d6(target.defense):
        damage = (d6(self.strength)) * self.weapon.damage
        total_damage = damage - self.armor.armor_value
        if total_damage > 0:
            target.take_damage(total_damage)
            return print(f"{self.name} attacks {target.name} for "+
                         "{total_damage} damage.")
        else:
            print(f"{self.name} fails to damage {target.name}. "+
                    f"{target.name}'s armor is too tough")