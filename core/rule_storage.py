import json
import os

CUSTOM_RULES_FILE = os.path.join("data", "custom_rules.json")

def ensure_file_exists():
    os.makedirs("data", exist_ok=True)

    # If file missing or blank → rewrite with {}
    if not os.path.exists(CUSTOM_RULES_FILE) or os.path.getsize(CUSTOM_RULES_FILE) == 0:
        with open(CUSTOM_RULES_FILE, "w") as f:
            json.dump({}, f, indent=4)


def load_custom_rules() -> dict:
    ensure_file_exists()

    try:
        with open(CUSTOM_RULES_FILE, "r") as f:
            data = json.load(f)

            # If data isn’t a dict (corrupted), reset it
            if not isinstance(data, dict):
                raise ValueError("Invalid JSON structure.")

            return data

    except (json.JSONDecodeError, ValueError):
        # Rewrite invalid file to empty dict
        with open(CUSTOM_RULES_FILE, "w") as f:
            json.dump({}, f, indent=4)
        return {}


def save_custom_rule(name: str, rule: dict):
    rules = load_custom_rules()
    rules[name] = rule
    with open(CUSTOM_RULES_FILE, "w") as f:
        json.dump(rules, f, indent=4)


def delete_custom_rule(name: str):
    rules = load_custom_rules()
    if name in rules:
        del rules[name]
        with open(CUSTOM_RULES_FILE, "w") as f:
            json.dump(rules, f, indent=4)


custom_rules = load_custom_rules()