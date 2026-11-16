  programa {
  // leitura de matriz 3 x 3, soma dos numeros da matriz e exibição de tabela
  funcao inicio() {
    inteiro matriz [3] [3], i, j
    inteiro soma = 0
    para(i=0; i<3; i++){
      para(j=0; j<3; j++){
        escreva("Digite o valor da linha [", i+1, "] e coluna [", j+1,"]: ")
        leia(matriz [i] [j])
        soma = soma + matriz [i] [j]
      }
    }
    escreva("A soma dos números da matriz é: ", soma)
    escreva("\n\n<<<TABELA MATRIZ>>>\n")
    para(i=0; i<3; i++){
      para(j=0; j<3; j++){
        escreva("\t", matriz[i] [j], "\t")
      }
      escreva("\n")
    }
  }
}
