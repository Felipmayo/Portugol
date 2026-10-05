programa {
  funcao real MediaBoletim(real nota1, real nota2){
    retorne (nota1 + nota2) / 2
  }
  funcao inicio() {
    real nota1, nota2, media
    escreva("Insira a primeira nota: ")
    leia(nota1)

    escreva("Insira a segunda nota: ")
    leia(nota2)


    media = MediaBoletim(nota1, nota2)

    se(media >= 60 e media <= 100){
      escreva("APROVADO!!")
    }
    senao se(media < 60 e media >= 30){
      escreva("RECUPERAÇÃO!!")
    }
    senao se(media < 30){
      escreva("REPROVADO!!")
    }
    senao{
      escreva("Notas inválidas!!")
    }
    
  }
}
