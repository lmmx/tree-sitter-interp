Node ID: 0
 - Kind: "end", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 1
 - Kind: "identifier", Named: True, Hidden: False, Visible: False
 - Type: "identifier"
 - Rule:

```py
PatternRule(
type="PATTERN",
value="[_\\p{XID_Start}][_\\p{XID_Continue}]*",
flags=None,
)
```

Node ID: 2
 - Kind: ";", Named: False, Hidden: False, Visible: False
 - Type: ";"
 - Rule: not found.

Node ID: 3
 - Kind: "import", Named: False, Hidden: False, Visible: False
 - Type: "import"
 - Rule: not found.

Node ID: 4
 - Kind: ".", Named: False, Hidden: False, Visible: False
 - Type: "."
 - Rule: not found.

Node ID: 5
 - Kind: "from", Named: False, Hidden: False, Visible: False
 - Type: "from"
 - Rule: not found.

Node ID: 6
 - Kind: "__future__", Named: False, Hidden: True, Visible: False
 - Type: "__future__"
 - Rule: not found.

Node ID: 7
 - Kind: "(", Named: False, Hidden: False, Visible: False
 - Type: "("
 - Rule: not found.

Node ID: 8
 - Kind: ")", Named: False, Hidden: False, Visible: False
 - Type: ")"
 - Rule: not found.

No information found for node ID 9
Node ID: 10
 - Kind: "as", Named: False, Hidden: False, Visible: False
 - Type: "as"
 - Rule: not found.

Node ID: 11
 - Kind: "*", Named: False, Hidden: False, Visible: False
 - Type: "*"
 - Rule: not found.

Node ID: 12
 - Kind: "print", Named: False, Hidden: False, Visible: False
 - Type: "print"
 - Rule: not found.

Node ID: 13
 - Kind: ">>", Named: False, Hidden: False, Visible: False
 - Type: ">>"
 - Rule: not found.

Node ID: 14
 - Kind: "assert", Named: False, Hidden: False, Visible: False
 - Type: "assert"
 - Rule: not found.

Node ID: 15
 - Kind: ":=", Named: False, Hidden: False, Visible: False
 - Type: ":="
 - Rule: not found.

Node ID: 16
 - Kind: "return", Named: False, Hidden: False, Visible: False
 - Type: "return"
 - Rule: not found.

Node ID: 17
 - Kind: "del", Named: False, Hidden: False, Visible: False
 - Type: "del"
 - Rule: not found.

Node ID: 18
 - Kind: "raise", Named: False, Hidden: False, Visible: False
 - Type: "raise"
 - Rule: not found.

Node ID: 19
 - Kind: "pass", Named: False, Hidden: False, Visible: False
 - Type: "pass"
 - Rule: not found.

Node ID: 20
 - Kind: "break", Named: False, Hidden: False, Visible: False
 - Type: "break"
 - Rule: not found.

Node ID: 21
 - Kind: "continue", Named: False, Hidden: False, Visible: False
 - Type: "continue"
 - Rule: not found.

Node ID: 22
 - Kind: "if", Named: False, Hidden: False, Visible: False
 - Type: "if"
 - Rule: not found.

Node ID: 23
 - Kind: ":", Named: False, Hidden: False, Visible: False
 - Type: ":"
 - Rule: not found.

Node ID: 24
 - Kind: "elif", Named: False, Hidden: False, Visible: False
 - Type: "elif"
 - Rule: not found.

Node ID: 25
 - Kind: "else", Named: False, Hidden: False, Visible: False
 - Type: "else"
 - Rule: not found.

Node ID: 26
 - Kind: "match", Named: False, Hidden: False, Visible: False
 - Type: "match"
 - Rule: not found.

Node ID: 27
 - Kind: "case", Named: False, Hidden: False, Visible: False
 - Type: "case"
 - Rule: not found.

Node ID: 28
 - Kind: "async", Named: False, Hidden: False, Visible: False
 - Type: "async"
 - Rule: not found.

Node ID: 29
 - Kind: "for", Named: False, Hidden: False, Visible: False
 - Type: "for"
 - Rule: not found.

Node ID: 30
 - Kind: "in", Named: False, Hidden: False, Visible: False
 - Type: "in"
 - Rule: not found.

Node ID: 31
 - Kind: "while", Named: False, Hidden: False, Visible: False
 - Type: "while"
 - Rule: not found.

Node ID: 32
 - Kind: "try", Named: False, Hidden: False, Visible: False
 - Type: "try"
 - Rule: not found.

Node ID: 33
 - Kind: "except", Named: False, Hidden: False, Visible: False
 - Type: "except"
 - Rule: not found.

Node ID: 34
 - Kind: "except*", Named: False, Hidden: False, Visible: False
 - Type: "except*"
 - Rule: not found.

Node ID: 35
 - Kind: "finally", Named: False, Hidden: False, Visible: False
 - Type: "finally"
 - Rule: not found.

Node ID: 36
 - Kind: "with", Named: False, Hidden: False, Visible: False
 - Type: "with"
 - Rule: not found.

Node ID: 37
 - Kind: "def", Named: False, Hidden: False, Visible: False
 - Type: "def"
 - Rule: not found.

Node ID: 38
 - Kind: "->", Named: False, Hidden: False, Visible: False
 - Type: "->"
 - Rule: not found.

Node ID: 39
 - Kind: "**", Named: False, Hidden: False, Visible: False
 - Type: "**"
 - Rule: not found.

Node ID: 40
 - Kind: "global", Named: False, Hidden: False, Visible: False
 - Type: "global"
 - Rule: not found.

Node ID: 41
 - Kind: "nonlocal", Named: False, Hidden: False, Visible: False
 - Type: "nonlocal"
 - Rule: not found.

Node ID: 42
 - Kind: "exec", Named: False, Hidden: False, Visible: False
 - Type: "exec"
 - Rule: not found.

