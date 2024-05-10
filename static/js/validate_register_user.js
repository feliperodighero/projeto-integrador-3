function goBack() {
  window.location.href = '/select_user_patient';
}

function validateUsername() {
  var username = document.getElementById("UserName").value;
  var regex = /^[a-zA-Z\u00C0-\u00FF]+$/; // Regex para letras

  if (!regex.test(username)) {
    alert(
      "Nome do cliente inválido. Por favor, insira apenas letras, com ou sem acentos."
    );
    return false;
  }
  return true;
}

function validatePassword() {
  var password = document.getElementById("UserPassword").value;
  var confirmPassword = document.getElementById("UserConfirmPassword").value;

  if (password != confirmPassword) {
    alert("As senhas não coincidem. Por favor, insira novamente.");
    return false;
  }
  return true;
}

function validateCPF() {
  var cpf = document.getElementById("UserCpf").value;
  var regex = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/; // Regex para o formato XXX.XXX.XXX-XX

  if (!regex.test(cpf)) {
    alert("CPF inválido. Por favor, insira no formato XXX.XXX.XXX-XX.");
    return false;
  }
  return true;
}

function validatePhoneNumber() {
  var phoneNumber = document.getElementById("UserNumberPhone").value;
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
  var birthDate = new Date(document.getElementById("UserDateBirth").value);
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
  } else if (age < 16) {
    alert("O usuário deve ter pelo menos 16 anos.");
    return false;
  }
  return true;
}

function validateCRM() {
  var crm = document.getElementById("UserCrm").value;
  var regex = /^\d{6}$/; // Regex para exatamente 6 números

  if (!regex.test(crm)) {
    alert("CRM inválido. Por favor, insira exatamente 6 números.");
    return false;
  }
  return true;
}

function validateCargo() {
  var cargo = document.getElementById("UserCodeCarg").value;

  if (cargo != 1 && cargo != 2) {
    alert(
      "Cargo inválido. Por favor, insira 1 para dentista ou 2 para secretário."
    );
    return false;
  }
  return true;
}

function validateStreet() {
  var street = document.getElementById("UserStreet").value;
  var regex = /^[a-zA-Z0-9\s]+$/; // Regex para letras e espaços

  if (!regex.test(street)) {
    alert("Rua inválida. Por favor, insira apenas letras e números.");
    return false;
  }
  return true;
}

function validateHouseNumber() {
  var houseNumber = document.getElementById("UserNumberHouse").value;
  var regex = /^[a-zA-Z0-9]+$/; // Regex para letras e números

  if (!regex.test(houseNumber)) {
    alert("Número inválido. Por favor, insira apenas letras e números, sem caracteres especiais.");
    return false;
  }
  return true;
}


function validateNeighborhood() {
  var neighborhood = document.getElementById("UserNeighborhood").value;
  var regex = /^[a-zA-Z0-9\s]+$/; // Regex para letras e espaços

  if (!regex.test(neighborhood)) {
    alert("Bairro inválido. Por favor, insira apenas letras, números e espaços.");
    return false;
  }
  return true;
}
