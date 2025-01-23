**GOFFI_MKDIR** é um utilitário executável que cria estruturas de pastas e arquivos com base em uma sintaxe personalizada. Ideal para desenvolvedores que precisam configurar rapidamente projetos organizados.

---

## Como usar

1. Baixe o executável **GOFFI_MKDIR**.
2. Abra o terminal ou prompt de comando.
3. Execute o comando no formato:
   ```bash
   GOFFI_MKDIR.exe folder{subfolder1,subfolder2{subsubfolder1,subsubfolder2}}
   ```
4. O programa criará a estrutura conforme especificado. Exemplo:
   ```
   folder/
   ├── subfolder1/
   ├── subfolder2/
       ├── subsubfolder1/
       └── subsubfolder2/
   ```

---

### Para criar arquivos
- Use extensões para criar arquivos automaticamente:
  ```bash
  GOFFI_MKDIR.exe folder{file1.txt,subfolder{file2.js}}
  ```
  Resultado:
  ```
  folder/
  ├── file1.txt
  └── subfolder/
      └── file2.js
  ```

---

## Adicionando o **GOFFI_MKDIR** às variáveis de ambiente (Windows)

1. **Copie o caminho do executável**  
   Coloque o executável `GOFFI_MKDIR.exe` em uma pasta fixa, por exemplo:  
   ```
   C:\Ferramentas\Goffi
   ```

2. **Abra o Painel de Controle**  
   - Pesquise por **"Variáveis de Ambiente"** no menu Iniciar e clique em **Editar as variáveis de ambiente do sistema**.

3. **Edite as Variáveis do Sistema**  
   - Na janela **Propriedades do Sistema**, clique no botão **Variáveis de Ambiente**.
   - Na seção **Variáveis do sistema**, selecione a variável chamada `Path` e clique em **Editar**.

4. **Adicione o Caminho do Executável**  
   - Clique em **Novo** e insira o caminho onde está o executável, por exemplo:  
     ```
     C:\Ferramentas\Goffi
     ```
   - Confirme clicando em **OK** em todas as janelas.

5. **Teste no Prompt de Comando**  
   - Abra um novo prompt de comando e digite:  
     ```bash
     GOFFI_MKDIR.exe
     ```
   - Se aparecer a ajuda ou uma mensagem de erro relacionada à falta de argumentos, a configuração foi feita corretamente.

---

## Recursos
- **Hierarquia Recursiva:** Criação automática de subpastas aninhadas.
- **Arquivos e Pastas:** Detecta automaticamente arquivos (com extensão) e pastas.
- **Fácil de Usar:** Sintaxe intuitiva e suporte para projetos complexos.

