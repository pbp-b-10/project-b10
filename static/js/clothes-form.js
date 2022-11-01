async function successAfterSubmit() {
    document.getElementById("success").innerHTML = ""
    htmlString = `\n<div class="alert alert-success" role="alert">\n
                    \nThank you for your donation! See your donation history <a href="/history/clothes" class="alert-link">here</a>\n
                    </div>`
    document.getElementById("success").innerHTML = htmlString
    setInterval(exitSuccess, 3500)
}

async function exitSuccess() {
    document.getElementById("success").innerHTML = ""
    htmlString = ``
    document.getElementById("success").innerHTML = htmlString
}

async function submitCloth() {
    fetch("create", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(successAfterSubmit)
    return false
}

document.getElementById("button-submit").onclick = submitCloth