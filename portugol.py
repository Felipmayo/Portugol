programa {
  funcao inicio() {
    inteiro salario, desconto, final

    escreva ("Insira o sálario: ")
    leia (salario)

    se (salario >= 2000){
     escreva ("O salário som um bônus de 15%, vale: ",salario + (salario * 0.15))
    }
    senao{
     escreva ("O salário vale: ",salario)
    }

  }
}
