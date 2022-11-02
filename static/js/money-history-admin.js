async function getMoney() {
    return fetch("api/money").then((res) => res.json())
  }

  async function refreshMoney() {
        
        document.getElementById("data").innerHTML = ""
        const money = await getMoney()
        let htmlString = ''
        money.forEach((item) => {
          htmlString += `\n<tr><td> ${item.fields.donation}
                          <td> ${item.fields.date}
                          </td></tr>`
        })
        document.getElementById("data").innerHTML = htmlString
  }
  
  async function successAfterCancel() {
      refreshMoney()
      document.getElementById("success").innerHTML = ""
      htmlString = `\n<div class="alert alert-primary" role="alert">\n
                      You have canceled a donation\n
                      </div>`
      document.getElementById("success").innerHTML = htmlString
      setInterval(exitSuccess, 2500)
  }

  async function exitSuccess() {
      document.getElementById("success").innerHTML = ""
      htmlString = ``
      document.getElementById("success").innerHTML = htmlString
  }

  async function cancelMoney(pk) {
          $.ajax({
              url: `money/${pk}/delete`,
              type: "DELETE",
              success: function() {
                $(`#${pk}`).remove();
              }
          }).then(successAfterCancel)
      }

  refreshMoney()