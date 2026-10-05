programa {
  funcao inicio() {
    real a 
    real b
    cadeia operador

    escreva ("Insira o primeiro numero: ")
    leia(a)

    escreva ("Insira o segundo numero: ")
    leia(b)

    escreva ("Insira o simbolo do operador desejado: ")
    leia(operador)

    calculadora(a, b, operador)
  }

  funcao calculadora (real a, real b, cadeia operador){
    se(operador == "+"){
      escreva("O resultado é: ", a + b) 
    }
    senao se (operador == "-"){
      escreva("O resultado é: ", a - b)
    }
    senao se(operador == "*"){
      escreva("O resultado é: ", a * b)
    }
    senao se(operador == "/"){
      se(b != 0){
        escreva("O resultado é: ", a / b)
      }
      senao{
        escreva("Divisão por zero!!")
      }
    }
    senao{
      escreva("Operação inválida!!")
    }
  }
}
