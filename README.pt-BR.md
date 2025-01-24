🌍 [Read in English](README.md)

# Dashboard de Suporte ao Cliente

Aplicação interativa desenvolvida em Streamlit para analisar e visualizar o desempenho de um centro de atendimento ao cliente. Este dashboard permite que os usuários monitorem métricas chave, como chamadas recebidas, chamadas atendidas e taxas de atendimento, além de gerar insights automatizados por meio de inteligência artificial.

## Funcionalidades

- **Visualização de Métricas**: Exibe métricas como chamadas recebidas, chamadas atendidas e taxas de atendimento de forma clara e concisa.
- **Gráficos Interativos**: Apresenta gráficos de linha e barras para visualizar tendências ao longo do tempo e a distribuição de chamadas.
- **Relatório AI**: Gera um relatório de insights baseado em dados históricos, fornecendo recomendações para melhorar o desempenho do atendimento.

## Técnologias Utilizadas

- [Streamlit](https://streamlit.io) - Para construção da aplicação web.
- [Pandas](https://pandas.pydata.org) - Para manipulação e análise de dados.
- [dotenv](https://pypi.org/project/python-dotenv/) - Para gerenciamento de variáveis de ambiente.
- [Gemini API](https://ai.google.dev/gemini-api/docs) - Para geração de insights utilizando inteligência artificial.

## Passos para instalação e execução

1. Clone o repositório:

```bash
   git clone https://github.com/felipeclarindo/customer-support-dashboard.git
```

2. Entre no diretorio:

```bash
    cd customer-support-dashboard
```

3. Crie um ambiente virtual:

```bash
python -m venv .venv
```

4. Execute o arquivo `.bat` em `.venv/Scripts/activate.bat`.

5. Instale as dependencias:

```bash
    pip install -r requirements.txt
```

6. Crie um arquivo `.env` na raiz do projeto baseado no arquivo [.env example](./.env.example) e adicione sua chave da API do OpenAI:

```bash
    GEMINI_API_KEY=sua_chave_da_api
```

7. Execute o dashboard:

```bash
    streamlit run ./main.py
```

8. O dashboard será aberto no seu navegador padrão em:
   - `http://localhost:8501`

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## Licença

Este projeto está licenciado sob a [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
