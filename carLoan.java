public class CarLoan {
  boolean isValid;
  int carLoan;
  int loanLength;
  double interestRate;
  int downPayment;
  String carModel;

public CarLoan(int loan, int length, double interest, int payment, String model){
  carLoan = loan;
  loanLength = length;
  interestRate = interest;
  downPayment = payment;
  carModel = model;
}

public void checkRequirements() {
  if (carLoan <= 0 || interestRate <=0) {
    System.out.println("You must take out a valid loan!");
    isValid = false;
  } else if (downPayment >= carLoan) {
    System.out.println("You're very kind to leave us a tip, but we're afraid we can't take it.");
    isValid = false;
  } else {
    double totalInterest = 1+(interestRate/100);
    double monthlyBalance = ((carLoan - downPayment)*totalInterest)/(loanLength*12);
    System.out.println("Congratulations on purchasing a " + carModel + ", you opted to take a " + carLoan + " dollars loan for a duration of " + loanLength + " years, since you paid " + downPayment +" upfront and chose a " + Math.round(interestRate) + " percent interest rate, your monthly payments amount to " + Math.round(monthlyBalance) + " dollars.");
  }

}

public static void main(String[] args) {
  CarLoan Ferrari = new CarLoan(10000,3,5,2000,"Ferrari");
  Ferrari.checkRequirements();
}
}