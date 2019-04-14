import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        String cmd = "./test.sh gakki";
        Process child = Runtime.getRuntime().exec(cmd);
        Scanner sc = new Scanner(child.getInputStream());
        int exitValue = child.exitValue();
        System.out.printf("exit value: %d%n", exitValue);
        System.out.println(sc.nextLine());
    }
}
