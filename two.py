class Rule:
    def __init__(self, antecedents, consequent):
        self.antecedents = set(antecedents)
        self.consequent = consequent

def forward_chaining(rules, initial_facts, goal):
    known_facts = set(initial_facts)
    fired_rules = []
    
    print("Initial Known Facts:", sorted(list(known_facts)))
    print("Target Goal:", goal)
    print("=" * 50)
    
    changed = True
    step = 1
    while changed:
        changed = False
        for rule in rules:
            if rule not in fired_rules:
                if rule.antecedents.issubset(known_facts):
                    fired_rules.append(rule)
                    if rule.consequent not in known_facts:
                        known_facts.add(rule.consequent)
                        changed = True
                        print(f"Step {step}: Rule Fired: IF {' AND '.join(rule.antecedents)} THEN '{rule.consequent}'")
                        print(f"       -> Added Fact: '{rule.consequent}'")
                        step += 1
                        if rule.consequent == goal:
                            print("=" * 50)
                            print(f"Goal '{goal}' successfully inferred!")
                            return True, known_facts
    print("=" * 50)
    if goal in known_facts:
        print(f"Goal '{goal}' is satisfied.")
        return True, known_facts
    else:
        print(f"Goal '{goal}' could not be inferred.")
        return False, known_facts

def main():
    rules = [
        Rule(['has_feathers'], 'bird'),
        Rule(['lays_eggs', 'has_wings'], 'bird'),
        Rule(['bird', 'swims', 'cannot_fly'], 'penguin'),
        Rule(['penguin'], 'arctic_animal'),
        Rule(['bird', 'can_fly', 'eats_fish'], 'seagull')
    ]
    
    initial_facts = ['lays_eggs', 'has_wings', 'cannot_fly', 'swims']
    goal = 'arctic_animal'
    
    print("Forward Chaining Inference Engine")
    success, final_facts = forward_chaining(rules, initial_facts, goal)
    print("Final Knowledge Base Facts:", sorted(list(final_facts)))
    print("Inference Result:", "SUCCESS" if success else "FAILURE")

if __name__ == '__main__':
    main()