Node ID: 43
 - Kind: "type", Named: False, Hidden: False, Visible: False
 - Type: "type"
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="expression"),
SymbolRule(type="SYMBOL", name="splat_type"),
SymbolRule(type="SYMBOL", name="generic_type"),
SymbolRule(type="SYMBOL", name="union_type"),
SymbolRule(type="SYMBOL", name="constrained_type"),
SymbolRule(type="SYMBOL", name="member_type"),
],
)
```

Node ID: 44
 - Kind: "=", Named: False, Hidden: False, Visible: False
 - Type: "="
 - Rule: not found.

Node ID: 45
 - Kind: "class", Named: False, Hidden: False, Visible: False
 - Type: "class"
 - Rule: not found.

Node ID: 46
 - Kind: "[", Named: False, Hidden: False, Visible: False
 - Type: "["
 - Rule: not found.

Node ID: 47
 - Kind: "]", Named: False, Hidden: False, Visible: False
 - Type: "]"
 - Rule: not found.

Node ID: 48
 - Kind: "@", Named: False, Hidden: False, Visible: False
 - Type: "@"
 - Rule: not found.

Node ID: 49
 - Kind: "-", Named: False, Hidden: False, Visible: False
 - Type: "-"
 - Rule: not found.

Node ID: 50
 - Kind: "_", Named: False, Hidden: True, Visible: False
 - Type: "_"
 - Rule: not found.

Node ID: 51
 - Kind: "|", Named: False, Hidden: False, Visible: False
 - Type: "|"
 - Rule: not found.

Node ID: 52
 - Kind: "{", Named: False, Hidden: False, Visible: False
 - Type: "{"
 - Rule: not found.

Node ID: 53
 - Kind: "}", Named: False, Hidden: False, Visible: False
 - Type: "}"
 - Rule: not found.

Node ID: 54
 - Kind: "+", Named: False, Hidden: False, Visible: False
 - Type: "+"
 - Rule: not found.

Node ID: 55
 - Kind: "not", Named: False, Hidden: False, Visible: False
 - Type: "not"
 - Rule: not found.

Node ID: 56
 - Kind: "and", Named: False, Hidden: False, Visible: False
 - Type: "and"
 - Rule: not found.

Node ID: 57
 - Kind: "or", Named: False, Hidden: False, Visible: False
 - Type: "or"
 - Rule: not found.

Node ID: 58
 - Kind: "/", Named: False, Hidden: False, Visible: False
 - Type: "/"
 - Rule: not found.

Node ID: 59
 - Kind: "%", Named: False, Hidden: False, Visible: False
 - Type: "%"
 - Rule: not found.

Node ID: 60
 - Kind: "//", Named: False, Hidden: False, Visible: False
 - Type: "//"
 - Rule: not found.

Node ID: 61
 - Kind: "&", Named: False, Hidden: False, Visible: False
 - Type: "&"
 - Rule: not found.

Node ID: 62
 - Kind: "^", Named: False, Hidden: False, Visible: False
 - Type: "^"
 - Rule: not found.

Node ID: 63
 - Kind: "<<", Named: False, Hidden: False, Visible: False
 - Type: "<<"
 - Rule: not found.

Node ID: 64
 - Kind: "~", Named: False, Hidden: False, Visible: False
 - Type: "~"
 - Rule: not found.

Node ID: 65
 - Kind: "<", Named: False, Hidden: False, Visible: False
 - Type: "<"
 - Rule: not found.

Node ID: 66
 - Kind: "<=", Named: False, Hidden: False, Visible: False
 - Type: "<="
 - Rule: not found.

Node ID: 67
 - Kind: "==", Named: False, Hidden: False, Visible: False
 - Type: "=="
 - Rule: not found.

Node ID: 68
 - Kind: "!=", Named: False, Hidden: False, Visible: False
 - Type: "!="
 - Rule: not found.

Node ID: 69
 - Kind: ">=", Named: False, Hidden: False, Visible: False
 - Type: ">="
 - Rule: not found.

Node ID: 70
 - Kind: ">", Named: False, Hidden: False, Visible: False
 - Type: ">"
 - Rule: not found.

Node ID: 71
 - Kind: "<>", Named: False, Hidden: False, Visible: False
 - Type: "<>"
 - Rule: not found.

Node ID: 72
 - Kind: "is", Named: False, Hidden: False, Visible: False
 - Type: "is"
 - Rule: not found.

Node ID: 73
 - Kind: "lambda", Named: False, Hidden: False, Visible: False
 - Type: "lambda"
 - Rule:

```py
PrecRule(
type="PREC",
value=-2,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="lambda"),
FieldRule(
name="parameters",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="lambda_parameters"
),
BlankRule(type="BLANK"),
],
),
),
StringRule(type="STRING", value=":"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
],
),
)
```

Node ID: 74
 - Kind: "+=", Named: False, Hidden: False, Visible: False
 - Type: "+="
 - Rule: not found.

Node ID: 75
 - Kind: "-=", Named: False, Hidden: False, Visible: False
 - Type: "-="
 - Rule: not found.

Node ID: 76
 - Kind: "*=", Named: False, Hidden: False, Visible: False
 - Type: "*="
 - Rule: not found.

Node ID: 77
 - Kind: "/=", Named: False, Hidden: False, Visible: False
 - Type: "/="
 - Rule: not found.

Node ID: 78
 - Kind: "@=", Named: False, Hidden: False, Visible: False
 - Type: "@="
 - Rule: not found.

Node ID: 79
 - Kind: "//=", Named: False, Hidden: False, Visible: False
 - Type: "//="
 - Rule: not found.

Node ID: 80
 - Kind: "%=", Named: False, Hidden: False, Visible: False
 - Type: "%="
 - Rule: not found.

Node ID: 81
 - Kind: "**=", Named: False, Hidden: False, Visible: False
 - Type: "**="
 - Rule: not found.

Node ID: 82
 - Kind: ">>=", Named: False, Hidden: False, Visible: False
 - Type: ">>="
 - Rule: not found.

Node ID: 83
 - Kind: "<<=", Named: False, Hidden: False, Visible: False
 - Type: "<<="
 - Rule: not found.

Node ID: 84
 - Kind: "&=", Named: False, Hidden: False, Visible: False
 - Type: "&="
 - Rule: not found.

Node ID: 85
 - Kind: "^=", Named: False, Hidden: False, Visible: False
 - Type: "^="
 - Rule: not found.

Node ID: 86
 - Kind: "|=", Named: False, Hidden: False, Visible: False
 - Type: "|="
 - Rule: not found.

Node ID: 87
 - Kind: "yield", Named: False, Hidden: False, Visible: False
 - Type: "yield"
 - Rule:

```py
PrecRule(
type="PREC_RIGHT",
value=0,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="yield"),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="from"),
SymbolRule(
type="SYMBOL", name="expression"
),
],
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="_expressions"
),
BlankRule(type="BLANK"),
],
),
],
),
],
),
)
```

Node ID: 88
 - Kind: "ellipsis", Named: True, Hidden: False, Visible: False
 - Type: "ellipsis"
 - Rule:

```py
StringRule(type="STRING", value="...")
```

Node ID: 89
 - Kind: "escape_sequence", Named: True, Hidden: False, Visible: False
 - Type: "escape_sequence"
 - Rule:

```py
TokenRule(
type="IMMEDIATE_TOKEN",
content=PrecRule(
type="PREC",
value=1,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="\\"),
ChoiceRule(
type="CHOICE",
members=[
PatternRule(
type="PATTERN",
value="u[a-fA-F\\d]{4}",
flags=None,
),
PatternRule(
type="PATTERN",
value="U[a-fA-F\\d]{8}",
flags=None,
),
PatternRule(
type="PATTERN",
value="x[a-fA-F\\d]{2}",
flags=None,
),
PatternRule(
type="PATTERN",
value="\\d{1,3}",
flags=None,
),
PatternRule(
type="PATTERN",
value="\\r?\\n",
flags=None,
),
PatternRule(
type="PATTERN",
value="['\"abfrntv\\\\]",
flags=None,
),
PatternRule(
type="PATTERN",
value="N\\{[^}]+\\}",
flags=None,
),
],
),
],
),
),
)
```

Node ID: 90
 - Kind: "_not_escape_sequence", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
TokenRule(
type="IMMEDIATE_TOKEN",
content=StringRule(type="STRING", value="\\"),
)
```

Node ID: 91
 - Kind: "format_specifier_token1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 92
 - Kind: "type_conversion", Named: True, Hidden: False, Visible: False
 - Type: "type_conversion"
 - Rule:

```py
PatternRule(type="PATTERN", value="![a-z]", flags=None)
```

Node ID: 93
 - Kind: "integer", Named: True, Hidden: False, Visible: False
 - Type: "integer"
 - Rule:

```py
TokenRule(
type="TOKEN",
content=ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="0x"),
StringRule(type="STRING", value="0X"),
],
),
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="_?[A-Fa-f0-9]+",
flags=None,
),
),
ChoiceRule(
type="CHOICE",
members=[
PatternRule(
type="PATTERN",
value="[Ll]",
flags=None,
),
BlankRule(type="BLANK"),
],
),
],
),
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="0o"),
StringRule(type="STRING", value="0O"),
],
),
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="_?[0-7]+",
flags=None,
),
),
ChoiceRule(
type="CHOICE",
members=[
PatternRule(
type="PATTERN",
value="[Ll]",
flags=None,
),
BlankRule(type="BLANK"),
],
),
],
),
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="0b"),
StringRule(type="STRING", value="0B"),
],
),
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="_?[0-1]+",
flags=None,
),
),
ChoiceRule(
type="CHOICE",
members=[
PatternRule(
type="PATTERN",
value="[Ll]",
flags=None,
),
BlankRule(type="BLANK"),
],
),
],
),
SeqRule(
type="SEQ",
members=[
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="[0-9]+_?",
flags=None,
),
),
ChoiceRule(
type="CHOICE",
members=[
ChoiceRule(
type="CHOICE",
members=[
PatternRule(
type="PATTERN",
value="[Ll]",
flags=None,
),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
PatternRule(
type="PATTERN",
value="[jJ]",
flags=None,
),
BlankRule(type="BLANK"),
],
),
],
),
],
),
],
),
)
```

Node ID: 94
 - Kind: "float", Named: True, Hidden: False, Visible: False
 - Type: "float"
 - Rule:

```py
TokenRule(
type="TOKEN",
content=SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="[0-9]+_?",
flags=None,
),
),
StringRule(type="STRING", value="."),
ChoiceRule(
type="CHOICE",
members=[
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="[0-9]+_?",
flags=None,
),
),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
PatternRule(
type="PATTERN",
value="[eE][\\+-]?",
flags=None,
),
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="[0-9]+_?",
flags=None,
),
),
],
),
BlankRule(type="BLANK"),
],
),
],
),
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="[0-9]+_?",
flags=None,
),
),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="."),
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="[0-9]+_?",
flags=None,
),
),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
PatternRule(
type="PATTERN",
value="[eE][\\+-]?",
flags=None,
),
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="[0-9]+_?",
flags=None,
),
),
],
),
BlankRule(type="BLANK"),
],
),
],
),
SeqRule(
type="SEQ",
members=[
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="[0-9]+_?",
flags=None,
),
),
SeqRule(
type="SEQ",
members=[
PatternRule(
type="PATTERN",
value="[eE][\\+-]?",
flags=None,
),
Repeat1Rule(
type="REPEAT1",
content=PatternRule(
type="PATTERN",
value="[0-9]+_?",
flags=None,
),
),
],
),
],
),
],
),
ChoiceRule(
type="CHOICE",
members=[
PatternRule(
type="PATTERN", value="[jJ]", flags=None
),
BlankRule(type="BLANK"),
],
),
],
),
)
```

Node ID: 95
 - Kind: "await", Named: False, Hidden: False, Visible: False
 - Type: "await"
 - Rule:

```py
PrecRule(
type="PREC",
value=20,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="await"),
SymbolRule(type="SYMBOL", name="primary_expression"),
],
),
)
```

Node ID: 96
 - Kind: "true", Named: True, Hidden: False, Visible: False
 - Type: "true"
 - Rule:

```py
StringRule(type="STRING", value="True")
```

Node ID: 97
 - Kind: "false", Named: True, Hidden: False, Visible: False
 - Type: "false"
 - Rule:

```py
StringRule(type="STRING", value="False")
```

Node ID: 98
 - Kind: "none", Named: True, Hidden: False, Visible: False
 - Type: "none"
 - Rule:

