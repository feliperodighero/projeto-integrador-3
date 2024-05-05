function goBack() {
    window.location.href = '/select_user_patient';
}

function validateClientname() {
    var clientname = document.getElementById("ClientName").value;
    var regex = /^[a-zA-Z]+$/; // Regex para letras sem acentos

    if (!regex.test(clientname)) {
      alert(
        "Nome do cliente inválido. Por favor, insira apenas letras sem acentos."
      );
      return false;
    }
    return true;
  }

  function validateCPF() {
    var cpf = document.getElementById("ClientCpf").value;
    var regex = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/; // Regex para o formato XXX.XXX.XXX-XX

    if (!regex.test(cpf)) {
      alert("CPF inválido. Por favor, insira no formato XXX.XXX.XXX-XX.");
      return false;
    }
    return true;
  }

  function validatePhoneNumber() {
    var phoneNumber = document.getElementById("ClientNumberPhone").value;
    var regex = /^\(\d{2}\)\d{5}-\d{4}$/; // Regex para o formato (XX)XXXXX-XXXX

    if (!regex.test(phoneNumber)) {
      alert(
        "Número de telefone inválido. Por favor, insira no formato (XX)XXXXX-XXXX."
      );
      return false;
    }
    return true;
  }

  function validateBirthDate() {
    var birthDate = new Date(document.getElementById("ClientDateBirth").value);
    var today = new Date();
    var age = today.getFullYear() - birthDate.getFullYear();
    var m = today.getMonth() - birthDate.getMonth();

    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }

    if (birthDate > today) {
      alert(
        "A data de nascimento está inválida. Por favor, insira uma data de nascimento válida."
      );
      return false;
    }

    return true;
  }

  function validateStreet() {
    var street = document.getElementById("ClientStreet").value;
    var regex = /^[a-zA-Z\s]+$/; // Regex para letras e espaços

    if (!regex.test(street)) {
      alert("Rua inválida. Por favor, insira apenas letras.");
      return false;
    }
    return true;
  }

  function validateHouseNumber() {
    var houseNumber = document.getElementById("ClientNumberHouse").value;
    var regex = /^\d+$/; // Regex para números

    if (!regex.test(houseNumber)) {
      alert("Número da casa inválido. Por favor, insira apenas números.");
      return false;
    }
    return true;
  }

  function validateNeighborhood() {
    var neighborhood = document.getElementById("ClientNeighborhood").value;
    var regex = /^[a-zA-Z\s]+$/; // Regex para letras e espaços

    if (!regex.test(neighborhood)) {
      alert("Bairro inválido. Por favor, insira apenas letras.");
      return false;
    }
    return true;
  }
