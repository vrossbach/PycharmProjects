from importlib import metadata

print(metadata.version('pip'))  # 20.2.4

metadados_pip = metadata.metadata('pip')

print(list(metadados_pip))

print(metadados_pip['Project-URL'])

print(len(metadata.files('pip')))

print(metadata.requires('pip'))

print(metadata.requires('matplotlib'))

print(metadata.requires('numpy'))

# Verificar se existem conflitos entre bibliotecas