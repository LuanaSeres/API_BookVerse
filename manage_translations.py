import polib
import os

# Caminho onde os arquivos de tradução serão salvos
locale_path = 'locale/pt_BR/LC_MESSAGES/'
os.makedirs(locale_path, exist_ok=True)

# Criar ou carregar um arquivo .po existente
po_filepath = os.path.join(locale_path, 'django.po')
if os.path.exists(po_filepath):
    po = polib.pofile(po_filepath)
else:
    po = polib.POFile()

# Adicionar metadados se o arquivo .po for novo
if not po.metadata:
    po.metadata = {
        'Project-Id-Version': '1.0',
        'Report-Msgid-Bugs-To': 'you@example.com',
        'POT-Creation-Date': '2024-06-14 12:00+0000',
        'PO-Revision-Date': '2024-06-14 12:00+0000',
        'Last-Translator': 'You <you@example.com>',
        'Language-Team': 'Portuguese',
        'Language': 'pt_BR',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Content-Transfer-Encoding': '8bit',
    }

# Adicionar entradas de tradução
entries = [
    {'msgid': 'Title', 'msgstr': 'Título'},
    {'msgid': 'Author', 'msgstr': 'Autor'},
    {'msgid': 'Genre', 'msgstr': 'Gênero'},
    {'msgid': 'Description', 'msgstr': 'Descrição'},
    {'msgid': 'Rating', 'msgstr': 'Avaliação'},
    {'msgid': 'Comment', 'msgstr': 'Comentário'},
    {'msgid': 'Priority', 'msgstr': 'Prioridade'},
    {'msgid': 'Status', 'msgstr': 'Status'},
    {'msgid': 'Progress', 'msgstr': 'Progresso'},
    {'msgid': 'Username', 'msgstr': 'Nome de usuário'},
    {'msgid': 'Email', 'msgstr': 'Email'},
    {'msgid': 'Password', 'msgstr': 'Senha'},
    {'msgid': 'This field is required.', 'msgstr': 'Este campo é obrigatório.'},
    {'msgid': 'Enter a valid username.', 'msgstr': 'Digite um nome de usuário válido.'},
    {'msgid': 'Enter a valid email address.', 'msgstr': 'Digite um endereço de email válido.'},
    {'msgid': 'Enter a valid password.', 'msgstr': 'Digite uma senha válida.'},
]

for entry in entries:
    # Verificar se a entrada já existe
    if not po.find(entry['msgid']):
        po.append(polib.POEntry(msgid=entry['msgid'], msgstr=entry['msgstr']))

# Salvar o arquivo .po
po.save(po_filepath)

# Compilar o arquivo .po para .mo
mo_filepath = os.path.join(locale_path, 'django.mo')
po.save_as_mofile(mo_filepath)

print(f"Arquivo .po salvo em: {po_filepath}")
print(f"Arquivo .mo salvo em: {mo_filepath}")
