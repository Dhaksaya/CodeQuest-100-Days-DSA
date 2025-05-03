import java.util.*;
class Day_10_sol {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your password: ");
        String a = sc.nextLine();
        boolean U = false;
        boolean L = false;
        boolean D = false;
        boolean S = false;
        String specialChars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~";

        for (char ch : a.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                U = true;
            } else if (Character.isLowerCase(ch)) {
                L = true;
            } else if (Character.isDigit(ch)) {
                D = true;
            } else if (specialChars.contains(String.valueOf(ch))) {
                S = true;
            }
        }

        StringBuilder missing = new StringBuilder();

        if (a.length() < 8) {
            missing.append("minimum length of 8 characters, ");
        }
        if (!U) {
            missing.append("uppercase letter, ");
        }
        if (!L) {
            missing.append("lowercase letter, ");
        }
        if (!D) {
            missing.append("digit, ");
        }
        if (!S) {
            missing.append("special character, ");
        }

        if (missing.length() == 0) {
            System.out.println("Strong Password");
        } else {
            String missingStr = missing.substring(0, missing.length() - 2);
            System.out.println("Weak Password (Missing " + missingStr + ")");
        }
    }
}
