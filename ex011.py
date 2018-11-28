larg = float(input("Digite a largura da parede"))
alt = float(input('Digite a altura da parede'))
area = larg * alt
tinta = area / 2
print('Sua parede tem {} de largura e {} de altura'.format(larg, alt))
print('A area em metros quadrados é de {:.2f}'.format(area))
print('Você precisa de {:.2f} litros de tinta'.format(tinta))


