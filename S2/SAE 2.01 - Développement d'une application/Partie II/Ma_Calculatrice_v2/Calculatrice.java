
public class Calculatrice{

	public static void main (String[] args){

		System.out.println("Début du programme : ");

		Expression deux = new Nombre(2) ;
		Expression trois = new Nombre(3) ;
		Expression dixSept = new Nombre(17) ;

		Expression s = new Soustraction(dixSept, deux) ;
		Expression a = new Addition(deux, trois) ;
		Expression d = new Division(s, a) ;

		Expression zero = new Soustraction(trois,trois);
		Expression divisionByZero = new Division(s,zero);
		Expression mult = new Multiplication(a,s);
		System.out.println(a + " * " + s + " = " + mult.valeur());

		Expression addition = new Addition(d,a);
		System.out.println(d + " + " + a + " = " + addition.valeur());
		
		Expression soustraction = new Soustraction(mult,s);
		System.out.println(mult + " - " + s + " = " + soustraction.valeur());

		try{

			System.out.println(s + " / " + a + " = " + d.valeur()); // affiche ((17 - 2) / (2 + 3)) = 3 
			System.out.println(s + " / " + zero + " = " + divisionByZero.valeur()); 

		}

		catch(ArithmeticException e){

			System.out.println("Impossible de diviser par 0");

		}

		System.out.println("Fin du programme : ");

	}


}