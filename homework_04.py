import unittest
import random
import string

def text_analysis(text):
    if text.isdigit():
        print("This is a number.")
        if int(text) % 2 == 0:
            return "The number is even."
        else:
            return "The number is odd."
    else:
        return f"This is a word. It consists of {len(text)} letters."


class MyTestClass(unittest.TestCase):
    def test_text_analysis(self):
        random_even_number = random.randint(1, 100000) * 2
        random_odd_number = random_even_number - 1

        characters = string.ascii_letters + string.punctuation + string.whitespace
        number = random.randint(1, 20)
        random_string = ''.join(random.choice(characters) for i in range(number))
        self.assertEqual(text_analysis(random_even_number), "The number is even.")
        self.assertEqual(text_analysis(random_odd_number), "The number is odd.")
        self.assertEqual(text_analysis(random_string), f"This is a word. It consists of {number} letters.")

    def test_incorrect_values(self):
        bools = [True, False]
        random_bool = random.choice(bools)
        with self.assertRaises(TypeError):
            text_analysis(random_bool)


if __name__ == '__main__':
    unittest.main()