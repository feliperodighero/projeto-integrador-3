(() => {
  "use strict";

  const forms = document.querySelectorAll(".needs-validation");

  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();

function goBack() {
  window.location.href = "/select_user_patient";
}

function validateClientname() {
  var clientname = document.getElementById("ClientName").value;
  var regex = /^[a-zA-Z\u00C0-\u00FF]+$/; // Regex para letras com e sem acentos
  var clientError = document.getElementById("ClientError");

  if (!regex.test(clientname)) {
    clientError.style.display = "block";
    return false;
  } else {
    clientError.style.display = "none";
    return true;
  }
}

function validateCPF() {
  var cpf = document.getElementById("ClientCpf").value;
  var regex = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/; // Regex para o formato XXX.XXX.XXX-XX
  var clientcpfError = document.getElementById("ClientCPFError");

  if (!regex.test(cpf)) {
    clientcpfError.style.display = "block";
    return false;
  } else {
    clientcpfError.style.display - "none";
    return true;
  }
}

function validateCEP() {
  var cep = document.getElementById("ClientCep").value;
  var regex = /^[0-9]{5}-[0-9]{3}$/;
  var clientcepError = document.getElementById("ClientCEPError");

  if (cep === "" || !regex.test(cep)) {
    clientcepError.style.display = "block";
    return false;
  } else {
    clientcepError.style.display = "none";
    return true;
  }
}

function validatePhoneNumber() {
  var phoneNumber = document.getElementById("ClientNumberPhone").value;
  var regex = /^\(\d{2}\)\d{5}-\d{4}$/; // Regex para o formato (XX)XXXXX-XXXX
  var clienttelefoneError = document.getElementById("ClientTelefoneError");

  if (!regex.test(phoneNumber)) {
    clienttelefoneError.style.display = "block";
    return false;
  } else {
    clienttelefoneError.style.display = "none";
    return true;
  }
}

function validateBirthDate() {
  var birthDate = document.getElementById("ClientDateBirth").value;
  var clientDataNascError = document.getElementById("ClientDataNascError");

  if (!birthDate) {
    clientDataNascError.style.display = "block";
    return false;
  } else {
    clientDataNascError.style.display = "none";
    return true;
  }
}

function validateForm() {
  return (
    validateClientname() &&
    validateCPF() &&
    validatePhoneNumber() &&
    validateBirthDate() &&
    validateStreet() &&
    validateHouseNumber() &&
    validateNeighborhood()
  );
}

document.getElementById("complementos-cards").onsubmit = function (event) {
  if (!validateForm()) {
    event.preventDefault();
    event.stopPropagation();
  }
};

function validateBirthDate() {
  var birthDate = document.getElementById("ClientDateBirth").value;
  var clientDataNascError = document.getElementById("ClientDataNascError");

  if (!birthDate) {
    clientDataNascError.style.display = "block";
    return false;
  } else {
    clientDataNascError.style.display = "none";
    return true;
  }
}

function validateStreet() {
  var street = document.getElementById("ClientStreet").value;
  var regex = /^[a-zA-Z0-9\s]+$/; // Regex para letras e espaços
  var clientruaError = document.getElementById("ClientRuaError");

  if (!regex.test(street)) {
    clientruaError.style.display = "block";
    return false;
  } else {
    clientruaError.style.display = "none";
    return true;
  }
}

function validateHouseNumber() {
  var houseNumber = document.getElementById("ClientNumberHouse").value;
  var regex = /^[a-zA-Z0-9]+$/; // Regex para números
  var clientnumeroError = document.getElementById("ClientNumeroError");

  if (!regex.test(houseNumber)) {
    clientnumeroError.style.display = "block";
    return false;
  } else {
    clientnumeroError.style.document = "none";
    return true;
  }
}

function validateNeighborhood() {
  var neighborhood = document.getElementById("ClientNeighborhood").value;
  var regex = /^[a-zA-Z0-9\s]+$/; // Regex para letras, números e espaços
  var clientbairroError = (document.getElementById = "ClientBairroError");
  if (!regex.test(neighborhood)) {
    clientbairroError.style.display = "block";
    return false;
  } else {
    clientbairroError.style.display = "none";
    return true;
  }
}
