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



programa {
  funcao inicio() {
    real a, b
    cadeia operacao

    escreva("Digite o primeiro número: ")
    leia(a)

    escreva("Digite o segundo número: ")
    leia(b)  

    escreva("Símbolo da operação desejada: ")
    leia(operacao)

    se (operacao == "+")
      escreva(a, " + ", b ," = ", a + b)
    
    se (operacao == "-")
      escreva(a, " - ", b ," = ", a - b)
    
    se (operacao == "*")
      escreva(a, " * ", b ," = ", a * b)
    
    se (operacao == "/" e b!=0 )
      escreva(a, " / ", b ," = ", a / b)
    
    senao
      escreva("Operação inválida")   
    }
  }



programa {
  funcao inicio() {
    inteiro idade
    logico autorizacao
    escreva("Insira a idade: ")
    leia(idade)
    escreva("Você possui autorização? ")
    leia(autorizacao)

    se (autorizacao == "sim"){
      autorizacao == verdadeiro
    }
    senao{
      autorizacao == falso
    }
    se (idade >= 12 e idade <= 18 e autorizacao){
      escreva("Você pode praticar esporte")
    }
    senao{
      escreva("Você não pode praticar esse esporte")
    }
  }
}



programa {
  funcao inicio() {
    logico chovendo
    logico pode_sair
    escreva ("Está chovendo? ")
    leia (chovendo)

    pode_sair = nao chovendo
    escreva ("Pode sair = ", pode_sair)
  }
}



programa {
  funcao inicio() {
    #FUNÇÃO: BLOCOS DE CÓDIGO = TAREFA ESPECÍFICA ===> RETORNO (RESULTADO)
   inteiro compra
   escreva("Insira o valor da compra: ")
   leia(compra)

   se (compra >= 100 e compra < 300){
    escreva("O valor ficou: ", compra - (compra*0.10))
   }
   senao se (compra >= 300 e compra < 500){
    escreva("O valor ficou: ", compra - (compra*0.15))
   }
   senao se (compra >= 500){
    escreva("O valor ficou: ", compra - (compra*0.20))
   }
   senao{
    escreva("O valor ficou: ", compra)
   }
}
}



programa
{
    funcao cadeia escolher_opcao(inteiro op)
    {
        escolha (op)
        {
            caso 1:
                retorne "Dinheiro"

            caso 2:
                retorne "Crédito"

            caso 3:
                retorne "Débito"

            caso 4:
                retorne "Boleto"

            caso 5:
                retorne "Pix"

            caso contrario:
                retorne "Opção inválida"
        }
    }

    funcao inicio()
    {
        inteiro op
        cadeia forma

        escreva("------ MENU ------\n")
        escreva("\nOpções de pagamento:")
        escreva("\n1 - Dinheiro")
        escreva("\n2 - Crédito")
        escreva("\n3 - Débito")
        escreva("\n4 - Boleto")
        escreva("\n5 - Pix")

        escreva("\n\nEscolha a forma de pagamento: ")
        leia(op)

        forma = escolher_opcao(op)

        escreva("\nForma escolhida: ", forma)
    }
}
