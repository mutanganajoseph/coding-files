import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner x = new Scanner(System.in);
        int marks;
        
        // Input marks from the user
        System.out.print("Enter the student's marks: ");
        marks = x.nextInt();      
        
        // Check marks using switch statement
        switch (marks) {
            case 70:
            case 71:
            case 72:
            case 73:
            case 74:
            case 75:
            case 76:
            case 77:
            case 78:
            case 79:
            case 80:
            case 81:
            case 82:
            case 83:
            case 84:
            case 85:
            case 86:
            case 87:
            case 88:
            case 89:
            case 90:
            case 91:
            case 92:
            case 93:
            case 94:
            case 95:
            case 96:
            case 97:
            case 98:
            case 99:
            case 100:
                System.out.println("Student's marks: " + marks + " (Grade A)");
                break;
            case 60:
            case 61:
            case 62:
            case 63:
            case 64:
            case 65:
            case 66:
            case 67:
            case 68:
            case 69:
                System.out.println("Student's marks: " + marks + " (Grade B)");
                break;
            case 50:
            case 51:
            case 52:
            case 53:
            case 54:
            case 55:
            case 56:
            case 57:
            case 58:
            case 59:
                System.out.println("Student's marks: " + marks + " (Grade C)");
                break;
                case 40:
                case 41:
                case 42:
                case 43:
                case 44:
                case 45:
                case 46:
                case 47:
                case 48:
                case 49:
                System.out.println("Student's marks: " + marks + " (Grade D)");
                break;
            default:
                System.out.println("Student's marks: " + marks + " (Fail)");
        }
    }
}
