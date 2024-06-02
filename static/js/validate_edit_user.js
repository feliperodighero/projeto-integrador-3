document.addEventListener('DOMContentLoaded', function () {
    const searchID = document.getElementById('SearchID');
    const searchCpfCnpj = document.getElementById('SearchCpfCnpj');
    const botaoPesquisar = document.getElementById('botao-edit-user');
    const laboratoryId = document.getElementById('UserId');

    const searchFields = [searchID, searchCpfCnpj];
    const otherFields = Array.from(document.querySelectorAll('.form-control')).filter(field => !searchFields.includes(field));

    function disableAllFields() {
        searchFields.forEach(field => {
            field.disabled = true;
            field.value = ''; // Limpa o valor do campo
        });
        otherFields.forEach(field => field.disabled = true);
    }

    function enableOtherFields() {
        otherFields.forEach(field => field.disabled = false);
    }

    document.getElementById('search-id').addEventListener('click', function () {
        disableAllFields();
        searchID.disabled = false;
    });

    document.getElementById('search-cpf-cnpj').addEventListener('click', function () {
        disableAllFields();
        searchCpfCnpj.disabled = false;
    });

    botaoPesquisar.addEventListener('click', function (event) {
        if (searchID.value || searchCpfCnpj.value) {
            // Permite que o formulário de pesquisa seja enviado
            enableOtherFields();
        } else {
            event.preventDefault();
            alert('Por favor, preencha um dos campos de busca.');
        }
    });

    disableAllFields();

    // Habilita os campos de edição após a submissão bem-sucedida
    if (laboratoryId && laboratoryId.value) {
        enableOtherFields();
    }
});