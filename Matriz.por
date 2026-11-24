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
//-----------------------------------------------------------------------
programa {
  inclua biblioteca Util --> util
  funcao inicio() {
    inteiro matriz [3] [3], i, j
    inteiro soma = 0
      para(i=0; i<3; i++){
        para(j=0; j<3; j++){
        matriz [i] [j] = util.sorteia (1,9)
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
//-----------------------------------------------------------------------
programa {
  funcao inicio() {
    inteiro identidade[3][3]
    inteiro i, j
    para(i=0; i<3; i++){
      para(j=0; j<3; j++){
        se(i == j){
          identidade[i][j] = 1
        }
        senao{
          identidade[i][j] = 0
        }
      }
    }
    escreva("\t<<<MATRIZ IDENTIDADE>>>\n")
    para(i=0; i<3; i++){
      para(j=0; j<3; j++){
        escreva("\t",identidade[i][j])
      }
      escreva("\n")
    }
  }
}
//-----------------------------------------------------------------------
programa {
  funcao inicio() {
    inteiro matriz[4][4]
    inteiro i, j
    inteiro soma, produto, maior
    soma = 0
    produto = 1
    para(i=0; i<4; i++){
      para(j=0; j<4; j++){
        escreva("Insira os valores das posições [", i,"][", j,"]: ")
        leia(matriz[i][j])
        se(i == j){
          soma += matriz[i][j]
        }
        se(i == 1){
          produto *= matriz[i][j]
        }
      }
    }
    maior = matriz[0][2]
    para(i=0; i<4; i++){
      se(matriz[i][2] > maior){
        maior = matriz[i][2]
      }
    }
    para(i=0; i<4; i++){
      para(j=0; j<4; j++){
        escreva("\t", matriz[i][j], " ")
      }
      escreva("\n")
    }
    escreva("A soma de todos os elementos da diagonal principal equivale a: ", soma)
    escreva("\nO produto dos elementos da segunda linha [1][x] é: ", produto)
    escreva("\nO maior número da terceira coluna [x][2] é: ", maior)
  }
}
