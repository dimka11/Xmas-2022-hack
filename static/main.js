document.addEventListener("DOMContentLoaded", function (event) {
    get_status();
    get_advised();
    get_shares_last();
});

function get_shares_last() {
    const myHeaders = new Headers();

    const statusRequest = new Request('get_shares_last', {
        method: 'GET',
        headers: myHeaders,
        mode: 'cors',
        cache: 'default',
    });

    fetch(statusRequest)
        .then((response) => response.json())
        .then((resp) => {
            console.log(resp)

            const shares_last = document.getElementById("shares_last");

            while (shares_last.firstChild) {
                shares_last.removeChild(shares_last.firstChild);
            }
            for (let item in resp) {
                console.log(item, resp[item][0], resp[item][1])
                let li = document.createElement("li");
                li.setAttribute("class", "list-group-item")
                li.appendChild(document.createTextNode(item + " " + resp[item][0] + " "))
                let span = document.createElement("span")

                if (resp[item][1] >= 0) {
                    span.setAttribute("class", "badge bg-primary")
                    span.appendChild(document.createTextNode("-" + resp[item][1]))
                } else {
                    span.setAttribute("class", "badge bg-danger")
                    span.appendChild(document.createTextNode(resp[item][1]))
                }

                li.appendChild(span)
                shares_last.appendChild(li)
            }
        })
        .catch((error) => {
            console.log(error)
        });
}

function get_advised() {
    const myHeaders = new Headers();

    const statusRequest = new Request('get_advised', {
        method: 'GET',
        headers: myHeaders,
        mode: 'cors',
        cache: 'default',
    });

    fetch(statusRequest)
        .then((response) => response.json())
        .then((resp) => {
            // console.log(resp.shares)

            const select = document.getElementById("sharesAdvised");

            while (select.firstChild) {
                select.removeChild(select.firstChild);
            }

            for (let item of resp.shares) {
                const option = document.createElement("option");
                option.appendChild(document.createTextNode(item));
                select.appendChild(option)
            }
        })
        .catch((error) => {
            console.log(error)
        });
}

function get_status() {
    const myHeaders = new Headers();

    const statusRequest = new Request('status', {
        method: 'GET',
        headers: myHeaders,
        mode: 'cors',
        cache: 'default',
    });

    fetch(statusRequest)
        .then((response) => response.json())
        .then((resp) => {
            console.log(resp)
        })
        .catch((error) => {
            console.log(error)
        });
}

function get_confirm() {
    const myHeaders = new Headers();

    const statusRequest = new Request('confirm', {
        method: 'GET',
        headers: myHeaders,
        mode: 'cors',
        cache: 'default',
    });

    fetch(statusRequest)
        .then((response) => response.json())
        .then((resp) => {
            console.log(resp)
        })
        .catch((error) => {
            console.log(error)
        });
}

function form_post(object) {
    const myHeaders = new Headers({'content-type': 'application/json'});

    const postRequest = new Request('form_post', {
        method: 'POST',
        headers: myHeaders,
        mode: 'cors',
        cache: 'default',
        body: JSON.stringify(object)
    });

    fetch(postRequest)
        .then((response) => response.json())
        .then((resp) => {
            console.log(resp)
            updateRespList(resp)
        });
}

function updateSharesLast(resp) {
    const shares_last_elem = document.getElementById("shares_last")
    // fill list of shares
}


function updateRespList(resp) {
    const shares_last_elem = document.getElementById("respList")
    while (shares_last_elem.firstChild) {
        shares_last_elem.removeChild(shares_last_elem.firstChild);
    }

    const resp_count_objects = Object.keys(resp).length;
    const resp_keys = Object.keys(resp)

    for (const key in resp) {
        if (resp.hasOwnProperty(key)) {
            const ul = document.getElementById("respList");
            const li = document.createElement("li");
            const span = document.createElement("span");
            li.appendChild(document.createTextNode(key));
            li.setAttribute("class", "list-group-item");
            span.setAttribute("class", "badge bg-black");
            span.appendChild(document.createTextNode(resp[key]));
            li.appendChild(span)
            ul.appendChild(li);
        }
    }


    // for (const property in resp) {
    //     console.log(resp[property])
    // const ul = document.getElementById("respList");
    // const li = document.createElement("li");
    // const span = document.createElement("span");
    // li.appendChild(document.createTextNode(property));
    // li.setAttribute("class", "list-group-item");
    // span.setAttribute("class", "badge bg-black");
    // span.appendChild(document.createTextNode(resp[property]));
    // li.appendChild(span)
    // ul.appendChild(li);
    // }
}


function getSelectValues(select) {
    var result = [];
    var options = select && select.options;
    var opt;

    for (var i = 0, iLen = options.length; i < iLen; i++) {
        opt = options[i];

        if (opt.selected) {
            result.push(opt.value || opt.text);
        }
    }
    return result;
}


function confirm() {
    const elem = document.getElementById("confirmBtn")
    // elem.style.backgroundColor = 'red';
    // elem.innerHTML = 'Ждите! Запрос идет'

    const risk_elem = document.getElementById("riskSelect")
    const value_risk = risk_elem.value;
    const risk_text = risk_elem.options[risk_elem.selectedIndex].text;

    const period_elem = document.getElementById("periodSelect")
    const value_period = period_elem.value;
    const period_text = period_elem.options[period_elem.selectedIndex].text;

    const shares_adv_elem = document.getElementById("sharesAdvised")
    const shares_adv_selected = getSelectValues(shares_adv_elem)
    // const value_adv_shares = shares_adv_elem.value;
    // const shares_adv_text = shares_adv_elem.options[shares_adv_elem.selectedIndex].text;

    form_post({risk: risk_text, period: period_text, selectedShares: shares_adv_selected})


    // const ul = document.getElementById("respList");
    // const li = document.createElement("li");
    // const span = document.createElement("span");
    // li.appendChild(document.createTextNode("VVVV "));
    // li.setAttribute("class", "list-group-item");
    // span.setAttribute("class", "badge bg-black");
    // span.appendChild(document.createTextNode("100"));
    // li.appendChild(span)
    // ul.appendChild(li);
    //
    // elem.innerHTML = 'Подобрать акции'
}