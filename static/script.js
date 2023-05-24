document.getElementById('cadastro').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário

    // Obter os valores dos campos de entrada
    let codigo = Number(document.getElementById('codigo').value);
    const nome = document.getElementById('nome').value;
    const tarifa = Number(document.getElementById('tarifa').value);
    const ar_condicionado = document.getElementById('ar').value
    const integracao = document.getElementById('integracao').value


    // Dados que serão enviados para a API Flask
    const dados = {
        codigo: codigo,
        nome: nome,
        tarifa: tarifa,
        ar_condicionado: ar_condicionado,
        integracao: integracao
    };

    // Opções da solicitação POST
    const opcoes = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(dados)
    };

    // URL da API Flask
    const url = 'http://127.0.0.1:5000/linha';

    // Enviar solicitação fetch
    fetch(url, opcoes)
      .then(response => response.json())
      .then(data => {
        // Manipular a resposta da API21
        console.log(data);
        alert('Linha Cadastrada')
      })
      .catch(error => {
        // Lidar com erros
        console.error('Erro:', error);
        alert('Erro com o servidor')
      });
  });