```py
StringRule(type="STRING", value="None")
```

Node ID: 99
 - Kind: "comment", Named: True, Hidden: False, Visible: False
 - Type: "comment"
 - Rule:

```py
TokenRule(
type="TOKEN",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="#"),
PatternRule(type="PATTERN", value=".*", flags=None),
],
),
)
```

Node ID: 100
 - Kind: "line_continuation", Named: True, Hidden: False, Visible: False
 - Type: "line_continuation"
 - Rule:

```py
TokenRule(
type="TOKEN",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="\\"),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(
type="STRING", value="\r"
),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="\n"),
],
),
StringRule(type="STRING", value="\x00"),
],
),
],
),
)
```

Node ID: 101
 - Kind: "_newline", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 102
 - Kind: "_indent", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 103
 - Kind: "_dedent", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 104
 - Kind: "string_start", Named: True, Hidden: False, Visible: False
 - Type: "string_start"
 - Rule: not found.

Node ID: 105
 - Kind: "_string_content", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 106
 - Kind: "escape_interpolation", Named: True, Hidden: False, Visible: False
 - Type: "escape_interpolation"
 - Rule: not found.

Node ID: 107
 - Kind: "string_end", Named: True, Hidden: False, Visible: False
 - Type: "string_end"
 - Rule: not found.

Node ID: 108
 - Kind: "module", Named: True, Hidden: False, Visible: False
 - Type: "module"
 - Rule:

```py
RepeatRule(
type="REPEAT",
content=SymbolRule(type="SYMBOL", name="_statement"),
)
```

Node ID: 109
 - Kind: "_statement", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="_simple_statements"),
SymbolRule(type="SYMBOL", name="_compound_statement"),
],
)
```

Node ID: 110
 - Kind: "_simple_statements", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="_simple_statement"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=";"),
SymbolRule(
type="SYMBOL",
name="_simple_statement",
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=";"),
BlankRule(type="BLANK"),
],
),
SymbolRule(type="SYMBOL", name="_newline"),
],
)
```

Node ID: 111
 - Kind: "import_statement", Named: True, Hidden: False, Visible: False
 - Type: "import_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="import"),
SymbolRule(type="SYMBOL", name="_import_list"),
],
)
```

Node ID: 112
 - Kind: "import_prefix", Named: True, Hidden: False, Visible: False
 - Type: "import_prefix"
 - Rule:

```py
Repeat1Rule(
type="REPEAT1", content=StringRule(type="STRING", value=".")
)
```

Node ID: 113
 - Kind: "relative_import", Named: True, Hidden: False, Visible: False
 - Type: "relative_import"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="import_prefix"),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="dotted_name"),
BlankRule(type="BLANK"),
],
),
],
)
```

Node ID: 114
 - Kind: "future_import_statement", Named: True, Hidden: False, Visible: False
 - Type: "future_import_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="from"),
StringRule(type="STRING", value="__future__"),
StringRule(type="STRING", value="import"),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="_import_list"),
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="("),
SymbolRule(
type="SYMBOL", name="_import_list"
),
StringRule(type="STRING", value=")"),
],
),
],
),
],
)
```

Node ID: 115
 - Kind: "import_from_statement", Named: True, Hidden: False, Visible: False
 - Type: "import_from_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="from"),
FieldRule(
name="module_name",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="relative_import"),
SymbolRule(type="SYMBOL", name="dotted_name"),
],
),
),
StringRule(type="STRING", value="import"),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="wildcard_import"),
SymbolRule(type="SYMBOL", name="_import_list"),
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="("),
SymbolRule(
type="SYMBOL", name="_import_list"
),
StringRule(type="STRING", value=")"),
],
),
],
),
],
)
```

Node ID: 116
 - Kind: "_import_list", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SeqRule(
type="SEQ",
members=[
FieldRule(
name="name",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="dotted_name"
),
SymbolRule(
type="SYMBOL", name="aliased_import"
),
],
),
),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
FieldRule(
name="name",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL",
name="dotted_name",
),
SymbolRule(
type="SYMBOL",
name="aliased_import",
),
],
),
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
)
```

Node ID: 117
 - Kind: "aliased_import", Named: True, Hidden: False, Visible: False
 - Type: "aliased_import"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
FieldRule(
name="name",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="dotted_name"),
),
StringRule(type="STRING", value="as"),
FieldRule(
name="alias",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="identifier"),
),
],
)
```

Node ID: 118
 - Kind: "wildcard_import", Named: True, Hidden: False, Visible: False
 - Type: "wildcard_import"
 - Rule:

```py
StringRule(type="STRING", value="*")
```

Node ID: 119
 - Kind: "print_statement", Named: True, Hidden: False, Visible: False
 - Type: "print_statement"
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
PrecRule(
type="PREC",
value=1,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="print"),
SymbolRule(type="SYMBOL", name="chevron"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
FieldRule(
name="argument",
type="FIELD",
content=SymbolRule(
type="SYMBOL",
name="expression",
),
),
],
),
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
),
),
PrecRule(
type="PREC",
value=-3,
content=PrecRule(
type="PREC_DYNAMIC",
value=-1,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="print"),
SeqRule(
type="SEQ",
members=[
FieldRule(
name="argument",
type="FIELD",
content=SymbolRule(
type="SYMBOL",
name="expression",
),
),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING",
value=",",
),
FieldRule(
name="argument",
type="FIELD",
content=SymbolRule(
type="SYMBOL",
name="expression",
),
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
),
),
),
],
)
```

Node ID: 120
 - Kind: "chevron", Named: True, Hidden: False, Visible: False
 - Type: "chevron"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=">>"),
SymbolRule(type="SYMBOL", name="expression"),
],
)
```

Node ID: 121
 - Kind: "assert_statement", Named: True, Hidden: False, Visible: False
 - Type: "assert_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="assert"),
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="expression"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
SymbolRule(
type="SYMBOL", name="expression"
),
],
),
),
],
),
],
)
```

Node ID: 122
 - Kind: "expression_statement", Named: True, Hidden: False, Visible: False
 - Type: "expression_statement"
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="expression"),
SeqRule(
type="SEQ",
members=[
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="expression"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING", value=","
),
SymbolRule(
type="SYMBOL",
name="expression",
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
),
SymbolRule(type="SYMBOL", name="assignment"),
SymbolRule(type="SYMBOL", name="augmented_assignment"),
SymbolRule(type="SYMBOL", name="yield"),
],
)
```

Node ID: 123
 - Kind: "named_expression", Named: True, Hidden: False, Visible: False
 - Type: "named_expression"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
FieldRule(
name="name",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="_named_expression_lhs"
),
),
StringRule(type="STRING", value=":="),
FieldRule(
name="value",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
],
)
```

Node ID: 124
 - Kind: "_named_expression_lhs", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
SymbolRule(type="SYMBOL", name="keyword_identifier"),
],
)
```

Node ID: 125
 - Kind: "return_statement", Named: True, Hidden: False, Visible: False
 - Type: "return_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="return"),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="_expressions"),
BlankRule(type="BLANK"),
],
),
],
)
```

Node ID: 126
 - Kind: "delete_statement", Named: True, Hidden: False, Visible: False
 - Type: "delete_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="del"),
SymbolRule(type="SYMBOL", name="_expressions"),
],
)
```

Node ID: 127
 - Kind: "raise_statement", Named: True, Hidden: False, Visible: False
 - Type: "raise_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="raise"),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="_expressions"),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="from"),
FieldRule(
name="cause",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="expression"
),
),
],
),
BlankRule(type="BLANK"),
],
),
],
)
```

Node ID: 128
 - Kind: "pass_statement", Named: True, Hidden: False, Visible: False
 - Type: "pass_statement"
 - Rule:

```py
PrecRule(
type="PREC_LEFT",
value=0,
content=StringRule(type="STRING", value="pass"),
)
```

Node ID: 129
 - Kind: "break_statement", Named: True, Hidden: False, Visible: False
 - Type: "break_statement"
 - Rule:

```py
PrecRule(
type="PREC_LEFT",
value=0,
content=StringRule(type="STRING", value="break"),
)
```

Node ID: 130
 - Kind: "continue_statement", Named: True, Hidden: False, Visible: False
 - Type: "continue_statement"
 - Rule:

```py
PrecRule(
type="PREC_LEFT",
value=0,
content=StringRule(type="STRING", value="continue"),
)
```

Node ID: 131
 - Kind: "if_statement", Named: True, Hidden: False, Visible: False
 - Type: "if_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="if"),
FieldRule(
name="condition",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
StringRule(type="STRING", value=":"),
FieldRule(
name="consequence",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_suite"),
),
RepeatRule(
type="REPEAT",
content=FieldRule(
name="alternative",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="elif_clause"),
),
),
ChoiceRule(
type="CHOICE",
members=[
FieldRule(
name="alternative",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="else_clause"
),
),
BlankRule(type="BLANK"),
],
),
],
)
```

Node ID: 132
 - Kind: "elif_clause", Named: True, Hidden: False, Visible: False
 - Type: "elif_clause"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="elif"),
