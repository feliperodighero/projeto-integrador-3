document.addEventListener('DOMContentLoaded', function () {
    const searchID = document.getElementById('SearchID');
    const searchCpfCnpj = document.getElementById('SearchCpfCnpj');
    const searchName = document.getElementById('SearchName');

    function disableAllFields() {
        searchID.disabled = true;
        searchCpfCnpj.disabled = true;
        searchName.disabled = true;
    }

    document.getElementById('search-id').addEventListener('click', function () {
        disableAllFields();
        searchID.disabled = false;
    });

    document.getElementById('search-cpf-cnpj').addEventListener('click', function () {
        disableAllFields();
        searchCpfCnpj.disabled = false;
    });

    document.getElementById('search-name').addEventListener('click', function () {
        disableAllFields();
        searchName.disabled = false;
    });

    disableAllFields();
});

document.addEventListener('DOMContentLoaded', function () {
    const searchID = document.getElementById('SearchID');
    const searchCpfCnpj = document.getElementById('SearchCpfCnpj');
    const searchName = document.getElementById('SearchName');
    const botaoEditUser = document.getElementById('botao-edit-user');
    const formFields = [
        document.getElementById('UserName'),
        document.getElementById('UserPassword'),
        document.getElementById('UserConfirmPassword'),
        document.getElementById('UserCpf'),
        document.getElementById('UserNumberPhone'),
        document.getElementById('UserComplement'),
        document.getElementById('UserDateBirth'),
        document.getElementById('UserCrm'),
        document.getElementById('UserCodeCarg'),
        document.getElementById('UserStreet'),
        document.getElementById('UserNumberHouse'),
        document.getElementById('UserNeighborhood'),
        document.getElementById('botao-confirmedit-user'),
        document.getElementById('botao-excluir-user')
    ];

    const searchFields = [searchID, searchCpfCnpj, searchName];

    function disableAllFields() {
        searchFields.forEach(field => {
            field.disabled = true;
            field.value = ''; // Limpa o valor do campo
        });
        formFields.forEach(field => field.disabled = true);
    }

    function enableFormFields() {
        formFields.forEach(field => field.disabled = false);
    }

    document.getElementById('search-id').addEventListener('click', function () {
        disableAllFields();
        searchID.disabled = false;
    });

    document.getElementById('search-cpf-cnpj').addEventListener('click', function () {
        disableAllFields();
        searchCpfCnpj.disabled = false;
    });

    document.getElementById('search-name').addEventListener('click', function () {
        disableAllFields();
        searchName.disabled = false;
    });

    botaoEditUser.addEventListener('click', function () {
        if (searchID.value || searchCpfCnpj.value || searchName.value) {
            enableFormFields();
        } else {
            alert('Por favor, preencha um dos campos de busca.');
        }
    });

    disableAllFields();
});
