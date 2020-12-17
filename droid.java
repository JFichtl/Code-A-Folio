public class Droid {

  int batteryLevel;
  String name;

  public Droid(String droidName) {
    name = droidName;
    batteryLevel = 100;    
  }

  public void performTask(Droid droid, String taskName) {
    System.out.println("The droid " + droid.name + " is performing task: " + taskName);
    batteryLevel -=10;
    energyReport(droid);
  }

  public void exchangeBattery(Droid droidA, Droid droidB, int c){
    batteryLevel +=c;
    droidB.batteryLevel -= c; 
    System.out.println( droidB.name + " is exchanging "+ c + " per cent battery with " + name);
    energyReport(droidB);
    energyReport(droidA);
  }

  public void energyReport(Droid droid) {
    System.out.println( droid.name + "'s battery level is at:' " + droid.batteryLevel);
  }

  public String toString(){
    return "Hello, I'm the droid " + name;
  }

  public static void main(String[] args) {
    Droid codey = new Droid("Codey");
    Droid albert = new Droid("Albert");
    System.out.println(codey);
    codey.performTask(albert, "dancing");
    codey.performTask(codey, "mowing the lawn");
    codey.exchangeBattery(codey, albert , 30);
  }
}