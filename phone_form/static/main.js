function sendPhoneNumber(){
    const parentElement = document.querySelector('.userdata-container');
    parentElement.innerHTML = '';

    const formData = new FormData();

    const phoneNumber = document.querySelector("#phoneNumberInput").value;
    const csrf = document.querySelector("[name=csrfmiddlewaretoken]").value;

    if (!phoneNumber) return alert("Phone Number must be provided");

    formData.append("csrfmiddlewaretoken", csrf);
    formData.append("phone_number", phoneNumber);

    fetch("/api/get-phone-number-info/", {method:"POST", body: formData})
    .then(response => response.json())
    .then(data => {
        if (data.error) return alert(data.error);
        addPhoneInfoCard(data);
    })
}

function addPhoneInfoCard(data){
    // Create the table element
    const table = document.createElement('table');
    table.classList.add('table', 'table-bordered');
    
    // Create the table head
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    
    // Add header cells
    const headerCells = [
        'Code',
        'Capacity',
        'Range',
        'Operator',
        'TIN',
        'Region',
        'RegionGAR'
    ];
    
    for (const cellText of headerCells) {
        const cell = document.createElement('th');
        cell.textContent = cellText;
        cell.scope = 'col';
        headerRow.appendChild(cell);
    }
    
    thead.appendChild(headerRow);
    
    // Create the table body
    const tbody = document.createElement('tbody');
    
    const row = document.createElement('tr');

    // Add table cells
    const tableCells = [
        data.abc,
        data.capacity,
        `${data.start} - ${data.end}`,
        data.operator,
        data.tin,
        data.region,
        data.gar_territory
    ];

    for (const cellValue of tableCells) {
        const cell = document.createElement('td');
        cell.textContent = cellValue;
        row.appendChild(cell);
    }
    
    tbody.appendChild(row);

    
    // Add head and body to the table
    table.appendChild(thead);
    table.appendChild(tbody);

    parent = document.querySelector(".userdata-container");
    parent.appendChild(table);
}
