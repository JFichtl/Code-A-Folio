public class MainActivity {
  int answer;
  int correctAnswer;
  int numberOfQuestions = 1;

  public int generateRandomNumber(int max){
  double seed = max*Math.random();
  int randomInteger = (int) Math.round(seed);
  //System.out.println(randomInteger);
  return randomInteger;
}

public MainActivity() {

  int totalCorrect=0;

  for (int i = 1; i <= numberOfQuestions; i+=1) {
    answer = generateRandomNumber(6);
    correctAnswer = generateRandomNumber(6);

    System.out.println("Question " + i + ":");
    isCorrect(answer, correctAnswer);

    if (isCorrect(answer, correctAnswer)) {
      System.out.println("You got it! " + answer + " was the correct answer!");
      totalCorrect+=1;
      } else { System.out.println("Nope! The correct answer was " + correctAnswer + ", not " +answer + ".");
      }

    if (i == numberOfQuestions) {
      System.out.println(getGameOverMessage(totalCorrect, numberOfQuestions));
      }
  }
  
  }

public boolean isCorrect(int answer, int correctAnswer) {
  if (answer == correctAnswer) {
    return true;
  } else {
    return false;
  }
}

// Add generateRandomNumber() here

public String getGameOverMessage(int totalCorrect, int totalQuestions) {
  if (totalCorrect == totalQuestions) {
    return "You got all the questions right! You Won!";
  } else {
    return "You got " + totalCorrect + " right out of " + numberOfQuestions + ". Better luck next time!";
  }
}

// Add getGameOverMessage() here

public static void main(String[] args) {
  MainActivity initialize = new MainActivity();

  }
}