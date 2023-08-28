 Construirei uma aplicação em Python que ofereça um menu com 5 opções ao usuário. As Opções são as seguintes:
				
    1) Cliente:
					a) Essa opção irá oferecer ao usuário a opção de realizar um CRUD com o Cliente. Deve ser exibido as seguintes opções:
						i) Cadastrar Cliente:
							Um. Os campos necessários para cadastrar um cliente são: ID, Nome, CPF, RG, Data Nascimento, CEP, Logradouro, Complemento, Bairro, Cidade, Estado e Número residência.
							Dois. Os campos do cliente devem ser validados com as validações construídas durante as aulas:
								Primeiro. CPF, RG, CEP e DATA.
						ii) Consultar Cliente:
						iii) Atualizar Cliente:
						iv) Deletar Cliente:
					b) O cliente deve ser construído seguindo o modelo do script que foi passado no repositório do GitHub. 
				
    2) Ordem:
					a) A ordem no sistema representa uma ordem de compra de uma ação. Ao selecionar essa opção deve ser exibido ao usuário a opção de:
						i) Cadastrar ordem de compra:
							Os campos necessários para cadastrar uma ordem são: ID, Nome, Ticket, Valor Compra, Quantidade Compra, Data Compra e ID do Cliente.
				
    3) Realizar análise da carteira:
					a) A opção de análise irá exibir ao usuário um gráfico utilizando a biblioteca Matplotlib contendo as informações das ações cadastradas no banco de dados de determinado usuário. Essa determinação deve ocorrer através da solicitação do CPF do Cliente.
				
    4) Consultar relatório de ação específica e enviá-la para o S3:
					a) Essa opção permite:
						i) Oferecer ao cliente uma opção para consultar dados de qualquer ação, para que ele possa se informar sobre o seu status atual.
      						i) Enviar o relatório diretamente para um bucket no S3 (serviço oferecido pela AWS)
				
    5) Sair:
					a) Opção sair irá encerrar a aplicação.

	Obs.:
		□ Todas as opções do menu devem perguntar ao usuário se ele deseja voltar ao menu principal ou sair da aplicação.
		□ O código deve ser escrito utilizando os princípios ensinados em aula da orientação a objetos.
