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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

programa {
  funcao inicio() {
    inteiro intervalo
    escreva("Insira o número: ")
    leia(intervalo)

    se (intervalo <= 50 e intervalo >= 10){
      escreva("Está no intervalo")
    }
    senao{
      escreva("Não está no intervalo")
    }
  }
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

programa {
  funcao inicio() {
    logico ingresso
    inteiro idade

    escreva("Insira a idade: ")
    leia(idade)

    escreva("Você possui um inggresso? ")
    leia(ingresso)

    se (ingresso == "sim"){
      ingresso == verdadeiro
    }
    senao{
      ingresso == falso
    }

    se (idade >= 18 e ingresso){
      escreva("Você pode entrar no evento")
    }
    senao{
      escreva("Acesso negado")
    }
  }
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

programa {
  funcao inicio() {
    cadeia autenticacao, cadastro
    escreva("cadastre a sua senha: ")
    leia(cadastro)

    escreva("Faça o seu login: ")
    leia(autenticacao)

    se (cadastro == autenticacao){
      escreva("Senha correta!")
    }
    senao{
      escreva("A senha está incorreta!")
    }
  }
}
