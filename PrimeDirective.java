// Import statement:
import java.util.ArrayList;

public class PrimeDirective {
  boolean prime;
  ArrayList<Boolean> primeCheck = new ArrayList<Boolean>();

public PrimeDirective() {
} 
  // Add your methods here:

public boolean isPrime(int a){
  if (a<1) {
    prime = false;
  }
  else if (a==2) {prime = true;}
  else if (a>1) {
    for (int i=2; i<a; i++) {
      if (a%i == 0) {
        prime = false;
      } else if (a%i != 0) {
        prime = true;
      } break;
  }
  }
  return prime;
}

public ArrayList<Integer> parityFilter(ArrayList<Integer> numberList, String parity) {
  ArrayList<Integer> orderedList = new ArrayList<Integer>();
  if (parity.equals("Even")) {
    for (int number : numberList) {
      if (number%2 == 0) {orderedList.add(number);}
    }
  } else if (parity.equals("Odd")){
    for (int number : numberList) {
      if ( (number-1)%2 == 0 ) {orderedList.add(number);}
    }
  }
  return orderedList;
}

public ArrayList<Integer> increasingOrder(ArrayList<Integer> numberList) {
  ArrayList<Integer> orderedList = new ArrayList<Integer>();

  boolean isGreater=false;

  for (int j=0; j<numberList.size(); j++) {
    for (int i=j; i<numberList.size(); i++) {
      if (numberList.get(j) < numberList.get(i)) {
        isGreater = false;
      } else if (numberList.get(j) > numberList.get(i)) {
        isGreater = true;
      } break;
    }
    if (!isGreater) {
      //numberList.remove(numberList.indexOf(number));
      orderedList.add(numberList.get(j));
      }
  }

  return orderedList;
}

public ArrayList<Integer> fibonacciNumbers(int n) {
  ArrayList<Integer> fibonacciNumbers = new ArrayList<Integer>();
  fibonacciNumbers.add(0);
  fibonacciNumbers.add(1);
  for (int i = 2; i<=n; i++) {
    int nthMinusTwoTerm = fibonacciNumbers.get(i-2);
    int nthMinusOneTerm = fibonacciNumbers.get(i-1);
    fibonacciNumbers.add(nthMinusTwoTerm + nthMinusOneTerm);
  }
  return fibonacciNumbers;
}

  public static void main(String[] args) {

    PrimeDirective pd = new PrimeDirective();
    int[] numbers = {0, 5 ,6, 29, 28, 33, 11, 100, 101, 43, 89};
    ArrayList<Integer> numberList = new ArrayList<Integer>();
    ArrayList<Integer> primeList = new ArrayList<Integer>();

    for (int number : numbers) {numberList.add(number);}

    for (int number : numbers) {
      System.out.println("Is " + number + " a prime number? " + pd.isPrime(number) );
      if (pd.isPrime(number)) {primeList.add(number);}
    }

    System.out.println(primeList);
    System.out.println(pd.parityFilter(numberList,"Even"));
    System.out.println(pd.fibonacciNumbers(10));
  }  

}