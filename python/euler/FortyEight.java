import java.math.BigInteger;

/**
  this solves the 48th problem
**/
public class FortyEight{
  public static void main(String [] args){
  BigInteger summation = BigInteger.valueOf(0);
  for(int i=1;i<=1000;i++)
     {
       BigInteger temp = BigInteger.valueOf(1);
       for(int j=1;j<=i;j++)
          {
           temp= temp.multiply(BigInteger.valueOf(i));
          }
         summation= summation.add(temp);
     }
	System.out.println(new StringBuilder(new StringBuilder(summation.toString()).reverse().substring(0,10)).reverse().toString());
 }
}
