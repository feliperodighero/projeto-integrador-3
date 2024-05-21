document.addEventListener('DOMContentLoaded', function () {
    const searchID = document.getElementById('SearchID');
    const searchCnpj = document.getElementById('SearchCnpj');
    const searchName = document.getElementById('SearchName');
    const botaoPesquisar = document.getElementById('botao-edit-laboratory');

    const searchFields = [searchID, searchCnpj, searchName];
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

    document.getElementById('search-cnpj').addEventListener('click', function () {
        disableAllFields();
        searchCnpj.disabled = false;
    });

    document.getElementById('search-name').addEventListener('click', function () {
        disableAllFields();
        searchName.disabled = false;
    });

    botaoPesquisar.addEventListener('click', function () {
        if (searchID.value || searchCnpj.value || searchName.value) {
            enableOtherFields();
        } else {
            alert('Por favor, preencha um dos campos de busca.');
        }
    });

    disableAllFields();
});

document.addEventListener('DOMContentLoaded', function () {
    const searchID = document.getElementById('SearchID');
    const searchCnpj = document.getElementById('SearchCnpj');
    const searchName = document.getElementById('SearchName');
    const botaoEditUser = document.getElementById('botao-edit-user');

    function disableAllFields() {
        [searchID, searchCnpj, searchName].forEach(field => {
            field.disabled = true;
            field.value = '';
        });
    }

    function enableFormFields() {
        document.querySelectorAll('#editForm input').forEach(input => input.disabled = false);
    }

    document.getElementById('search-id').addEventListener('click', function () {
        disableAllFields();
        searchID.disabled = false;
    });

    document.getElementById('search-cnpj').addEventListener('click', function () {
        disableAllFields();
        searchCnpj.disabled = false;
    });

    document.getElementById('search-name').addEventListener('click', function () {
        disableAllFields();
        searchName.disabled = false;
    });

    botaoEditUser.addEventListener('click', function (event) {
        const isValid = searchID.value || searchCnpj.value || searchName.value;
        if (!isValid) {
            event.preventDefault();
            alert('Por favor, preencha um dos campos de busca.');
        }
    });

    disableAllFields();
});