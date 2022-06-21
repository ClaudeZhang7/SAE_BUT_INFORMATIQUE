
public class Nombre extends Expression{


    private int valeurNombre;



    public Nombre(int val){

      this.valeurNombre = val;

    }

    public Nombre(Nombre val){
    	valeurNombre = val.valeur();
    }

    public int valeur(){

      return this.valeurNombre;

    }

    public String toString(){

      return "Le nombre est : " + this.valeurNombre;

    }
}