FieldRule(
name="condition",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
StringRule(type="STRING", value=":"),
FieldRule(
name="consequence",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_suite"),
),
],
)
```

Node ID: 133
 - Kind: "else_clause", Named: True, Hidden: False, Visible: False
 - Type: "else_clause"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="else"),
StringRule(type="STRING", value=":"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_suite"),
),
],
)
```

Node ID: 134
 - Kind: "match_statement", Named: True, Hidden: False, Visible: False
 - Type: "match_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="match"),
SeqRule(
type="SEQ",
members=[
FieldRule(
name="subject",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="expression"
),
),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
FieldRule(
name="subject",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="expression"
),
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=":"),
FieldRule(
name="body",
type="FIELD",
content=AliasRule(
type="ALIAS",
value="block",
named=True,
content=SymbolRule(
type="SYMBOL", name="_match_block"
),
),
),
],
)
```

Node ID: 135
 - Kind: "block", Named: True, Hidden: False, Visible: False
 - Type: "block"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
RepeatRule(
type="REPEAT",
content=SymbolRule(type="SYMBOL", name="_statement"),
),
SymbolRule(type="SYMBOL", name="_dedent"),
],
)
```

Node ID: 136
 - Kind: "case_clause", Named: True, Hidden: False, Visible: False
 - Type: "case_clause"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="case"),
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="case_pattern"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
SymbolRule(
type="SYMBOL", name="case_pattern"
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
FieldRule(
name="guard",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="if_clause"
),
),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=":"),
FieldRule(
name="consequence",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_suite"),
),
],
)
```

Node ID: 137
 - Kind: "for_statement", Named: True, Hidden: False, Visible: False
 - Type: "for_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="async"),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="for"),
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_left_hand_side"),
),
StringRule(type="STRING", value="in"),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_expressions"),
),
StringRule(type="STRING", value=":"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_suite"),
),
FieldRule(
name="alternative",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="else_clause"),
BlankRule(type="BLANK"),
],
),
),
],
)
```

Node ID: 138
 - Kind: "while_statement", Named: True, Hidden: False, Visible: False
 - Type: "while_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="while"),
FieldRule(
name="condition",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
StringRule(type="STRING", value=":"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_suite"),
),
ChoiceRule(
type="CHOICE",
members=[
FieldRule(
name="alternative",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="else_clause"
),
),
BlankRule(type="BLANK"),
],
),
],
)
```

Node ID: 139
 - Kind: "try_statement", Named: True, Hidden: False, Visible: False
 - Type: "try_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="try"),
StringRule(type="STRING", value=":"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_suite"),
),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
Repeat1Rule(
type="REPEAT1",
content=SymbolRule(
type="SYMBOL", name="except_clause"
),
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="else_clause"
),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL",
name="finally_clause",
),
BlankRule(type="BLANK"),
],
),
],
),
SeqRule(
type="SEQ",
members=[
Repeat1Rule(
type="REPEAT1",
content=SymbolRule(
type="SYMBOL",
name="except_group_clause",
),
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="else_clause"
),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL",
name="finally_clause",
),
BlankRule(type="BLANK"),
],
),
],
),
SymbolRule(type="SYMBOL", name="finally_clause"),
],
),
],
)
```

Node ID: 140
 - Kind: "except_clause", Named: True, Hidden: False, Visible: False
 - Type: "except_clause"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="except"),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="expression"),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(
type="STRING",
value="as",
),
StringRule(
type="STRING",
value=",",
),
],
),
SymbolRule(
type="SYMBOL",
name="expression",
),
],
),
BlankRule(type="BLANK"),
],
),
],
),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=":"),
SymbolRule(type="SYMBOL", name="_suite"),
],
)
```

Node ID: 141
 - Kind: "except_group_clause", Named: True, Hidden: False, Visible: False
 - Type: "except_group_clause"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="except*"),
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="expression"),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="as"),
SymbolRule(
type="SYMBOL", name="expression"
),
],
),
BlankRule(type="BLANK"),
],
),
],
),
StringRule(type="STRING", value=":"),
SymbolRule(type="SYMBOL", name="_suite"),
],
)
```

Node ID: 142
 - Kind: "finally_clause", Named: True, Hidden: False, Visible: False
 - Type: "finally_clause"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="finally"),
StringRule(type="STRING", value=":"),
SymbolRule(type="SYMBOL", name="_suite"),
],
)
```

Node ID: 143
 - Kind: "with_statement", Named: True, Hidden: False, Visible: False
 - Type: "with_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="async"),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="with"),
SymbolRule(type="SYMBOL", name="with_clause"),
StringRule(type="STRING", value=":"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_suite"),
),
],
)
```

Node ID: 144
 - Kind: "with_clause", Named: True, Hidden: False, Visible: False
 - Type: "with_clause"
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="with_item"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING", value=","
),
SymbolRule(
type="SYMBOL",
name="with_item",
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
),
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="("),
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="with_item"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING", value=","
),
SymbolRule(
type="SYMBOL",
name="with_item",
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=")"),
],
),
],
)
```

Node ID: 145
 - Kind: "with_item", Named: True, Hidden: False, Visible: False
 - Type: "with_item"
 - Rule:

```py
PrecRule(
type="PREC_DYNAMIC",
value=1,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="value",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
)
],
),
)
```

Node ID: 146
 - Kind: "function_definition", Named: True, Hidden: False, Visible: False
 - Type: "function_definition"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="async"),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="def"),
FieldRule(
name="name",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="identifier"),
),
FieldRule(
name="type_parameters",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="type_parameter"),
BlankRule(type="BLANK"),
],
),
),
FieldRule(
name="parameters",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="parameters"),
),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="->"),
FieldRule(
name="return_type",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="type"
),
),
],
),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=":"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_suite"),
),
],
)
```

Node ID: 147
 - Kind: "parameters", Named: True, Hidden: False, Visible: False
 - Type: "parameters"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="("),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="_parameters"),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=")"),
],
)
```

Node ID: 148
 - Kind: "lambda_parameters", Named: True, Hidden: False, Visible: False
 - Type: "lambda_parameters"
 - Rule:

```py
SymbolRule(type="SYMBOL", name="_parameters")
```

Node ID: 149
 - Kind: "list_splat", Named: True, Hidden: False, Visible: False
 - Type: "list_splat"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="*"),
SymbolRule(type="SYMBOL", name="expression"),
],
)
```

Node ID: 150
 - Kind: "dictionary_splat", Named: True, Hidden: False, Visible: False
 - Type: "dictionary_splat"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="**"),
SymbolRule(type="SYMBOL", name="expression"),
],
)
```

Node ID: 151
 - Kind: "global_statement", Named: True, Hidden: False, Visible: False
 - Type: "global_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="global"),
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
SymbolRule(
type="SYMBOL", name="identifier"
),
],
),
),
],
),
],
)
```

Node ID: 152
 - Kind: "nonlocal_statement", Named: True, Hidden: False, Visible: False
 - Type: "nonlocal_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="nonlocal"),
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
SymbolRule(
type="SYMBOL", name="identifier"
),
],
),
),
],
),
],
)
```

Node ID: 153
 - Kind: "exec_statement", Named: True, Hidden: False, Visible: False
 - Type: "exec_statement"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="exec"),
FieldRule(
name="code",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="string"),
SymbolRule(type="SYMBOL", name="identifier"),
],
),
),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="in"),
SeqRule(
type="SEQ",
members=[
SymbolRule(
type="SYMBOL", name="expression"
),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING",
value=",",
),
SymbolRule(
type="SYMBOL",
name="expression",
),
],
),
),
],
),
],
),
BlankRule(type="BLANK"),
],
),
],
)
```

Node ID: 154
 - Kind: "type_alias_statement", Named: True, Hidden: False, Visible: False
 - Type: "type_alias_statement"
 - Rule:

```py
PrecRule(
type="PREC_DYNAMIC",
value=1,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="type"),
SymbolRule(type="SYMBOL", name="type"),
StringRule(type="STRING", value="="),
SymbolRule(type="SYMBOL", name="type"),
],
),
)
```

Node ID: 155
 - Kind: "class_definition", Named: True, Hidden: False, Visible: False
 - Type: "class_definition"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="class"),
FieldRule(
name="name",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="identifier"),
),
FieldRule(
name="type_parameters",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="type_parameter"),
BlankRule(type="BLANK"),
],
),
),
FieldRule(
name="superclasses",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="argument_list"),
BlankRule(type="BLANK"),
],
),
),
StringRule(type="STRING", value=":"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_suite"),
),
],
)
```

Node ID: 156
 - Kind: "type_parameter", Named: True, Hidden: False, Visible: False
 - Type: "type_parameter"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="["),
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="type"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
SymbolRule(type="SYMBOL", name="type"),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="]"),
],
)
```

Node ID: 157
 - Kind: "parenthesized_list_splat", Named: True, Hidden: False, Visible: False
 - Type: "parenthesized_list_splat"
 - Rule:

```py
PrecRule(
type="PREC",
value=1,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="("),
ChoiceRule(
type="CHOICE",
members=[
AliasRule(
type="ALIAS",
value="parenthesized_expression",
named=True,
content=SymbolRule(
type="SYMBOL",
name="parenthesized_list_splat",
),
),
SymbolRule(type="SYMBOL", name="list_splat"),
],
),
StringRule(type="STRING", value=")"),
],
),
)
```

