public class Calculator{
  int result;

  public Calculator(){

  }

  public int add(int a, int b){
    result = a+b;
    return result;
  }

  public int subtract(int a, int b){
    result = a-b;
    return result;
  }

  public int multiply(int a, int b){
    result = a*b;
    return result;
  }

  public int divide(int a, int b){
    result =a/b;
    return result;
  }

  public int modulo(int a, int b){
    result = a%b;
    return result;
  }

  public String toString(){
    return "The result of the operation is " + result;
  }

  public static void main(String[] args){
    Calculator myCalculator = new Calculator();
    System.out.println(myCalculator.add(5,7));
    System.out.println(myCalculator.subtract(45,11));
  }
}