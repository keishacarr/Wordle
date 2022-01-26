import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //read in dictionary as list
        List<String> dictionary = FileUtils.readLines(new File("dictionary.txt"), "utf-8");
        System.out.print(dictionary);

        Scanner input = new Scanner(System.in);
        System.out.print("Enter a guess!");
        String guess = input.next();
        System.out.print(guess);
    }

}