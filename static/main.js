document.addEventListener("DOMContentLoaded", function (event) {
    get_status()
});

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
        });
}

function post_test() {
    const myHeaders = new Headers();

    const object = { status: 'test' };

    const statusRequest = new Request('post_test', {
        method: 'POST',
        headers: myHeaders,
        mode: 'cors',
        cache: 'default',
        body: JSON.stringify(object)
    });

    fetch(statusRequest)
        .then((response) => response.json())
        .then((resp) => {
            console.log(resp)
        });
}


function confirm() {
    const elem = document.getElementById("confirmBtn")
    // elem.style.backgroundColor = 'red';
    elem.innerHTML = 'Ждите! Запрос идет'

    get_confirm()
    post_test()



    const risk_elem = document.getElementById("riskSelect")


    var value = risk_elem.value;
    var text = risk_elem.options[risk_elem.selectedIndex].text;


    const period_elem = document.getElementById("periodSelect")
    const shares_adv_elem = document.getElementById("sharesAdvised")
    const shares_last_elem = document.getElementById("shares_last")




    const ul = document.getElementById("respList");
    const li = document.createElement("li");
    const span = document.createElement("span");
    li.appendChild(document.createTextNode("VVVV "));
    li.setAttribute("class", "list-group-item");
    span.setAttribute("class", "badge bg-black");
    span.appendChild(document.createTextNode("100"));
    li.appendChild(span)
    ul.appendChild(li);

    elem.innerHTML = 'Подобрать акции'
}