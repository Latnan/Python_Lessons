v = float(input('Insira um valor em metros: '))
km = float(v / 1000)
hm = float(v / 100)
dam = float(v / 10)
dm = float(v * 10)
cm = float(v * 100)
mm = float(v * 1000)
print(f'O valor {v} metros corresponde a:\n'
      f' {km} quilômetros\n'
      f' {hm} hectômetros\n'
      f' {dam:.3f} decâmetros\n'
      f' {dm:.0f} decímetros\n'
      f' {cm:.0f} centímetros\n'
      f' {mm:.0f} milímetros\n')
