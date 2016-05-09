import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Hangman {
    private static String constructSecretWord(String string) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) != ' ')
                sb.append('*');
            else
                sb.append(' ');
        }
        return sb.toString();
    }

    private static boolean characterInWord(String word, char character) {
        for (int i = 0; i < word.length(); i++)
            if (word.charAt(i) == character)
                return true;
        return false;
    }

    private static String updateSecretWord(String secretWord, char character, ArrayList<Integer> indexOccurrence) {
        char[] asterics = secretWord.toCharArray();
        for (Integer i: indexOccurrence) {
            if (i == 0) {
                asterics[i] = (char) (character - 32);
            } else {
                if (secretWord.charAt(i - 1) == ' ')
                    asterics[i] = (char) (character - 32);
                else
                    asterics[i] = character;
            }
        }
        return new String(asterics);
    }

    private static ArrayList<Integer> indexOccurrence(String word, char character) {
        ArrayList<Integer> indexOccurrance = new ArrayList<>();
        for (int i = 0; i < word.length(); i++)
            if (word.charAt(i) == character)
                indexOccurrance.add(i);
        return indexOccurrance;
    }

    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);
        String[] words = "Pimpernell,Lyuda,HellFire,Volcano,Conferrence Call,Interfacer,Lady Fist,Sand Hawk,Fibber".split(",");
        String word = words[random.nextInt(words.length)].toLowerCase();
        String secretWord = constructSecretWord(word);
        ArrayList<String> missedLetters = new ArrayList<>();
        int attempts = 7;

        while (attempts != 0) {
            System.out.printf("%s\nMissed letters: %s\n", secretWord, missedLetters.toString());
            System.out.print("\nEnter a character: ");
            String input = scanner.nextLine();
            if (input.length() == 1 && !input.equals("")) {
                char character = input.charAt(0);
                if (characterInWord(word, character)) {
                    ArrayList<Integer> characterIndex = indexOccurrence(word, character);
                    secretWord = updateSecretWord(secretWord, character, characterIndex);
                    if (secretWord.toLowerCase().equals(word)) {
                        System.out.printf("%s\nYou win!\n", secretWord);
                        scanner.close();
                        break;
                    }
                } else {
                    if (!missedLetters.contains(input))
                        missedLetters.add(input);
                    if (--attempts == 0) {
                        System.out.println("You lose!");
                        scanner.close();
                        break;
                    }
                }
            } else {
                System.out.println("Enter one character.");
            }
        }
    }
}