class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        result = []
        used = set()

        for char in key:
            if char not in used and char.isalpha():
                used.add(char)
                result.append(char)

        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in used:
                used.add(char)
                result.append(char)

        matrix = [result[i:i + 5] for i in range(0, 25, 5)]
        return matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None, None

    def prepare_plaintext(self, text):
        text = text.upper().replace("J", "I")
        result = ""
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i + 1] if i + 1 < len(text) else "X"
            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        if len(result) % 2 != 0:
            result += "X"
        return result

    def playfair_encrypt(self, plain_text, key):
        matrix = self.create_playfair_matrix(key)
        plain_text = self.prepare_plaintext(plain_text)
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            a, b = plain_text[i], plain_text[i + 1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, key):
        matrix = self.create_playfair_matrix(key)
        cipher_text = cipher_text.upper().replace("J", "I")
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i + 1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        return decrypted_text
