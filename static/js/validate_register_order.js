document.getElementById("botaoPesquisarOS").addEventListener("click", function() {
    var orderCode = document.getElementById("listaCodigoOS").value;
    var patientName = document.getElementById("ListaNomePacienteOS").value;
    var orderDate = document.getElementById("ListaDateOS").value;

    var data = {
        OrderCode: orderCode,
        PatientName: patientName,
        OrderDate: orderDate
    };

    fetch("/search_orders", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        var tableBody = document.getElementById("tabela-ordem-servico-info");
        tableBody.innerHTML = ""; // Limpar tabela

        if (data.orders && data.orders.length > 0) {
            data.orders.forEach(order => {
                var row = document.createElement("tr");

                var orderCodeCell = document.createElement("th");
                orderCodeCell.scope = "row";
                orderCodeCell.textContent = order.order_code;
                row.appendChild(orderCodeCell);

                var patientNameCell = document.createElement("td");
                patientNameCell.textContent = order.patient_name;
                row.appendChild(patientNameCell);

                var orderDateCell = document.createElement("td");
                orderDateCell.textContent = order.order_date;
                row.appendChild(orderDateCell);

                var actionsCell = document.createElement("td");
                var viewButton = document.createElement("button");
                viewButton.className = "btn btn-secondary";
                viewButton.textContent = "Visualizar";
                viewButton.setAttribute("data-bs-toggle", "modal");
                viewButton.setAttribute("data-bs-target", "#visualizarModal");
                actionsCell.appendChild(viewButton);
                row.appendChild(actionsCell);

                tableBody.appendChild(row);
            });
        } else {
            var row = document.createElement("tr");
            var noResultsCell = document.createElement("td");
            noResultsCell.colSpan = 4;
            noResultsCell.textContent = "Nenhum resultado encontrado.";
            row.appendChild(noResultsCell);
            tableBody.appendChild(row);
        }
    })
    .catch(error => {
        console.error("Error fetching orders:", error);
    });
});