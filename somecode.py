import alina
Alina = alina.AliNA(skip_error_data = False, warn = True, gpu = False)

struct = Alina.fold('UAGCGUAGGGGAAACGCCCGGUUACAUU')
print(struct)