Node ID: 158
 - Kind: "argument_list", Named: True, Hidden: False, Visible: False
 - Type: "argument_list"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="("),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="expression"
),
SymbolRule(
type="SYMBOL", name="list_splat"
),
SymbolRule(
type="SYMBOL",
name="dictionary_splat",
),
AliasRule(
type="ALIAS",
value="parenthesized_expression",
named=True,
content=SymbolRule(
type="SYMBOL",
name="parenthesized_list_splat",
),
),
SymbolRule(
type="SYMBOL",
name="keyword_argument",
),
],
),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING", value=","
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL",
name="expression",
),
SymbolRule(
type="SYMBOL",
name="list_splat",
),
SymbolRule(
type="SYMBOL",
name="dictionary_splat",
),
AliasRule(
type="ALIAS",
value="parenthesized_expression",
named=True,
content=SymbolRule(
type="SYMBOL",
name="parenthesized_list_splat",
),
),
SymbolRule(
type="SYMBOL",
name="keyword_argument",
),
],
),
],
),
),
],
),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=")"),
],
)
```

Node ID: 159
 - Kind: "decorated_definition", Named: True, Hidden: False, Visible: False
 - Type: "decorated_definition"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
Repeat1Rule(
type="REPEAT1",
content=SymbolRule(type="SYMBOL", name="decorator"),
),
FieldRule(
name="definition",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="class_definition"
),
SymbolRule(
type="SYMBOL", name="function_definition"
),
],
),
),
],
)
```

Node ID: 160
 - Kind: "decorator", Named: True, Hidden: False, Visible: False
 - Type: "decorator"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="@"),
SymbolRule(type="SYMBOL", name="expression"),
SymbolRule(type="SYMBOL", name="_newline"),
],
)
```

Node ID: 161
 - Kind: "block", Named: True, Hidden: False, Visible: False
 - Type: "block"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
RepeatRule(
type="REPEAT",
content=SymbolRule(type="SYMBOL", name="_statement"),
),
SymbolRule(type="SYMBOL", name="_dedent"),
],
)
```

Node ID: 162
 - Kind: "expression_list", Named: True, Hidden: False, Visible: False
 - Type: "expression_list"
 - Rule:

```py
PrecRule(
type="PREC_RIGHT",
value=0,
content=SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="expression"),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
SeqRule(
type="SEQ",
members=[
Repeat1Rule(
type="REPEAT1",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING", value=","
),
SymbolRule(
type="SYMBOL",
name="expression",
),
],
),
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(
type="STRING", value=","
),
BlankRule(type="BLANK"),
],
),
],
),
],
),
],
),
)
```

Node ID: 163
 - Kind: "dotted_name", Named: True, Hidden: False, Visible: False
 - Type: "dotted_name"
 - Rule:

```py
PrecRule(
type="PREC",
value=1,
content=SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="."),
SymbolRule(type="SYMBOL", name="identifier"),
],
),
),
],
),
)
```

Node ID: 164
 - Kind: "case_pattern", Named: True, Hidden: False, Visible: False
 - Type: "case_pattern"
 - Rule:

```py
PrecRule(
type="PREC",
value=1,
content=ChoiceRule(
type="CHOICE",
members=[
AliasRule(
type="ALIAS",
value="as_pattern",
named=True,
content=SymbolRule(type="SYMBOL", name="_as_pattern"),
),
SymbolRule(type="SYMBOL", name="keyword_pattern"),
SymbolRule(type="SYMBOL", name="_simple_pattern"),
],
),
)
```

Node ID: 165
 - Kind: "_simple_pattern", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
PrecRule(
type="PREC",
value=1,
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="class_pattern"),
SymbolRule(type="SYMBOL", name="splat_pattern"),
SymbolRule(type="SYMBOL", name="union_pattern"),
AliasRule(
type="ALIAS",
value="list_pattern",
named=True,
content=SymbolRule(
type="SYMBOL", name="_list_pattern"
),
),
AliasRule(
type="ALIAS",
value="tuple_pattern",
named=True,
content=SymbolRule(
type="SYMBOL", name="_tuple_pattern"
),
),
SymbolRule(type="SYMBOL", name="dict_pattern"),
SymbolRule(type="SYMBOL", name="string"),
SymbolRule(type="SYMBOL", name="concatenated_string"),
SymbolRule(type="SYMBOL", name="true"),
SymbolRule(type="SYMBOL", name="false"),
SymbolRule(type="SYMBOL", name="none"),
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="-"),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="integer"),
SymbolRule(type="SYMBOL", name="float"),
],
),
],
),
SymbolRule(type="SYMBOL", name="complex_pattern"),
SymbolRule(type="SYMBOL", name="dotted_name"),
StringRule(type="STRING", value="_"),
],
),
)
```

Node ID: 166
 - Kind: "as_pattern", Named: True, Hidden: False, Visible: False
 - Type: "as_pattern"
 - Rule:

```py
PrecRule(
type="PREC_LEFT",
value=0,
content=SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="expression"),
StringRule(type="STRING", value="as"),
FieldRule(
name="alias",
type="FIELD",
content=AliasRule(
type="ALIAS",
value="as_pattern_target",
named=True,
content=SymbolRule(
type="SYMBOL", name="expression"
),
),
),
],
),
)
```

Node ID: 167
 - Kind: "union_pattern", Named: True, Hidden: False, Visible: False
 - Type: "union_pattern"
 - Rule:

```py
PrecRule(
type="PREC_RIGHT",
value=0,
content=SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="_simple_pattern"),
Repeat1Rule(
type="REPEAT1",
content=PrecRule(
type="PREC_LEFT",
value=0,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="|"),
SymbolRule(
type="SYMBOL", name="_simple_pattern"
),
],
),
),
),
],
),
)
```

Node ID: 168
 - Kind: "list_pattern", Named: True, Hidden: False, Visible: False
 - Type: "list_pattern"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="["),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="_patterns"),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="]"),
],
)
```

Node ID: 169
 - Kind: "tuple_pattern", Named: True, Hidden: False, Visible: False
 - Type: "tuple_pattern"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="("),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="_patterns"),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=")"),
],
)
```

Node ID: 170
 - Kind: "dict_pattern", Named: True, Hidden: False, Visible: False
 - Type: "dict_pattern"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="{"),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL",
name="_key_value_pattern",
),
SymbolRule(
type="SYMBOL",
name="splat_pattern",
),
],
),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING",
value=",",
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL",
name="_key_value_pattern",
),
SymbolRule(
type="SYMBOL",
name="splat_pattern",
),
],
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="}"),
],
)
```

Node ID: 171
 - Kind: "_key_value_pattern", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
FieldRule(
name="key",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_simple_pattern"),
),
StringRule(type="STRING", value=":"),
FieldRule(
name="value",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="case_pattern"),
),
],
)
```

Node ID: 172
 - Kind: "keyword_pattern", Named: True, Hidden: False, Visible: False
 - Type: "keyword_pattern"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
StringRule(type="STRING", value="="),
SymbolRule(type="SYMBOL", name="_simple_pattern"),
],
)
```

Node ID: 173
 - Kind: "splat_pattern", Named: True, Hidden: False, Visible: False
 - Type: "splat_pattern"
 - Rule:

```py
PrecRule(
type="PREC",
value=1,
content=SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="*"),
StringRule(type="STRING", value="**"),
],
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
StringRule(type="STRING", value="_"),
],
),
],
),
)
```

Node ID: 174
 - Kind: "class_pattern", Named: True, Hidden: False, Visible: False
 - Type: "class_pattern"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="dotted_name"),
StringRule(type="STRING", value="("),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
SeqRule(
type="SEQ",
members=[
SymbolRule(
type="SYMBOL", name="case_pattern"
),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING",
value=",",
),
SymbolRule(
type="SYMBOL",
name="case_pattern",
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=")"),
],
)
```

Node ID: 175
 - Kind: "complex_pattern", Named: True, Hidden: False, Visible: False
 - Type: "complex_pattern"
 - Rule:

```py
PrecRule(
type="PREC",
value=1,
content=SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="-"),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="integer"),
SymbolRule(type="SYMBOL", name="float"),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="+"),
StringRule(type="STRING", value="-"),
],
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="integer"),
SymbolRule(type="SYMBOL", name="float"),
],
),
],
),
)
```

Node ID: 176
 - Kind: "_parameters", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="parameter"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
SymbolRule(
type="SYMBOL", name="parameter"
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
)
```

Node ID: 177
 - Kind: "_patterns", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="pattern"),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
SymbolRule(type="SYMBOL", name="pattern"),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
)
```

Node ID: 178
 - Kind: "parameter", Named: False, Hidden: False, Visible: False
 - Type: "parameter"
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
SymbolRule(type="SYMBOL", name="typed_parameter"),
SymbolRule(type="SYMBOL", name="default_parameter"),
SymbolRule(type="SYMBOL", name="typed_default_parameter"),
SymbolRule(type="SYMBOL", name="list_splat_pattern"),
SymbolRule(type="SYMBOL", name="tuple_pattern"),
SymbolRule(type="SYMBOL", name="keyword_separator"),
SymbolRule(type="SYMBOL", name="positional_separator"),
SymbolRule(type="SYMBOL", name="dictionary_splat_pattern"),
],
)
```

