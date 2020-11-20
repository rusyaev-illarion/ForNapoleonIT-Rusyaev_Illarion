rule_add = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
}
rule_div = {
        ('I', 'V'): 3,
        ('I', 'X'): 8,
        ('X', 'L'): 30,
        ('X', 'C'): 80,
        ('C', 'D'): 300,
        ('C', 'M'): 800,
}
class Solution:

    def romanToInt(self, s: str) -> int:
        number = 0
        prev_literal = None
        for literal in s:
            if prev_literal and rule_add[prev_literal] < rule_add[literal]:
                number += rule_div[(prev_literal, literal)]
            else:
                number += rule_add[literal]
            prev_literal = literal
        return number
    while True:
        s = input("Введите символы в диапазоне от 1 до 15: ")
        if 1 <= len(s) <= 15:
            k = romanToInt("self", s)
            if 1 <= k <= 3999:
                print(k)
                break
            else:
                print("Введенное число не лежит в диапазоне от 1 до 3999!")
        else:
            print("Введенная длинна не корректна!")