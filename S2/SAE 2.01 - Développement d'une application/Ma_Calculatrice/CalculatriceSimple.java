
public class CalculatriceSimple{

public static void main (String[] args) {

  System.out.println("Début du programme ");

  Nombre six = new Nombre(6) ;
  Nombre dix = new Nombre(10) ;
  Nombre zero = new Nombre(0);

  System.out.println(six);

  System.out.println(six.valeur());

  Operation soustraction = new Soustraction(dix,six) ;

  System.out.println(soustraction.toString() + " = " + soustraction.valeur());

  Operation addition = new Addition(six,dix);

  System.out.println(addition.toString()+ " = "+ addition.valeur());

  Operation multiplication = new Multiplication(six,dix);

  System.out.println(multiplication.toString()+ " = "+ multiplication.valeur());

  Operation division = new Division(dix,six);

  Operation divisionByZero = new Division(six,zero);

  try{

  	System.out.println(division+" = "+ division.valeur());
  	System.out.println(divisionByZero+" = "+ divisionByZero.valeur());

  }

  catch(ArithmeticException e){

  	System.out.println("Impossible de diviser par 0");

  }

  System.out.println("Fin du programme ");


}
}
