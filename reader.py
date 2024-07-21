import re


def parse_line(line):
    # Define the regex pattern for each line
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
            "visible": match.group("visible") == "true",
        }
    else:
        return None


def read_file(file_path):
    parsed_data = []
    with open(file_path, "r") as file:
        for line in file:
            parsed_line = parse_line(line.strip())
            if parsed_line:
                parsed_data.append(parsed_line)
    return parsed_data


# Example usage
file_path = "python.txt"
data = read_file(file_path)
for entry in data:
    print(entry)
