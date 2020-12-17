import java.util.ArrayList;

class List {
  
  public static void main(String[] args) {

    double phiOne = (1+Math.sqrt(5))/2;
    double phiTwo = (1-Math.sqrt(5))/2;

    ArrayList<Integer> fibonacciSequence = new ArrayList<Integer>();
    
    for (int i = 0; i <= 10; i++) {
      double powerCalc =  (Math.pow(phiOne,i)-Math.pow(phiTwo,i))/(Math.sqrt(5));
      int newTerm = (int) Math.round(powerCalc);
      fibonacciSequence.add(newTerm);
}

    
    System.out.println("Fibonacci's numbers:");

    System.out.println(fibonacciSequence);   


  }
  
}