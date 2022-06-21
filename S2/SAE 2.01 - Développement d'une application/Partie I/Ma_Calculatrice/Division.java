
public class Division extends Operation{
  

  public  Division(Nombre val1, Nombre val2){

    super(val1,val2);

  }


  public int valeur() throws ArithmeticException {

  	if (this.getOperande2().valeur()==0)

  		throw new ArithmeticException();

  	else

  		return this.getOperande1().valeur() / this.getOperande2().valeur();
  }

  public String toString(){

  	return "("+this.getOperande1().valeur()+" / "+ this.getOperande2().valeur() +")";

  }

}
