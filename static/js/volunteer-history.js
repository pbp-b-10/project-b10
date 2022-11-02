
const template = document.getElementsByTagName('template')[0];

function getVolunteers() {
    return fetch("/api/volunteer").then((res) => {
    return res.json()
    })
}

async function refreshVolunteers() {
    const volunteers = await getVolunteers()
    const table =  document.getElementById("data");
    table.innerHTML = "";
    volunteers.forEach((item) => {
        const duplicate = template.cloneNode(true).content
        /** @type {HTMLElement[]} */
        const fields = duplicate.querySelectorAll('td')
        fields[0].innerHTML = item.title
        fields[1].innerHTML = item.divisi
        fields[2].innerHTML = item.amount
        fields[3].innerHTML = `<button class="delete-button"
                onmouseover="this.style.backgroundColor='#E14D2A';"
                onmouseout="this.style.backgroundColor='#F96666';"
                onclick="cancelVolunteer(${item.id})">X</button>`
        table.appendChild(duplicate)
    })
}

function cancelVolunteer(id) {
    $.ajax({
        url: `volunteer/${id}/delete`,
        type: "DELETE",
        success: function() {
            $(`#${id}`).remove();
        }
    }).then(refreshVolunteers)
}

refreshVolunteers()