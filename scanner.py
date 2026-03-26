class Scanner:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.keywords = {"if", "then", "else", "end"} #tylko przyklady

    def get_next_token(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

        if self.pos >= len(self.text):
            return ('EOF', None)

        char = self.text[self.pos]
        start_pos = self.pos

        if char.isdigit():
            value = ""
            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                value += self.text[self.pos]
                self.pos += 1
            return ('NUMBER', int(value))

        if char.isalpha():
            value = ""
            while self.pos < len(self.text) and self.text[self.pos].isalnum():
                value += self.text[self.pos]
                self.pos += 1
            
            token_type = 'KEYWORD' if value.lower() in self.keywords else 'ID'
            return (token_type, value)

        operators = {
            '+': 'PLUS', '-': 'MINUS', '*': 'MUL', '/': 'DIV',
            '(': 'LPAREN', ')': 'RPAREN', '=': 'ASSIGN'
        }

        if char in operators:
            self.pos += 1
            return (operators[char], char)

        self.pos += 1
        return ('ERROR', f"Nieznany znak: {char} na pozycji {start_pos}")

input_text = "x = 2 + 3 * (76 + 8 / 3) if end"
lexer = Scanner(input_text)

print(f"{'TYP TOKENA':<15} | {'WARTOŚĆ':<15}")
print("-" * 35)

while True:
    token_type, value = lexer.get_next_token()
    print(f"{token_type:<15} | {str(value):<15}")
    if token_type in ['EOF', 'ERROR']:
        break
