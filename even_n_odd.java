import java.util.regex.*;

public class even_n_odd {

    public static void main(String[] args) {
        

        Pattern pattern = Pattern.compile("(((b*ab*ab*)&&(a*ba*ba*)*(a*ba*))(c|d)*|(cbadcbad)*)");

        Matcher match = pattern.matcher("aabbbaa");
        boolean matchfound = match.find();
        if(matchfound) 
        {
            System.out.println("yes");
        }
            else {
            System.out.println("wrong");
            }

    }
    
}