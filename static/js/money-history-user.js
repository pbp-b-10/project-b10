async function getMoney() {
    return fetch("money/json").then((res) => res.json())
  }

  async function refreshMoney() {
        
        document.getElementById("data").innerHTML = ""
        const money = await getMoney()
        let htmlString = ''
        money.forEach((item) => {
          htmlString += `\n<tr>`
          if (user === 'staff') {
            htmlString += `<td> ${item.fields.name}`
          }
          htmlString += `<td> ${item.fields.donation} 
                          </td><td> ${item.fields.date} 
                          </td><td>  <button id="delete-button" style="font-weight:bold;
                                                                        background-color:#F96666;
                                                                        border: none;
                                                                        text-decoration: none;
                                                                        display: inline-block;"
                                                                        onmouseover="this.style.backgroundColor='#E14D2A';"
                                                                        onmouseout="this.style.backgroundColor='#F96666';"
                                                                        onclick="cancelCloth(${item.pk})"
                                                                        >X</button>
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