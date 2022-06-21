
public abstract class Operation{

  private Nombre valeurNombre1;
  private Nombre valeurNombre2;

  public Operation(Nombre val1, Nombre val2){

    this.valeurNombre1 = val1;
    this.valeurNombre2 = val2;

  }
  
  public abstract int valeur();

  public Nombre getOperande1(){

    return this.valeurNombre1;

  }

  public Nombre getOperande2(){

    return this.valeurNombre2;

  }

}
