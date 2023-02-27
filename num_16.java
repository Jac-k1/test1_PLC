import java.util.regex.*;
public class num_16 {


    public static void main(String[] args) {
        

        Pattern pattern = Pattern.compile("(/*(\n.*?)*)[*/]$");

        Matcher match = pattern.matcher("/* this is comment*/");
        boolean matchfound = match.find();
        if(matchfound) 
        {
            System.out.println("multi-line comment");
        }
            else {
            System.out.println("this is not a comment");
            }

    }
    
}
