class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        form = [".-","-...","-.-.","-..",".","..-.","--.","....",
                "..",".---","-.-",".-..","--","-.","---",".--.",
                "--.-",".-.","...","-","..-","...-",".--","-..-",
                "-.--","--.."]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        char_to_morse = {alphabet[i]: form[i] for i in range(26)}
        transformations = set()

        for word in words:
            transformation = ''.join(char_to_morse[char] for char in word)
            transformations.add(transformation)
            
        return len(transformations)