Node ID: 179
 - Kind: "pattern", Named: False, Hidden: False, Visible: False
 - Type: "pattern"
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
SymbolRule(type="SYMBOL", name="keyword_identifier"),
SymbolRule(type="SYMBOL", name="subscript"),
SymbolRule(type="SYMBOL", name="attribute"),
SymbolRule(type="SYMBOL", name="list_splat_pattern"),
SymbolRule(type="SYMBOL", name="tuple_pattern"),
SymbolRule(type="SYMBOL", name="list_pattern"),
],
)
```

Node ID: 180
 - Kind: "tuple_pattern", Named: True, Hidden: False, Visible: False
 - Type: "tuple_pattern"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="("),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="_patterns"),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=")"),
],
)
```

Node ID: 181
 - Kind: "list_pattern", Named: True, Hidden: False, Visible: False
 - Type: "list_pattern"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="["),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="_patterns"),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="]"),
],
)
```

Node ID: 182
 - Kind: "default_parameter", Named: True, Hidden: False, Visible: False
 - Type: "default_parameter"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
FieldRule(
name="name",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
SymbolRule(type="SYMBOL", name="tuple_pattern"),
],
),
),
StringRule(type="STRING", value="="),
FieldRule(
name="value",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
],
)
```

Node ID: 183
 - Kind: "typed_default_parameter", Named: True, Hidden: False, Visible: False
 - Type: "typed_default_parameter"
 - Rule:

```py
PrecRule(
type="PREC",
value=-1,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="name",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="identifier"),
),
StringRule(type="STRING", value=":"),
FieldRule(
name="type",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="type"),
),
StringRule(type="STRING", value="="),
FieldRule(
name="value",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
],
),
)
```

Node ID: 184
 - Kind: "list_splat_pattern", Named: True, Hidden: False, Visible: False
 - Type: "list_splat_pattern"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="*"),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
SymbolRule(type="SYMBOL", name="keyword_identifier"),
SymbolRule(type="SYMBOL", name="subscript"),
SymbolRule(type="SYMBOL", name="attribute"),
],
),
],
)
```

Node ID: 185
 - Kind: "dictionary_splat_pattern", Named: True, Hidden: False, Visible: False
 - Type: "dictionary_splat_pattern"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="**"),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
SymbolRule(type="SYMBOL", name="keyword_identifier"),
SymbolRule(type="SYMBOL", name="subscript"),
SymbolRule(type="SYMBOL", name="attribute"),
],
),
],
)
```

Node ID: 186
 - Kind: "as_pattern", Named: True, Hidden: False, Visible: False
 - Type: "as_pattern"
 - Rule:

```py
PrecRule(
type="PREC_LEFT",
value=0,
content=SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="expression"),
StringRule(type="STRING", value="as"),
FieldRule(
name="alias",
type="FIELD",
content=AliasRule(
type="ALIAS",
value="as_pattern_target",
named=True,
content=SymbolRule(
type="SYMBOL", name="expression"
),
),
),
],
),
)
```

Node ID: 187
 - Kind: "_expression_within_for_in_clause", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="expression"),
AliasRule(
type="ALIAS",
value="lambda",
named=True,
content=SymbolRule(
type="SYMBOL", name="lambda_within_for_in_clause"
),
),
],
)
```

Node ID: 188
 - Kind: "expression", Named: False, Hidden: False, Visible: False
 - Type: "expression"
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="comparison_operator"),
SymbolRule(type="SYMBOL", name="not_operator"),
SymbolRule(type="SYMBOL", name="boolean_operator"),
SymbolRule(type="SYMBOL", name="lambda"),
SymbolRule(type="SYMBOL", name="primary_expression"),
SymbolRule(type="SYMBOL", name="conditional_expression"),
SymbolRule(type="SYMBOL", name="named_expression"),
SymbolRule(type="SYMBOL", name="as_pattern"),
],
)
```

Node ID: 189
 - Kind: "primary_expression", Named: False, Hidden: False, Visible: False
 - Type: "primary_expression"
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="await"),
SymbolRule(type="SYMBOL", name="binary_operator"),
SymbolRule(type="SYMBOL", name="identifier"),
SymbolRule(type="SYMBOL", name="keyword_identifier"),
SymbolRule(type="SYMBOL", name="string"),
SymbolRule(type="SYMBOL", name="concatenated_string"),
SymbolRule(type="SYMBOL", name="integer"),
SymbolRule(type="SYMBOL", name="float"),
SymbolRule(type="SYMBOL", name="true"),
SymbolRule(type="SYMBOL", name="false"),
SymbolRule(type="SYMBOL", name="none"),
SymbolRule(type="SYMBOL", name="unary_operator"),
SymbolRule(type="SYMBOL", name="attribute"),
SymbolRule(type="SYMBOL", name="subscript"),
SymbolRule(type="SYMBOL", name="call"),
SymbolRule(type="SYMBOL", name="list"),
SymbolRule(type="SYMBOL", name="list_comprehension"),
SymbolRule(type="SYMBOL", name="dictionary"),
SymbolRule(type="SYMBOL", name="dictionary_comprehension"),
SymbolRule(type="SYMBOL", name="set"),
SymbolRule(type="SYMBOL", name="set_comprehension"),
SymbolRule(type="SYMBOL", name="tuple"),
SymbolRule(type="SYMBOL", name="parenthesized_expression"),
SymbolRule(type="SYMBOL", name="generator_expression"),
SymbolRule(type="SYMBOL", name="ellipsis"),
AliasRule(
type="ALIAS",
value="list_splat",
named=True,
content=SymbolRule(
type="SYMBOL", name="list_splat_pattern"
),
),
],
)
```

Node ID: 190
 - Kind: "not_operator", Named: True, Hidden: False, Visible: False
 - Type: "not_operator"
 - Rule:

```py
PrecRule(
type="PREC",
value=12,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="not"),
FieldRule(
name="argument",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
],
),
)
```

Node ID: 191
 - Kind: "boolean_operator", Named: True, Hidden: False, Visible: False
 - Type: "boolean_operator"
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
PrecRule(
type="PREC_LEFT",
value=11,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(
type="STRING", value="and"
),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=10,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="or"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="expression"
),
),
],
),
),
],
)
```

Node ID: 192
 - Kind: "binary_operator", Named: True, Hidden: False, Visible: False
 - Type: "binary_operator"
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
PrecRule(
type="PREC_LEFT",
value=18,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="+"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=18,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="-"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=19,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="*"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=19,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="@"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=19,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="/"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=19,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="%"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=19,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="//"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_RIGHT",
value=21,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="**"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=14,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="|"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=15,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="&"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=16,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="^"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=17,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value="<<"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
PrecRule(
type="PREC_LEFT",
value=17,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="operator",
type="FIELD",
content=StringRule(type="STRING", value=">>"),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
),
],
)
```

Node ID: 193
 - Kind: "unary_operator", Named: True, Hidden: False, Visible: False
 - Type: "unary_operator"
 - Rule:

```py
PrecRule(
type="PREC",
value=20,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="operator",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="+"),
StringRule(type="STRING", value="-"),
StringRule(type="STRING", value="~"),
],
),
),
FieldRule(
name="argument",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
],
),
)
```

Node ID: 194
 - Kind: "comparison_operator", Named: True, Hidden: False, Visible: False
 - Type: "comparison_operator"
 - Rule:

```py
PrecRule(
type="PREC_LEFT",
value=13,
content=SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="primary_expression"),
Repeat1Rule(
type="REPEAT1",
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="operators",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
StringRule(
type="STRING", value="<"
),
StringRule(
type="STRING", value="<="
),
StringRule(
type="STRING", value="=="
),
StringRule(
type="STRING", value="!="
),
StringRule(
type="STRING", value=">="
),
StringRule(
type="STRING", value=">"
),
StringRule(
type="STRING", value="<>"
),
StringRule(
type="STRING", value="in"
),
AliasRule(
type="ALIAS",
value="not in",
named=False,
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING",
value="not",
),
StringRule(
type="STRING",
value="in",
),
],
),
),
StringRule(
type="STRING", value="is"
),
AliasRule(
type="ALIAS",
value="is not",
named=False,
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING",
value="is",
),
StringRule(
type="STRING",
value="not",
),
],
),
),
],
),
),
SymbolRule(
type="SYMBOL", name="primary_expression"
),
],
),
),
],
),
)
```

Node ID: 195
 - Kind: "lambda", Named: True, Hidden: False, Visible: False
 - Type: "lambda"
 - Rule:

```py
PrecRule(
type="PREC",
value=-2,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="lambda"),
FieldRule(
name="parameters",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="lambda_parameters"
),
BlankRule(type="BLANK"),
],
),
),
StringRule(type="STRING", value=":"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
],
),
)
```

Node ID: 196
 - Kind: "lambda", Named: True, Hidden: False, Visible: False
 - Type: "lambda"
 - Rule:

```py
PrecRule(
type="PREC",
value=-2,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="lambda"),
FieldRule(
name="parameters",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="lambda_parameters"
),
BlankRule(type="BLANK"),
],
),
),
StringRule(type="STRING", value=":"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
],
),
)
```

Node ID: 197
 - Kind: "assignment", Named: True, Hidden: False, Visible: False
 - Type: "assignment"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_left_hand_side"),
),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="="),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="_right_hand_side"
),
),
],
),
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=":"),
FieldRule(
name="type",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="type"
),
),
],
),
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=":"),
FieldRule(
name="type",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="type"
),
),
StringRule(type="STRING", value="="),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="_right_hand_side"
),
),
],
),
],
),
],
)
```

