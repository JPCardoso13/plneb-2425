# Exercício 1:
def reverse_string(s):
    """Devolve a string invertida."""
    return s[::-1]

# Alternativa: return ''.join(reversed(s)) ou usar um for loop explícito.


# Exercício 2:
def count_as(s):
    """Conta o número de caracteres 'a' e 'A'"""
    char_map = {'a': 0, 'A': 0}
    for char in s:
        if char in char_map.keys():
            char_map[char] += 1

    return char_map

# Alternativa: return {'a': s.count('a'), 'A': s.count('A')}


# Exercício 3:
def count_vowels(s):
    """Conta o número de vogais numa string."""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1

    return count


# Exercício 4:
def to_lowercase(s):
    """Devolve a string em minúsculas."""
    return s.lower()


# Exercício 5:
def to_uppercase(s):
    """Devolve a string em maiúsculas."""
    return s.upper()


# Exercício 6:
def is_palindrome(s):
    """Verifica se uma string é uma capicua."""
    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


# Exercício 7:
def are_balanced(s1, s2):
    """Verifica se todos os elementos de s1 estão presentes em s2."""
    for char in s1:
        if char not in s2:
            return False
    return True

# Alternativa: return set(s1).issubset(set(s2)) (mais eficiente para strings grandes)
# Nota: A alternativa é mais eficiente porque a verificação de existência de um elemento no set não usa iteração.


# Exercício 8:
def check_occurrences(s1, s2):
    """Calcula o número de ocorrências de s1 em s2."""
    return s2.count(s1) if len(s1) else 0


# Exercício 9:
def is_anagram(s1, s2):
    """Verifica se duas strings são anagrams."""
    if len(s1) != len(s2):
        return False

    char_map = {}
    for char in s1:
        if char not in char_map.keys():
            char_map[char] = 1
        else:
            char_map[char] += 1

    for char in s2:
        if char not in char_map.keys() or char_map[char] <= 0:
            return False
        char_map[char] -= 1

    return True

"""
Primeira tentativa para resolver o exercício 9 (menos eficiente):
def is_anagram(s1, s2):
    if s1 == s2:
        return True
    else:
        for i in range(len(s2)):
            if s2[i] == s1[0]:
                return is_anagram(s1[1:], s2[:i] + s2[i + 1:])
        return False
"""


# Exercício 10:
def group_anagrams(string_list):
    """Agrupa palavras que são anagramas."""
    anagram_map = {}
    for string in string_list:
        key = ''.join(sorted(string))
        if key not in anagram_map:
            anagram_map[key] = [string]
        else:
            anagram_map[key].append(string)

    return anagram_map


if __name__ == '__main__':
    def test(num_exercise, func, *args):
        """
        Função para automatizar testes das funções criadas
        e imprimir os resultados obtidos de forma formatada.
        """
        def format(arg):
            """Função auxiliar para formatação de strings."""
            return f"'{arg}'" if isinstance(arg, str) else str(arg)

        output = func(*args)

        print(f"\n----- EXERCÍCIO {num_exercise} -----")
        for i, arg in enumerate(args):
            formatted_arg = format(arg)
            print(f"arg{i + 1} = {formatted_arg}")
        formatted_input = ", ".join(f"arg{i + 1}" for i in range(len(args)))
        formatted_output = format(output)
        print(f"{func.__name__}({formatted_input}) ---> {formatted_output}")


    # Execução de testes
    test(1, reverse_string, "bom dia")
    test(2, count_as, "boA tArde")
    test(3, count_vowels, "bOa noIte")
    test(4, to_lowercase, "bOM diA")
    test(5, to_uppercase, "Boa tardE")
    test(6, is_palindrome, "radar")
    test(6, is_palindrome, "boa noite")
    test(7, are_balanced, "dois", "esternocleidomastoideu")
    test(7, are_balanced, "esternocleidomastoideu", "bom dia")
    test(8, check_occurrences, "abc", "abcerd0lkwabcgacbabc")
    test(8, check_occurrences, "abc", "")
    test(8, check_occurrences, "xyz", "abcerd0lkwabcgacbabc")
    test(9, is_anagram, "listen", "silent")
    test(9, is_anagram, "hello", "world")
    test(9, is_anagram, "roma", "")
    test(9, is_anagram, "", "")
    test(10, group_anagrams, ["roma", "amor", "sacas", "casas", "tigre", "trige", "iceman", "cinema", "sozinho"])
