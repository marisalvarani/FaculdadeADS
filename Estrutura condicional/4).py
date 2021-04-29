P1 = float(input())
P2 = float(input())
P3 = float(input())
F = float(input())
media = ((P1*2)+(P2*2)+(P3*3))/7
frequencia = F*100
if F<0.75:
    print("Frequencia: ", "{:.0f}".format(frequencia),"%")
    print("Media final: ", "{:.1f}".format(media))
    print("Aluno reprovado por faltas!")
elif media>9.0 and F>=0.75:
    print("Frequencia: ", "{:.0f}".format(frequencia),"%")
    print("Media final: ", "{:.1f}".format(media))
    print("Aluno aprovado com louvor!")
elif media>=6.0 and media<=9.0 and F>=0.75:
    print("Frequencia: ", "{:.0f}".format(frequencia),"%")
    print("Media final: ", "{:.1f}".format(media))
    print("Aluno aprovado")
elif media>=4.0 and media<6.0 and F>=0.75:
    print("Frequencia: ", "{:.0f}".format(frequencia),"%")
    print("Media final: ", "{:.1f}".format(media))
    print("Aluno de recuperação!")
else:
    print("Frequencia: ", "{:.0f}".format(frequencia),"%")
    print("Media final: ", "{:.1f}".format(media))
    print("Aluno reprovado!")