Node ID: 198
 - Kind: "augmented_assignment", Named: True, Hidden: False, Visible: False
 - Type: "augmented_assignment"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_left_hand_side"),
),
FieldRule(
name="operator",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="+="),
StringRule(type="STRING", value="-="),
StringRule(type="STRING", value="*="),
StringRule(type="STRING", value="/="),
StringRule(type="STRING", value="@="),
StringRule(type="STRING", value="//="),
StringRule(type="STRING", value="%="),
StringRule(type="STRING", value="**="),
StringRule(type="STRING", value=">>="),
StringRule(type="STRING", value="<<="),
StringRule(type="STRING", value="&="),
StringRule(type="STRING", value="^="),
StringRule(type="STRING", value="|="),
],
),
),
FieldRule(
name="right",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="_right_hand_side"
),
),
],
)
```

Node ID: 199
 - Kind: "pattern_list", Named: True, Hidden: False, Visible: False
 - Type: "pattern_list"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="pattern"),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
SeqRule(
type="SEQ",
members=[
Repeat1Rule(
type="REPEAT1",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING", value=","
),
SymbolRule(
type="SYMBOL", name="pattern"
),
],
),
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
),
],
),
],
)
```

Node ID: 200
 - Kind: "_right_hand_side", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="expression"),
SymbolRule(type="SYMBOL", name="expression_list"),
SymbolRule(type="SYMBOL", name="assignment"),
SymbolRule(type="SYMBOL", name="augmented_assignment"),
SymbolRule(type="SYMBOL", name="pattern_list"),
SymbolRule(type="SYMBOL", name="yield"),
],
)
```

Node ID: 201
 - Kind: "yield", Named: True, Hidden: False, Visible: False
 - Type: "yield"
 - Rule:

```py
PrecRule(
type="PREC_RIGHT",
value=0,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="yield"),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="from"),
SymbolRule(
type="SYMBOL", name="expression"
),
],
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="_expressions"
),
BlankRule(type="BLANK"),
],
),
],
),
],
),
)
```

Node ID: 202
 - Kind: "attribute", Named: True, Hidden: False, Visible: False
 - Type: "attribute"
 - Rule:

```py
PrecRule(
type="PREC",
value=22,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="object",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
StringRule(type="STRING", value="."),
FieldRule(
name="attribute",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="identifier"),
),
],
),
)
```

Node ID: 203
 - Kind: "subscript", Named: True, Hidden: False, Visible: False
 - Type: "subscript"
 - Rule:

```py
PrecRule(
type="PREC",
value=22,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="value",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
StringRule(type="STRING", value="["),
SeqRule(
type="SEQ",
members=[
FieldRule(
name="subscript",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="expression"
),
SymbolRule(
type="SYMBOL", name="slice"
),
],
),
),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
FieldRule(
name="subscript",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL",
name="expression",
),
SymbolRule(
type="SYMBOL",
name="slice",
),
],
),
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="]"),
],
),
)
```

Node ID: 204
 - Kind: "slice", Named: True, Hidden: False, Visible: False
 - Type: "slice"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="expression"),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=":"),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="expression"),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=":"),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="expression"
),
BlankRule(type="BLANK"),
],
),
],
),
BlankRule(type="BLANK"),
],
),
],
)
```

Node ID: 205
 - Kind: "call", Named: True, Hidden: False, Visible: False
 - Type: "call"
 - Rule:

```py
PrecRule(
type="PREC",
value=22,
content=SeqRule(
type="SEQ",
members=[
FieldRule(
name="function",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="primary_expression"
),
),
FieldRule(
name="arguments",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="generator_expression"
),
SymbolRule(
type="SYMBOL", name="argument_list"
),
],
),
),
],
),
)
```

Node ID: 206
 - Kind: "typed_parameter", Named: True, Hidden: False, Visible: False
 - Type: "typed_parameter"
 - Rule:

```py
PrecRule(
type="PREC",
value=-1,
content=SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
SymbolRule(
type="SYMBOL", name="list_splat_pattern"
),
SymbolRule(
type="SYMBOL", name="dictionary_splat_pattern"
),
],
),
StringRule(type="STRING", value=":"),
FieldRule(
name="type",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="type"),
),
],
),
)
```

Node ID: 207
 - Kind: "type", Named: True, Hidden: False, Visible: False
 - Type: "type"
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="expression"),
SymbolRule(type="SYMBOL", name="splat_type"),
SymbolRule(type="SYMBOL", name="generic_type"),
SymbolRule(type="SYMBOL", name="union_type"),
SymbolRule(type="SYMBOL", name="constrained_type"),
SymbolRule(type="SYMBOL", name="member_type"),
],
)
```

Node ID: 208
 - Kind: "splat_type", Named: True, Hidden: False, Visible: False
 - Type: "splat_type"
 - Rule:

```py
PrecRule(
type="PREC",
value=1,
content=SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="*"),
StringRule(type="STRING", value="**"),
],
),
SymbolRule(type="SYMBOL", name="identifier"),
],
),
)
```

Node ID: 209
 - Kind: "generic_type", Named: True, Hidden: False, Visible: False
 - Type: "generic_type"
 - Rule:

```py
PrecRule(
type="PREC",
value=1,
content=SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
SymbolRule(type="SYMBOL", name="type_parameter"),
],
),
)
```

Node ID: 210
 - Kind: "union_type", Named: True, Hidden: False, Visible: False
 - Type: "union_type"
 - Rule:

```py
PrecRule(
type="PREC_LEFT",
value=0,
content=SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="type"),
StringRule(type="STRING", value="|"),
SymbolRule(type="SYMBOL", name="type"),
],
),
)
```

Node ID: 211
 - Kind: "constrained_type", Named: True, Hidden: False, Visible: False
 - Type: "constrained_type"
 - Rule:

```py
PrecRule(
type="PREC_RIGHT",
value=0,
content=SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="type"),
StringRule(type="STRING", value=":"),
SymbolRule(type="SYMBOL", name="type"),
],
),
)
```

Node ID: 212
 - Kind: "member_type", Named: True, Hidden: False, Visible: False
 - Type: "member_type"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="type"),
StringRule(type="STRING", value="."),
SymbolRule(type="SYMBOL", name="identifier"),
],
)
```

Node ID: 213
 - Kind: "keyword_argument", Named: True, Hidden: False, Visible: False
 - Type: "keyword_argument"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
FieldRule(
name="name",
type="FIELD",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="identifier"),
SymbolRule(
type="SYMBOL", name="keyword_identifier"
),
],
),
),
StringRule(type="STRING", value="="),
FieldRule(
name="value",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
],
)
```

Node ID: 214
 - Kind: "list", Named: True, Hidden: False, Visible: False
 - Type: "list"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="["),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="_collection_elements"
),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="]"),
],
)
```

Node ID: 215
 - Kind: "set", Named: True, Hidden: False, Visible: False
 - Type: "set"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="{"),
SymbolRule(type="SYMBOL", name="_collection_elements"),
StringRule(type="STRING", value="}"),
],
)
```

Node ID: 216
 - Kind: "tuple", Named: True, Hidden: False, Visible: False
 - Type: "tuple"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="("),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="_collection_elements"
),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value=")"),
],
)
```

Node ID: 217
 - Kind: "dictionary", Named: True, Hidden: False, Visible: False
 - Type: "dictionary"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="{"),
ChoiceRule(
type="CHOICE",
members=[
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="pair"
),
SymbolRule(
type="SYMBOL",
name="dictionary_splat",
),
],
),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING", value=","
),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL",
name="pair",
),
SymbolRule(
type="SYMBOL",
name="dictionary_splat",
),
],
),
],
),
),
],
),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="}"),
],
)
```

Node ID: 218
 - Kind: "pair", Named: True, Hidden: False, Visible: False
 - Type: "pair"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
FieldRule(
name="key",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
StringRule(type="STRING", value=":"),
FieldRule(
name="value",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
],
)
```

Node ID: 219
 - Kind: "list_comprehension", Named: True, Hidden: False, Visible: False
 - Type: "list_comprehension"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="["),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
SymbolRule(type="SYMBOL", name="_comprehension_clauses"),
StringRule(type="STRING", value="]"),
],
)
```

Node ID: 220
 - Kind: "dictionary_comprehension", Named: True, Hidden: False, Visible: False
 - Type: "dictionary_comprehension"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="{"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="pair"),
),
SymbolRule(type="SYMBOL", name="_comprehension_clauses"),
StringRule(type="STRING", value="}"),
],
)
```

Node ID: 221
 - Kind: "set_comprehension", Named: True, Hidden: False, Visible: False
 - Type: "set_comprehension"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="{"),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
