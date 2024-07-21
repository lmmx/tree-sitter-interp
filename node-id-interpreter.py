import re
from typing import Dict, List, Optional


class NodeInfo:
    def __init__(self, id: int, kind: str, named: bool, hidden: bool, visible: bool):
        self.id = id
        self.kind = kind
        self.named = named
        self.hidden = hidden
        self.visible = visible


class NodeType:
    def __init__(self, type_name: str, fields: Dict[str, str], subtypes: List[str]):
        self.type_name = type_name
        self.fields = fields
        self.subtypes = subtypes


class GrammarRule:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content


class NodeInterpreter:
    def __init__(self, node_ids_file: str, node_types_file: str, grammar_file: str):
        self.node_ids: Dict[int, NodeInfo] = self._parse_node_ids(node_ids_file)
        self.node_types: Dict[str, NodeType] = self._parse_node_types(node_types_file)
        self.grammar_rules: Dict[str, GrammarRule] = self._parse_grammar(grammar_file)

    def _parse_node_ids(self, filename: str) -> Dict[int, NodeInfo]:
        node_ids = {}
        with open(filename, "r") as file:
            for line in file:
                parsed_line = self._parse_line(line.strip())
                if parsed_line:
                    node_ids[parsed_line["index"]] = NodeInfo(
                        parsed_line["index"],
                        parsed_line["kind"],
                        parsed_line["named"],
                        parsed_line["hidden"],
                        parsed_line["visible"],
                    )
        return node_ids

    def _parse_node_types(self, filename: str) -> Dict[str, NodeType]:
        node_types = {}
        current_type = None
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("## "):
                    if current_type:
                        node_types[current_type.type_name] = current_type
                    type_name = re.sub(r"^\d+\)\s*", "", line[3:].strip())
                    current_type = NodeType(type_name, {}, [])
                elif 'type="FIELD"' in line and current_type:
                    field_match = re.search(r'name="(\w+)".*content=(\w+)', line)
                    if field_match:
                        current_type.fields[field_match.group(1)] = field_match.group(2)
                elif 'type="SYMBOL"' in line and current_type:
                    subtype_match = re.search(r'name="(\w+)"', line)
                    if subtype_match:
                        current_type.subtypes.append(subtype_match.group(1))
        if current_type:
            node_types[current_type.type_name] = current_type
        return node_types

    def _parse_grammar(self, filename: str) -> Dict[str, GrammarRule]:
        grammar_rules = {}
        current_rule = None
        in_rules_section = False
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("## Rules"):
                    in_rules_section = True
                elif line.startswith("##") and in_rules_section:
                    if not line.startswith("###"):
                        break  # Exit when a new section starts after the Rules section
                if in_rules_section:
                    if line.startswith("### "):
                        if current_rule:
                            grammar_rules[current_rule.name] = current_rule
                        rule_name = re.sub(r"^\d+\)\s*", "", line[4:].strip())
                        current_rule = GrammarRule(rule_name, "")
                    elif current_rule and line:
                        current_rule.content += line + "\n"
        if current_rule:
            grammar_rules[current_rule.name] = current_rule
        return grammar_rules

    def interpret_node_id(self, node_id: int) -> Optional[str]:
        node_info = self.node_ids.get(node_id)
        if not node_info:
            return None

        interpretation = f"Node ID: {node_id}\n"
        interpretation += f' - Kind: "{node_info.kind}", '
        interpretation += f"Named: {node_info.named}, "
        interpretation += f"Hidden: {node_info.hidden}, "
        interpretation += f"Visible: {node_info.visible}\n"

        node_type = self.node_types.get(node_info.kind)
        if node_type:
            interpretation += f' - Type: "{node_type.type_name}"\n'
            if node_type.fields:
                interpretation += "Fields:\n"
                for field, content in node_type.fields.items():
                    interpretation += f"  - {field}: {content}\n"
            if node_type.subtypes:
                interpretation += "Subtypes:\n"
                for subtype in node_type.subtypes:
                    interpretation += f"  - {subtype}\n"
        else:
            interpretation += " - Type: not found\n"

        grammar_rule = self.grammar_rules.get(node_info.kind)
        if grammar_rule:
            interpretation += f" - Rule:\n\n{grammar_rule.content}"
        else:
            interpretation += " - Rule: not found.\n"

        return interpretation

    @staticmethod
    def _parse_line(line: str):
        pattern = re.compile(
            r"(?P<index>\d+):\s*kind=(?P<kind>[^,]+),\s*named=(?P<named>\w+),\s*hidden=(?P<hidden>\w+),\s*visible=(?P<visible>\w+)"
        )
        match = pattern.match(line)
        if match:
            return {
                "index": int(match.group("index")),
                "kind": match.group("kind"),
                "named": match.group("named") == "true",
                "hidden": match.group("hidden") == "true",
                "visible": match.group("visible") == "visible",
            }
        else:
            return None


# Usage
interpreter = NodeInterpreter("python.txt", "python-nodes.md", "python-grammar.md")

# Example usage
for node_id in range(274):
    result = interpreter.interpret_node_id(node_id)
    if result:
        print(result)
    else:
        print(f"No information found for node ID {node_id}")
