programa {
  funcao inicio() {
    real nota1, nota2, media
    logico aprovado

    escreva("Insira a primeira nota: ")
    leia(nota1)

    escreva("Insira a segunda nota: ")
    leia(nota2)
    
    media = MediaBoletim(nota1, nota2)

    se(media >= 70 e media <= 100){
      aprovado = verdadeiro
    }
    senao{
      aprovado = falso
    } 
    
    se(aprovado){
      escreva("APROVADO!!")
    }
    senao se(media < 70 e media >= 40){
      escreva("EXAME!!")
    }
    senao se(media < 40){
      escreva("REPROVADO!!")
    }
    senao{
      escreva("Notas inválidas!!")
    }
  }
    funcao real MediaBoletim(real nota1, real nota2){
    retorne (nota1 + nota2) / 2
  }
}
