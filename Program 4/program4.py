# Program 4: Representation of Knowledge Using Predicate Logic
# and Rule-Based Systems
#
# Concepts: Knowledge Representation, Rules, Forward Chaining

class RuleBasedSystem:
    def __init__(self, facts, rules):
        self.facts = set(facts)
        self.rules = rules

    def forward_chain(self):
        iterations = 0

        while True:
            new_fact_added = False

            for rule in self.rules:
                # Check if all conditions of the rule exist in current facts
                if all(condition in self.facts for condition in rule["if"]):

                    # Add the conclusion if it is not already present
                    if rule["then"] not in self.facts:
                        print(
                            f"Rule Triggered: IF {rule['if']} "
                            f"THEN Add {rule['then']}"
                        )

                        self.facts.add(rule["then"])
                        new_fact_added = True

            # Stop when no new fact can be derived
            if not new_fact_added:
                break

            iterations += 1

        print(f"\nForward chaining completed in {iterations} iteration(s).")
        return self.facts


# Example Usage
if __name__ == "__main__":

    # Initial facts
    initial_facts = [
        "Socrates_is_human",
        "All_humans_are_mortal"
    ]

    # Production rules
    production_rules = [
        {
            "if": [
                "Socrates_is_human",
                "All_humans_are_mortal"
            ],
            "then": "Socrates_is_mortal"
        }
    ]

    # Create the rule-based system
    rbs = RuleBasedSystem(initial_facts, production_rules)

    # Display initial facts
    print("Initial Knowledge Base:")
    for fact in sorted(initial_facts):
        print("-", fact)

    print("\nApplying Rules...\n")

    # Perform forward chaining
    final_kb = rbs.forward_chain()

    # Display final knowledge base
    print("\nFinal Knowledge Base Facts:")
    for fact in sorted(final_kb):
        print("-", fact)