SymbolRule(type="SYMBOL", name="_comprehension_clauses"),
StringRule(type="STRING", value="}"),
],
)
```

Node ID: 222
 - Kind: "generator_expression", Named: True, Hidden: False, Visible: False
 - Type: "generator_expression"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="("),
FieldRule(
name="body",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="expression"),
),
SymbolRule(type="SYMBOL", name="_comprehension_clauses"),
StringRule(type="STRING", value=")"),
],
)
```

Node ID: 223
 - Kind: "_comprehension_clauses", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="for_in_clause"),
RepeatRule(
type="REPEAT",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="for_in_clause"),
SymbolRule(type="SYMBOL", name="if_clause"),
],
),
),
],
)
```

Node ID: 224
 - Kind: "parenthesized_expression", Named: True, Hidden: False, Visible: False
 - Type: "parenthesized_expression"
 - Rule:

```py
PrecRule(
type="PREC",
value=1,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="("),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="expression"),
SymbolRule(type="SYMBOL", name="yield"),
],
),
StringRule(type="STRING", value=")"),
],
),
)
```

Node ID: 225
 - Kind: "_collection_elements", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="expression"),
SymbolRule(type="SYMBOL", name="yield"),
SymbolRule(type="SYMBOL", name="list_splat"),
SymbolRule(
type="SYMBOL",
name="parenthesized_list_splat",
),
],
),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=","),
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL",
name="expression",
),
SymbolRule(
type="SYMBOL", name="yield"
),
SymbolRule(
type="SYMBOL",
name="list_splat",
),
SymbolRule(
type="SYMBOL",
name="parenthesized_list_splat",
),
],
),
],
),
),
],
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
)
```

Node ID: 226
 - Kind: "for_in_clause", Named: True, Hidden: False, Visible: False
 - Type: "for_in_clause"
 - Rule:

```py
PrecRule(
type="PREC_LEFT",
value=0,
content=SeqRule(
type="SEQ",
members=[
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="async"),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="for"),
FieldRule(
name="left",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="_left_hand_side"
),
),
StringRule(type="STRING", value="in"),
FieldRule(
name="right",
type="FIELD",
content=SeqRule(
type="SEQ",
members=[
SymbolRule(
type="SYMBOL",
name="_expression_within_for_in_clause",
),
RepeatRule(
type="REPEAT",
content=SeqRule(
type="SEQ",
members=[
StringRule(
type="STRING", value=","
),
SymbolRule(
type="SYMBOL",
name="_expression_within_for_in_clause",
),
],
),
),
],
),
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value=","),
BlankRule(type="BLANK"),
],
),
],
),
)
```

Node ID: 227
 - Kind: "if_clause", Named: True, Hidden: False, Visible: False
 - Type: "if_clause"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="if"),
SymbolRule(type="SYMBOL", name="expression"),
],
)
```

Node ID: 228
 - Kind: "conditional_expression", Named: True, Hidden: False, Visible: False
 - Type: "conditional_expression"
 - Rule:

```py
PrecRule(
type="PREC_RIGHT",
value=-1,
content=SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="expression"),
StringRule(type="STRING", value="if"),
SymbolRule(type="SYMBOL", name="expression"),
StringRule(type="STRING", value="else"),
SymbolRule(type="SYMBOL", name="expression"),
],
),
)
```

Node ID: 229
 - Kind: "concatenated_string", Named: True, Hidden: False, Visible: False
 - Type: "concatenated_string"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="string"),
Repeat1Rule(
type="REPEAT1",
content=SymbolRule(type="SYMBOL", name="string"),
),
],
)
```

Node ID: 230
 - Kind: "string", Named: True, Hidden: False, Visible: False
 - Type: "string"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
SymbolRule(type="SYMBOL", name="string_start"),
RepeatRule(
type="REPEAT",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="interpolation"),
SymbolRule(type="SYMBOL", name="string_content"),
],
),
),
SymbolRule(type="SYMBOL", name="string_end"),
],
)
```

Node ID: 231
 - Kind: "string_content", Named: True, Hidden: False, Visible: False
 - Type: "string_content"
 - Rule:

```py
PrecRule(
type="PREC_RIGHT",
value=0,
content=Repeat1Rule(
type="REPEAT1",
content=ChoiceRule(
type="CHOICE",
members=[
SymbolRule(
type="SYMBOL", name="escape_interpolation"
),
SymbolRule(type="SYMBOL", name="escape_sequence"),
SymbolRule(
type="SYMBOL", name="_not_escape_sequence"
),
SymbolRule(type="SYMBOL", name="_string_content"),
],
),
),
)
```

Node ID: 232
 - Kind: "interpolation", Named: True, Hidden: False, Visible: False
 - Type: "interpolation"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="{"),
FieldRule(
name="expression",
type="FIELD",
content=SymbolRule(type="SYMBOL", name="_f_expression"),
),
ChoiceRule(
type="CHOICE",
members=[
StringRule(type="STRING", value="="),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
FieldRule(
name="type_conversion",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="type_conversion"
),
),
BlankRule(type="BLANK"),
],
),
ChoiceRule(
type="CHOICE",
members=[
FieldRule(
name="format_specifier",
type="FIELD",
content=SymbolRule(
type="SYMBOL", name="format_specifier"
),
),
BlankRule(type="BLANK"),
],
),
StringRule(type="STRING", value="}"),
],
)
```

Node ID: 233
 - Kind: "_f_expression", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule:

```py
ChoiceRule(
type="CHOICE",
members=[
SymbolRule(type="SYMBOL", name="expression"),
SymbolRule(type="SYMBOL", name="expression_list"),
SymbolRule(type="SYMBOL", name="pattern_list"),
SymbolRule(type="SYMBOL", name="yield"),
],
)
```

Node ID: 234
 - Kind: "format_specifier", Named: True, Hidden: False, Visible: False
 - Type: "format_specifier"
 - Rule:

```py
SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value=":"),
RepeatRule(
type="REPEAT",
content=ChoiceRule(
type="CHOICE",
members=[
TokenRule(
type="TOKEN",
content=PrecRule(
type="PREC",
value=1,
content=PatternRule(
type="PATTERN",
value="[^{}\\n]+",
flags=None,
),
),
),
AliasRule(
type="ALIAS",
value="format_expression",
named=True,
content=SymbolRule(
type="SYMBOL", name="interpolation"
),
),
],
),
),
],
)
```

Node ID: 235
 - Kind: "await", Named: True, Hidden: False, Visible: False
 - Type: "await"
 - Rule:

```py
PrecRule(
type="PREC",
value=20,
content=SeqRule(
type="SEQ",
members=[
StringRule(type="STRING", value="await"),
SymbolRule(type="SYMBOL", name="primary_expression"),
],
),
)
```

Node ID: 236
 - Kind: "positional_separator", Named: True, Hidden: False, Visible: False
 - Type: "positional_separator"
 - Rule:

```py
StringRule(type="STRING", value="/")
```

Node ID: 237
 - Kind: "keyword_separator", Named: True, Hidden: False, Visible: False
 - Type: "keyword_separator"
 - Rule:

```py
StringRule(type="STRING", value="*")
```

Node ID: 238
 - Kind: "module_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 239
 - Kind: "_simple_statements_repeat1", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 240
 - Kind: "import_prefix_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 241
 - Kind: "_import_list_repeat1", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 242
 - Kind: "print_statement_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 243
 - Kind: "assert_statement_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 244
 - Kind: "if_statement_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 245
 - Kind: "match_statement_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 246
 - Kind: "_match_block_repeat1", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 247
 - Kind: "case_clause_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 248
 - Kind: "try_statement_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 249
 - Kind: "try_statement_repeat2", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 250
 - Kind: "with_clause_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 251
 - Kind: "global_statement_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 252
 - Kind: "type_parameter_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 253
 - Kind: "argument_list_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 254
 - Kind: "decorated_definition_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 255
 - Kind: "dotted_name_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 256
 - Kind: "union_pattern_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 257
 - Kind: "dict_pattern_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 258
 - Kind: "_parameters_repeat1", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 259
 - Kind: "_patterns_repeat1", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 260
 - Kind: "comparison_operator_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 261
 - Kind: "subscript_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 262
 - Kind: "dictionary_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 263
 - Kind: "_comprehension_clauses_repeat1", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 264
 - Kind: "_collection_elements_repeat1", Named: False, Hidden: True, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 265
 - Kind: "for_in_clause_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 266
 - Kind: "concatenated_string_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 267
 - Kind: "string_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 268
 - Kind: "string_content_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 269
 - Kind: "format_specifier_repeat1", Named: False, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 270
 - Kind: "as_pattern_target", Named: True, Hidden: False, Visible: False
 - Type: not found
 - Rule: not found.

Node ID: 271
 - Kind: "format_expression", Named: True, Hidden: False, Visible: False
 - Type: "format_expression"
 - Rule: not found.

Node ID: 272
 - Kind: "is not", Named: False, Hidden: False, Visible: False
 - Type: "is not"
 - Rule: not found.

Node ID: 273
 - Kind: "not in", Named: False, Hidden: False, Visible: False
 - Type: "not in"
 - Rule: not found.

