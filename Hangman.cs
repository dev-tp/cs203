
using System;
using System.Collections.Generic;
using System.Text;

public class Hangman
{
    private static string ConstructSecretWord(string word)
    {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < word.Length; i++) {
            if (word[i] != ' ')
                sb.Append('*');
            else
                sb.Append(' ');
        }
        return sb.ToString();
    }

    private static bool CharacterInWord(string word, char character)
    {
        for (int i = 0; i < word.Length; i++)
            if (word[i] == character)
                return true;
        return false;
    }

    private static List<int> IndexOccurrence(String word, char character)
    {
        List<int> indexOccurrance = new List<int>();
        for (int i = 0; i < word.Length; i++)
            if (word[i] == character)
                indexOccurrance.Add(i);
        return indexOccurrance;
    }

    private static string UpdateSecretWord(String secretWord, char character, List<int> indexOccurrence)
    {
        char[] asterics = secretWord.ToCharArray();
        foreach (var i in indexOccurrence) {
            if (i == 0) {
                asterics[i] = (char) (character - 32); // Uppercase first letter
            } else {
                if (secretWord[i - 1] == ' ')
                    asterics[i] = (char) (character - 32); // Uppercase letter after space
                else
                    asterics[i] = character;
            }
        }
        return new string(asterics);
    }

    public static void Main(string[] args)
    {
        Random random = new Random();
        string[] words = "Pimpernell,Lyuda,HellFire,Volcano,Conferrence Call,Interfacer,Lady Fist,Sand Hawk,Fibber".Split(',');
        string word = words[random.Next(words.Length)].ToLower();
        string secretWord = ConstructSecretWord(word);
        List<string> missedLetters = new List<string>();
        int attempts = 7;

        while (attempts != 0) {
            Console.WriteLine("{0}\nMissed letters: {1}", secretWord, string.Join(", ", missedLetters.ToArray())); // missedLetters.toString()
            Console.Write("\nEnter a character: ");
            string input = Console.ReadLine();
            if (input.Length == 1 && !input.Equals("")) {
                char character = input.ToLower()[0];
                if (CharacterInWord(word, character)) {
                    List<int> characterIndex = IndexOccurrence(word, character);
                    secretWord = UpdateSecretWord(secretWord, character, characterIndex);
                    if (secretWord.ToLower().Equals(word)) {
                        Console.WriteLine("{0}\nYou win!", secretWord);
                        break;
                    }
                }
                else {
                    if (!missedLetters.Contains(input))
                        missedLetters.Add(input);
                    if (--attempts == 0) {
                        Console.WriteLine("You lose. The word was: {0}", word);
                        break;
                    }
                }
            }
            else {
                Console.WriteLine("Enter one character.");
            }
        }
    }
}