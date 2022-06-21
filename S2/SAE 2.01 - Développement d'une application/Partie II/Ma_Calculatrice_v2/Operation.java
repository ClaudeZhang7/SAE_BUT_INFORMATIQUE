public abstract class Operation extends Expression{

  private Expression valeurExpression1;
  private Expression valeurExpression2;

  public Operation(Expression val1, Expression val2){

    this.valeurExpression1 = val1;
    this.valeurExpression2 = val2;

  }
  

  public Expression getOperande1(){

    return this.valeurExpression1;

  }

  public Expression getOperande2(){

    return this.valeurExpression2;

  }

}